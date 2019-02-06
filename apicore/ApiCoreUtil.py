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
            print("Key>>",key)
        for key, value in data.items():
            print("Key>>",key, "<======>","Value>>",value)
            if key == jsonKey:
                val = value
                print("BREAKKKKKKKK val = value")
                break
        return val

    def find(self, key, dictionary):
        for k, v in dictionary.items():
            if k == key:
                yield v
            elif isinstance(v, dict):
                for result in self.find(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in self.find(key, d):
                        yield result

    def iterate_all(self, iterable, returned="key"):
        print("HI*************************8")
        """Returns an iterator that returns all keys or values
           of a (nested) iterable.

           Arguments:
               - iterable: <list> or <dictionary>
               - returned: <string> "key" or "value"

           Returns:
               - <iterator>
        """

        if isinstance(iterable, dict):
            for key, value in iterable.items():
                if returned == "key":
                    yield key
                elif returned == "value":
                    if not (isinstance(value, dict) or isinstance(value, list)):
                        yield value
                else:
                    raise ValueError("'returned' keyword only accepts 'key' or 'value'.")
                for ret in self.iterate_all(value, returned=returned):
                    yield ret
        elif isinstance(iterable, list):
            for el in iterable:
                for ret in self.iterate_all(el, returned=returned):
                    yield ret
# test = ApiCoreUtil()
# print("CMD>>>>",test.prepareAuthCommand())
# test.getAutorizationToken()


