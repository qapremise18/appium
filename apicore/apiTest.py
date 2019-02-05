from apicore.ApiCoreUtil import ApiCoreUtil
from apicore.UserService import UserService
import requests,urllib3
import http.client
class apiTest(ApiCoreUtil):

    getUserURL = "https://user-service-dot-premise-qa.appspot.com/api/user/v1/users/email/"

    def mytest(self, emaildID):

        testURL = apiTest.getUserURL + emaildID
        auth_token = super(apiTest, self).getAutorizationToken().strip()
        print("toekn type>>",type(auth_token))
        print("toekn type>>", auth_token.strip())
        hed = {'Authorization': 'Bearer ' + auth_token}
        # data = {'app' : 'aaaaa'}

        response = requests.get(testURL, headers=hed)
        print(response)
        print(response.json())
        print("*****************************")
        conn = http.client.HTTPConnection(testURL)

        headers = {'authorization': "Bearer "+auth_token}

        conn.request("GET", "/api/private", headers=headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))


test = apiTest()
test.mytest("qapremise18@gmail.com")
