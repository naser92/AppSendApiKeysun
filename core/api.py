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
        
    def sendInvoice(self,invoices,token):
        try:
            
            proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
            jsonInvoices = json.dumps(invoices)
            header = {
                    'Content-Type': 'application/json ; charset=utf-8',
                    'Authorization' : "Bearer " + token
                }
            url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6"
            try:
                result = r.post(url, jsonInvoices, headers=header, proxies=proxies,  verify=False,timeout=700)
                rr = json.loads(result.content)
                if result.status_code == 200:
                    return [result.status_code,rr]
                # returnResult = []
                # if result.status_code == 200:
                #     for invoice in listIndex:
                #         for data in rr['data']:
                #             if invoice[2] == data['uniqueId']:
                #                 if data['status'] == 3:
                                    
                #                 else:
                #                     pass


                else:
                    return [result.status_code,"serverError"]
            
            except:
                return [result.status_code,"Erorrserver"]


        except:
            return[-1,"ErrorSystem"]
    

if __name__ == "__main__":
    api = ApiKeysun()
    a = api.getToken("0780637356031","sUmM11kN")
    print (a)