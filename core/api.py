import requests as r
import json 

class ApiKeysun:
    def __init__(self,baseUrl = "https://mizeOnline.ir" ) -> None:
        self.baseUrl = baseUrl

    def getToken(self,username:str,password:str) -> str:
        url = "/identity/api/ServiceToken" 
        urlMain = self.baseUrl + url
        data = {
            "UserName": username,
            "Password": password
        }
        header = {
            'Content-Type': 'application/json ; charset=utf-8',
            
        }
        jsonData = json.dumps(data)
        try:
            result = r.post(urlMain, jsonData,headers=header)
            token = json.loads(result.content)
            self.token = token['data']['token']
            return token['data']['token']
        except:
            return ""
    

if __name__ == "__main__":
    api = ApiKeysun()
    a = api.getToken("0780637356031","sUmM11kN")
    print (a)