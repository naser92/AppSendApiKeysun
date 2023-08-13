import requests as r
import json 
import time
import pandas as pd
import numpy as np
class ApiKeysun:
    def __init__(self,baseUrl = "https://mizeOnline.ir" ) -> None:
    # def __init__(self,baseUrl = "https://localhost:44353" ) -> None:
        self.baseUrl = baseUrl

    def getToken(self,username:str,password:str) -> str:
        url = "/identity/api/ServiceToken" 
        urlMain = self.baseUrl + url
        # urlMain = "https://stage.keysundp.ir" + url
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
            
            # proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
            jsonInvoices = json.dumps(invoices)
            header = {
                    'Content-Type': 'application/json ; charset=utf-8',
                    'Authorization' : "Bearer " + token
                }
            url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6"
            try:
                # result = r.post(url, jsonInvoices, headers=header, proxies=proxies,  verify=False,timeout=700)
                result = r.post(url, jsonInvoices, headers=header,timeout=700,verify=False)
                rr = json.loads(result.content)
                if result.status_code == 200:
                    return [result.status_code,rr]
                else :
                    return [result.status_code,"serverError"]
            except:
                return [result.status_code,"Erorrserver"]
                
        except:
            return[-1,"ErrorSystem"]
    

    def revokeInvoice(self, revoke, token):
        try:
            jsonInvoices = json.dumps(revoke)
            header = {
                    'Content-Type': 'application/json ; charset=utf-8',
                    'Authorization' : "Bearer " + token
                }
            url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6/InvoiceRevok"
            # url = self.baseUrl + "/api/InvoiceExternalService_v6/InvoiceRevok"
            
            try:
                result = r.post(url, jsonInvoices, headers=header,timeout=700,verify=False)
                rr = json.loads(result.content)
                if result.status_code == 200:
                    return [result.status_code,rr]
                else:
                    return [result.status_code,"serverError"]

            except:
                return [result.status_code,"Erorrserver"]
        except:
            return[-1,"ErrorSystem"]
        
    def deleteInvoice(self,listUniqeId,token):
        try:
            jsonInvoices = json.dumps(listUniqeId)
            header = {
                    'Content-Type': 'application/json ; charset=utf-8',
                    'Authorization' : "Bearer " + token
                }
            url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6/DeleteByUniqueId"
            # url = self.baseUrl + "/api/InvoiceExternalService_v6/DeleteByUniqueId"
            try:
                result = r.post(url, jsonInvoices, headers=header,verify=False)
                rr = json.loads(result.content)
                if result.status_code == 200:
                    return [result.status_code,rr]
                    
            except:
                return [result.status_code,"serverError"]
        except:
            return[-1,"ErrorSystem"]

    def inquiryInvoiceByUniqeId(self,listUniqeId,token):
        try:
            jsonInvoices = json.dumps(listUniqeId)
            header = {
                    'Content-Type': 'application/json ; charset=utf-8',
                    'Authorization' : "Bearer " + token
                }
            url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6/InquiryByUniqueId"
            # url = self.baseUrl + "/api/InvoiceExternalService_v6/InquiryByUniqueId"
            try:
                result = r.post(url, jsonInvoices, headers=header,verify=False)
                rr = json.loads(result.content)
                if result.status_code == 200:
                    return [result.status_code,rr]
                    
            except:
                return [result.status_code,"serverError"]
        except:
            return[-1,"ErrorSystem"]

    def inquiryInvoiceByTaxserialnumber(self,listTaxSerialNumber,token):
        try:
            jsonInvoices = json.dumps(listTaxSerialNumber)
            header = {
                    'Content-Type': 'application/json ; charset=utf-8',
                    'Authorization' : "Bearer " + token
                }
            url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6/InquiryByTaxSerialNumber"
            # url = self.baseUrl + "/api/InvoiceExternalService_v6/InquiryByTaxSerialNumber"
            try:
                result = r.post(url, jsonInvoices, headers=header,verify=False)
                rr = json.loads(result.content)
                if result.status_code == 200:
                    return [result.status_code,rr]
                    
            except:
                return [result.status_code,"serverError"]
        except:
            return[-1,"ErrorSystem"]
        
    def GetVersion(self) -> str:
        response = r.get("https://files.mizeonline.ir/tps/assets/Eitak/eitak.json")
        if response.status_code == 200:
            data = response.json()
            try:
                self.urlVersion = data['url']
            except:
                self.urlVersion = None

            return data['version']
        else:
            return "0"
    
    def GetURL_Help(self) -> str:
        try:
            response = r.get("https://files.mizeonline.ir/tps/assets/Eitak/eitak.json")
            if response.status_code == 200:
                data = response.json()
                return data['urlHelp']
            else:
                return "O"
        except:
            return "0"
    
    def getUrl(self) -> str:
        return self.urlVersion

    def checkResult(self,statusCode,response,listIndex):
        if statusCode == 200 and response['error'] == False:
            data = response['data']
            result = pd.DataFrame(data)
            listInvoice = pd.DataFrame(listIndex)
            merge =  listInvoice.join(result.set_index('uniqueId'), on='uniqueId',validate='1:m')
            successR = merge[merge['status'] == 3]
            errorR = merge[merge['status'] != 3]
            
            print (successR)
            print (f"count Success =  {len(successR)}  count Error = {len(errorR['uniqueId'].drop_duplicates())}")
            print (errorR)

            



