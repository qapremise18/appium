from apicore.ApiCoreUtil import ApiCoreUtil
from apicore.HttpCalls import HttpCalls
import os,sys

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
                print("DDDDDDDDDD",UserService.getUserURL)
                print("EEEEEEE",UserService.getUserURL.join(emailID))
                jsonObj = httpCall.sendGet(UserService.getUserURL.join(emailID), UserService.authorizationToken, "GET")
                if jsonObj != None :
                    print("jsonObj result ::: ",jsonObj)
                    if "User not found" in jsonObj :
                        # premiseUserID = retrieveJSONValue(jsonObj, jsonFlow)
                        # print(" Premise User Id - " + premiseUserID)
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


useer = UserService()
useer.getUser("qapremise18@gmail.com")