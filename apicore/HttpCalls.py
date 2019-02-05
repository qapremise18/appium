import requests

class HttpCalls:
    def sendGet(self, url, accessToken, method):
        r = requests.get(url)
        print(r)
        return r