class APIEconomicCode():
    def __init__(self) -> None:
        pass

    def InquiryPerson(self,economic):
        url = "https://mizeonline.ir/externalservice/api/TaxEconomicCodeInformation"
        heder = {
            "Content-Type": "application/json",                
            "secret-key": "A9F6307A-C00C-42B5-9170-84ED4D58BF56"
        }

        body ={
            "economicCode": economic
        }
        bodyj = json.dumps(body)

        try:
            result = r.post(url,bodyj,headers=heder, verify=False)
            rr = json.loads(result.content)
            if rr['result'] != None:
                return rr['result']
            elif rr['error'] != None:
                return rr['error']
            else:
                return "پاسخی از سرور دریافت نشد"
        except:
            message = "خطا در شبکه"
            return message

    


if __name__ == "__main__":
    api = ApiKeysun()
    # a = api.getToken("0780637356031","sUmM11kN")
    responce = {
        "data": [
            {
            "status": 3,
            "uniqueId": "ac26c798-6d13-4d34-82ee-5ee96aee7671",
            "trakingId": "0a65423e-8565-4286-bb3d-fe215ccae5bf",
            "taxSerialNumber": "A1112D04C7B000000D87C7",
            "description": "",
            "title": ""
            },
            {
            "status": 1,
            "uniqueId": "ac26c798-6d13-4d34-82ee-fe215ccaeaaa",
            "trakingId": "0a65423e-8565-4286-bb3d-2",
            "taxSerialNumber": "A1112D04C7B000000D87C6",
            "description": "",
            "title": "فاکتور دو خطا"
            },
            {
            "status": 1,
            "uniqueId": "ac26c798-6d13-4d34-82ee-fe215ccaeaaa",
            "trakingId": "0a65423e-8565-4286-bb3d-2",
            "taxSerialNumber": "A1112D04C7B000000D87C6",
            "description": "",
            "title": "فاکتور دو خطا 2"
            },
            {
            "status": 3,
            "uniqueId": "ac26c798-6d13-4d34-82ee-fe215ccaebbb",
            "trakingId": "0a65423e-8565-4286-bb3d-1",
            "taxSerialNumber": "A1112D04C7B000000D87C5",
            "description": "",
            "title": "فاکتور تک خطا"
            },
            {
                      "status": 1,
                        "uniqueId": "8c98085d-10d7-4c84-b4b6-e55acf246721",
                        "description": "نوع خریدار نا معتبر است",
                        "title": "BuyerType"
            }
        ],
        "error": False,
        "succeeded": True
    }
    # indexlist = [
    #     ["1","11","ac26c798-6d13-4d34-82ee-5ee96aee7671"],
    #     ["2","22","0a65423e-8565-4286-bb3d-fe215ccaeaaa"],
    #     ["3","33","0a65423e-8565-4286-bb3d-fe215ccaebbb"]
    # ]
    indexlist = [
        {"indexRow":"1","invocieNumber":"11","uniqueId":"ac26c798-6d13-4d34-82ee-5ee96aee7671"},
        {"indexRow":"2","invocieNumber":"22","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaeaaa"},
        {"indexRow":"3","invocieNumber":"33","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaebbb"},
        {"indexRow":"4","invocieNumber":"44","uniqueId":"8c98085d-10d7-4c84-b4b6-e55acf246721"},
    ]
    a = api.checkResult(200,responce,indexlist)
    print (a)