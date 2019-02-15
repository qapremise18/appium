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
                    print("type(data",type(data))
                    print("data = json.dumps(jsonObj) ", data)
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

    def localPartialUpdateUser(self, emailID):
        print("*localPartialUpdateUser","*"*5)
        try :
            premiseUserID = self.getUser(emailID)
            if premiseUserID != "" :
                self.partialUpdateUserURL = UserService.partialUpdateUser.replace("USERID", premiseUserID)
                print("partialUpdateUser URL:::"+self.partialUpdateUserURL)
                httpCall = HttpCalls()
                jsonData = httpCall.sendPut(self.partialUpdateUserURL, UserService.authorizationToken, self.prepareLocalUpdateJSON())
                data = json.dumps(jsonData)
                if "User not found" not in data:
                     self.printUserDetails(jsonData)
            else :
                print("Unable to update Partial User as Premise ID is empty")
            return False
        except:
            print("Encountered exception in partialUpdateUser:::" + sys.exc_info())
        return False

    def prepareLocalUpdateJSON(self):
        # jsonObject = "{ \"country\": \"KE\", \"city\": \"KE.NB.XX-005\"}"
        jsonObject = "{ \"country\": \"US\", \"city\": \"US.CA.SF\"}"
        # jsonObject = "{ \"country\": \"PH\", \"city\": \"PH.MM.MN\"}"
        # jsonObject = "{ \"country\": \"MY\", \"city\": \"MY.KL.KL\"}"
        # jsonObject = "{ \"country\": \"ID\", \"city\": \"ID.JK.JP\"}"
        # jsonObject = "{ \"country\": \"TH\", \"city\": \"TH.CM.CM\"}"
        # jsonObject = "{ \"country\": \"NG\", \"city\": \"NG.LA.XX-006\"}"
        # jsonObject = "{ \"country\": \"VE\", \"city\": \"VE.XX-004\"}"
        # jsonObject = "{ \"country\": \"CO\", \"city\": \"CO.VC.CL\"}"
        # jsonObject = "{ \"country\": \"MX\", \"city\": \"MX.DF.AZ\"}"
        # jsonObject = "{ \"country\": \"IN\", \"city\": \"IN.MH.MC-000\"}"
        # jsonObject = "{ \"country\": \"BR\", \"city\": \"BR.SP\"}"
        # jsonObject = "{ \"country\": \"TR\", \"city\": \"TR.IB.BE\"}"
        # jsonObject = "{ \"country\": \"TZ\", \"city\": \"TZ.DO.DU\"}"
        # jsonObject = "{ \"country\": \"BD\", \"city\": \"BD.DA.DH\"}"
        # jsonObject = "{ \"country\": \"VN\", \"city\": \"VN.HC.HM\"}"
        # jsonObject = "{ \"country\": \"TH\", \"city\": \"TH.BM.PP\"}"
        # jsonObject = "{ \"country\": \"UA\", \"city\": \"UA.KC\"}"
        # jsonObject = "{ \"country\": \"GH\", \"city\": \"GH.AA.AC\"}"
        return jsonObject


    def printUserDetails(self, jsonData):

        premiseID = super(UserService, self).retrieveJSONValue(jsonData, UserService.jsonFlow)
        premiseUserEmailID = super(UserService, self).retrieveJSONValue(jsonData, UserService.userEmailID)
        premiseUserCountry = super(UserService, self).retrieveJSONValue(jsonData, UserService.userCountry)
        premiseUserCity =  super(UserService, self).retrieveJSONValue(jsonData, UserService.userCity)
        userStatus =  super(UserService, self).retrieveJSONValue(jsonData, UserService.userState)

        # print("User Details >>> ID ::: " + premiseID + " || EmailID ::: " + premiseUserEmailID + " || Country ::: "
        #     + premiseUserCountry + " || City ::: " + premiseUserCity + " || State ::: " + userStatus)
        print("User Details >>> ID :::{} || EmailID ::: {} || Country ::: {}  || City ::: {} || State ::: ".format( premiseID,
              premiseUserEmailID, premiseUserCountry , premiseUserCity, userStatus))

useer = UserService()
# s = useer.getUser("qapremise18@gmail.com")
# delUser = useer.softDeleteUser("qapremise18@gmail.com")
# print("userID>>",s)
useer.localPartialUpdateUser("qapremise18@gmail.com")