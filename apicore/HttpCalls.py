import requests, json

class HttpCalls:

    def sendGet(self, url, accessToken, method):
        print("##########START sendGet##################")
        response = None
        print("SENDGET>>URL ",url,"\n token>>"+accessToken)
        header = {'Authorization': 'Bearer ' + accessToken}
        response = requests.get(url, headers=header)
        print("response>>@@@@@@@@@@@@@@",response)
        print(response.json())
        print("##########END sendGet##################")
        return response.json()

    def sendDelete(self, url, accessToken, method):
        print("##########START sendDelete##################")
        response = None
        print("sendDelete>>URL ",url,"\n token>>"+accessToken)
        header = {'Authorization': 'Bearer ' + accessToken}
        response = requests.delete(url, headers=header)
        print("response>>@@@@@@@@@@@@@@",response)
        print(response.json())
        print("#########END sendDelete#################")
        return response.json()

    def sendPut(self, url, accessToken, responseBody):
        print("#########START sendPut##################")
        response = None
        print("sendPut>>URL ",url,"\n token>>"+accessToken)
        print("PUT>>responseBody **",responseBody)
        header = {'Authorization': 'Bearer ' + accessToken}
        # response = requests.put(url, data= json.dumps(responseBody), headers=header)
        # response = requests.put(url, json={ "country": "US", "city": "US.CA.SF"}, headers=header)
        response = requests.put(url, json= json.loads(responseBody) , headers=header)
        print("response sendPut >>@@@@@@@@@@@@@@",response)
        print(response.json())
        print("#########END sendPut##################")
        return response.json()

    def sendPost(self, url, accessToken, responseBody):
        print("#########START  sendPost##################")
        response = None
        print("sendPost>>URL ",url,"\n token>>"+accessToken)
        print("POST>>responseBody **",responseBody)
        header = {'Authorization': 'Bearer ' + accessToken}
        response = requests.post(url, json= json.loads(responseBody) , headers=header)
        print("response sendPost >>@@@@@@@@@@@@@@",response)
        print(response.json())
        print("#########END  sendPost##################")
        return response.json()