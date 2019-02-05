from apicore.ApiCoreUtil import ApiCoreUtil
from apicore.HttpCalls import HttpCalls
import os,sys,json

class UserService(ApiCoreUtil):
    deleteUser = "https://user-service-dot-premise-qa.appspot.com/api/user/v1/users/"
    getUserURL = "https://user-service-dot-premise-qa.appspot.com/api/user/v1/users/email/"
    suspendUser = "https://user-service-dot-premise-qa.appspot.com/api/user/v1/users/suspend"
    restoreUser = "https://user-service-dot-premise-qa.appspot.com/api/user/v1/users/restore"
    partialUpdateUser = "https://user-service-dot-premise-qa.appspot.com/api/user/v1/users/USERID/update-partial"
    # HttpCalls httpCall = None
    jsonFlow = "id"
    userErrorMessage = ""
    userEmailID = "email"
    userCity = "city"
    userCountry = "country"
    userState = "state"

    def getUser(self, emailID):
        premiseUserID = ""
        print("In getUser")
        try :
            if (super(UserService, self).getAutorizationToken() != None) :
                httpCall = HttpCalls()
                str =  UserService.getUserURL+ emailID
                jsonObj = httpCall.sendGet(str, UserService.authorizationToken, "GET")
                print("Type of json>>",type(jsonObj))
                if jsonObj != None :
                    print("jsonObj result ::: ",jsonObj)
                    data = json.dumps(jsonObj)
                    print("ccc",type(data))
                    print("ccc", data)
                    if "User not found" not in data:
                        premiseUserID = super(UserService, self).retrieveJSONValue(jsonObj, UserService.jsonFlow)
                        print(" Premise User Id - " ,premiseUserID)
                        print("PASSS")
                    else:
                         self.setUserGetErrorMsg(jsonObj)
                else :
                    print("Unable to get Premise User id:::Json object is NULL")
            else :
                    print("Unable to get Premise user id:::Null Authorization token")
        except :
            print("Encountered exception while retrieving user idr:::", sys.exc_info())

        return premiseUserID

    def getUserGetErrorMsg(self) :
         errorResponse = UserService.userErrorMessage
         UserService.userErrorMessage = ""
         return errorResponse

    def setUserGetErrorMsg(self, jsonMsg):
        userErrorMessage = jsonMsg

    def  softDeleteUser(self, emailID):
        try :
            premiseUserID = self.getUser(emailID)
            if (premiseUserID != "") :
                httpCall = HttpCalls()
                jsonData = httpCall.sendDelete(UserService.deleteUser + premiseUserID, UserService.authorizationToken, "DELETE")
                data = json.dumps(jsonData)
                if "User not found" not in data:
                    userStatus = self.retrieveJSONValue(jsonData, "state")
                    print("Status of email id - " + emailID + " is :- " + userStatus)
                else :
                     print("Unable to softDelete")
                     return False
        except :
                print("Encountered exception in softDeleteUser:::" + sys.exc_info())
                return False
        return True

useer = UserService()
s = useer.getUser("qapremise18@gmail.com")
delUser = useer.softDeleteUser("qapremise18@gmail.com")
print("userID>>",s)