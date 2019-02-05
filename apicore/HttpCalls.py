import requests

class HttpCalls:

    def sendGet(self, url, accessToken, method):
        response = None
        print("SENDGET>>URL ",url,"\n token>>"+accessToken)
        header = {'Authorization': 'Bearer ' + accessToken}
        response = requests.get(url, headers=header)
        print("response>>@@@@@@@@@@@@@@",response)
        print(response.json())
        print("############################")
        return response.json()

    def sendDelete(self, url, accessToken, method):
        response = None
        print("sendDelete>>URL ",url,"\n token>>"+accessToken)
        header = {'Authorization': 'Bearer ' + accessToken}
        response = requests.delete(url, headers=header)
        print("response>>@@@@@@@@@@@@@@",response)
        print(response.json())
        print("############################")
        return response.json()