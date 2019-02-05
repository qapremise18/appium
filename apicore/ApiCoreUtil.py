import os,sys,subprocess

class ApiCoreUtil:
    authCommand = "oauth2l fetch -f bare --json JSONFILENAME userinfo.email cloud-platform"
    authorizationToken = ""
    jsonFilePath = "resources/premise-qa.json"

    def prepareAuthCommand(self):
        ApiCoreUtil.jsonFilePath = "C:\\premise-qa.json"
        return ApiCoreUtil.authCommand.replace("JSONFILENAME", os.path.abspath(ApiCoreUtil.jsonFilePath))

    def getAutorizationToken(self) :
        error = None
        token = ""
        retValue = ""
        authCommand = self.prepareAuthCommand()
        if (authCommand != None or authCommand != "") :
            try :
                print("Executing command****************",authCommand)
                # os.system(authCommand)
                token = os.popen(authCommand).read()
                print(token)
            except :
                print("Error in  getAutorizationToken****************",sys.exc_info())

            if (token == None) :
                print("Returning Error :- ")
                # retValue = error
            else :
                print("Returning Token :- " + token)
                retValue = token
                ApiCoreUtil.authorizationToken = token.strip()
        return retValue

    def executeCommand(self, command):
        p = None
        try:
            p = os.popen(command)
        except:
            print("executeCommand Exception encountered")
        return p


    def retrieveJSONValue(self, data ,jsonKey):
        val = ""
        for key in data.keys():
            print(key)
        for key, value in data.items():
            print(key, value)
            if key == jsonKey:
                val = value
                break
        return val
# test = ApiCoreUtil()
# print("CMD>>>>",test.prepareAuthCommand())
# test.getAutorizationToken()


