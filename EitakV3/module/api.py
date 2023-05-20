import requests as r
import json 

class ApiKeysun:
    # def __init__(self,baseUrl = "https://mizeOnline.ir" ) -> None:
    def __init__(self,baseUrl = "https://localhost:44353" ) -> None:
        self.baseUrl = baseUrl

    def getToken(self,username:str,password:str) -> str:
        url = "/identity/api/ServiceToken" 
        # urlMain = self.baseUrl + url
        urlMain = "https://stage.keysundp.ir" + url
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
                # returnResult = []
                # if result.status_code == 200:
                #     for invoice in listIndex:
                #         for data in rr['data']:
                #             if invoice[2] == data['uniqueId']:
                #                 if data['status'] == 3:
                                    
                #                 else:
                #                     pass


                else :
                    return [result.status_code,"serverError"]
            
            except Exception as ex:
                print(ex)
                return [result.status_code,"Erorrserver"]
        except Exception as ex:
            print(ex)
            return[-1,"ErrorSystem"]
    

    def revokeInvoice(self, revoke, token):
        try:
            jsonInvoices = json.dumps(revoke)
            header = {
                    'Content-Type': 'application/json ; charset=utf-8',
                    'Authorization' : "Bearer " + token
                }
            url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6/InvoiceRevok"
            
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
            # url = self.baseUrl + "/taxpayer/api/InvoiceExternalService_v6/DeleteByUniqueId"
            url = self.baseUrl + "/api/InvoiceExternalService_v6/DeleteByUniqueId"
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
    a = api.getToken("0780637356031","sUmM11kN")
    print (a)