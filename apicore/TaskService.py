from apicore.ApiCoreUtil import ApiCoreUtil
from apicore.UserService import UserService
from apicore.HttpCalls import HttpCalls
import os, sys , json

class TaskService(ApiCoreUtil):

    getUser = "https://user-service-dot-premise-qa.appspot.com/api/user/v1/users/email/"
    getUserSubmissions = "https://submission-service-dot-premise-qa.appspot.com/api/submissions/v1/submissions/summary?userId="
    saveSubmission = "https://submission-service-dot-premise-qa.appspot.com/api/submissions/v1/submissions/SUBMISSIONID/status"
    getCompletedTasks = "https://submission-service-dot-premise-qa.appspot.com/api/submissions/v1/completed-tasks/"
    submitObservation = "https://submission-service-dot-premise-qa.appspot.com/api/submissions/v1/submissions/SUBMISSIONID/observations/OBSERVATIONID/status"
    jsonFlow = "items;submissionId"

    def taskSubmissionAction(self, emailID, action, observationFeedback, submissionFeedback):
        print("#"*10,"taskSubmissionAction","*"*10)
        try :
            user = UserService()
            premiseUserID = user.getUser(emailID)
            submissionID = self.getSubmissionId(premiseUserID)
            observationStatus = self.setObservationId(submissionID, self.prepareFeedback(observationFeedback, action))
            if submissionID != "" & observationStatus :
                newUrl = TaskService.saveSubmission.replace("SUBMISSIONID", submissionID)
                print("TaskService URL >>",newUrl)
                httpCall = HttpCalls()
                jsonData1 = httpCall.sendPost(TaskService.saveSubmission.replace("SUBMISSIONID", submissionID), ApiCoreUtil.authorizationToken,
                self.prepareFeedback(submissionFeedback, action))
                submissionStatus = super(TaskService, self).retrieveJSONValue(jsonData1, "status")
                print(" Submission Status is - " , submissionStatus)
            else :
                 print("Unable to perform ",action," ::: Could not get Submission Id")
        except:
                 print("Exception encountered in acceptSubmission :::" , sys.exc_info())
                 return False
        return True

    def getSubmissionId(self, premiseUserID):
        submissionID = ""
        try:
            httpCall = HttpCalls()
            jsonData = httpCall.sendGet(TaskService.getUserSubmissions+ premiseUserID, ApiCoreUtil.authorizationToken, "GET")
            print("json Response getSubmissionId: " ,jsonData)
            # submissionID =  super(TaskService, self).retrieveJSONValue(jsonData, TaskService.jsonFlow)
            # submissionID = super(TaskService, self).iterate_all(jsonData, "key")
            # submissionID = super(TaskService, self).find("submissionId",jsonData)
            app = ApiCoreUtil()
            print("type>>>SSSSSSSSSSSSSSS",type(jsonData))
            data = json.dumps(jsonData)
            print("type>>>SSSSSSSSSSSSSSS", type(data))
            submissionID = app.find123("submissionId", data)
            print(" Submission ID - " , submissionID)
        except :
            print("Exception encountered for getting Submission Id :::" , sys.exc_info())
            return submissionID


    def setObservationId(self,  submissionID, action):
        try:
            httpCall = HttpCalls()
            jsonData = httpCall.sendGet(TaskService.getCompletedTasks+ submissionID, ApiCoreUtil.authorizationToken, "GET")
            print("Observation Data ::: ", jsonData)
            observationSet = self.getObservationIDs(jsonData,"observationId")
            itr = observationSet.iterator()
            while(itr.hasNext()):
                observationID = itr.next().toString()
                print(observationSet)
                jsonData1 = httpCall.sendPost(TaskService.submitObservation.replace("SUBMISSIONID", submissionID).replace("OBSERVATIONID", observationID), ApiCoreUtil.authorizationToken, action)
        except :
            print("Exception encountered for submitting observationId :::" , sys.exc_info())
            return False
        return True

    def prepareFeedback(self, usereedback, action):
        feedback = ""
        if(usereedback!=""):
            feedback = ": \"userFeedback\": [:\"feedback\": \""+usereedback+"\"],\"status\": \""+action+"\""
        else:
            feedback = ": \"status\": \""+action+"\""

        return feedback



test = TaskService()
test.taskSubmissionAction("qapremise18@gmail.com", "APPROVED", "AAAAAAA", "BBBBBBBBB")