import uuid
import jdatetime
import math
from model.setting import VersionApp

class InvoiceData():
    def __init__(self,listInvoiceItem,listPayment) -> None:
        self.ListInvoiceItem = listInvoiceItem
        self.ListPayment = listPayment

    
    def generateInvoiceItem(self,data):
        invoiceItems = {
            "commodityType": 1,
            "commodityCode": data[2] if data[2] != "" else None,
            "unitType":data[3] if data[3] != "" else None,
            "amount": data[4] if data[4] != "" else None,
            "moneyType": data[5] if data[5] != "" else None,
            "equivalentToRial": data[6] if data[6] != "" else None,
            "unitPrice": data[7] if data[7] != "" else None,
            "discount": data[8] if data[8] != "" else None,
            "taxPercent": data[9] if data[9] != "" else None,
            "taxPrice":  data[10] if data[10] != "" else None ,
            "dutyPercent": data[11] if data[11] != "" else None,
            "dutyPrice": data[12] if data [12] != "" else None,
            "dutyTitle": data[13] if data[13] != "" else None,
            "otherLegalFundsPercent":data[14] if data[14] != "" else None,
            "otherLegalFundsPrice": data[15] if data[15] != "" else None,
            "otherLegalFundsTitle": data[16] if data[16] != "" else None ,
            "brokerContractNumber": data[17] if data[17] != "" else None,
            "exchangeContractNumber": data[18] if data[18] != "" else None,
            "exchangeContractDate": data[19] if data[19] != "" else None,
            "equivalentUnitType": None,
            "equivalentAmount": 0.0,
            "currencyAmount": 0.0,
            "saleProfit": 0.0,
            "brokerCommission": 0.0,
            "brokerContractNumber": None
            }
        return invoiceItems
    
    def generatePayment(self,data,vDate):
        if vDate == 1:
            date = data[4]
        elif vDate == 2 :
            date = str(data[4]).split('/')
            date = jdatetime.date(int(date[0]),int(date[1]),int(date[2])).togregorian()
        else:
            date = ""
        payment =    {
            "paymentMethod":data[2] if data[2] != "" else None,
            "paymentAmount":data[3] if data[3] != "" else None,
            "paymentDate": str(date) if date != "" else None,
            "switchNumber": data[5] if data[5] != "" else None,
            "acceptanceNumber": data[6] if data[6] != "" else None,
            "terminalNumber": data[7] if data[7] != "" else None,
            "traceNumber": data[8] if data[8] != "" else None,
            "payerCardNumber": data[9] if data[9] != "" else None,
            "payerNationalCode": data[10] if data[10] != "" else None
        }
        return payment

    def generateInvoiceNo1(self,invoice,vDate):
        getItems = lambda x, xs: [y for y in xs if x[0] == y[0] and x[1] == y[1]]
        
        listItem= []
        indexItem = getItems(invoice,self.ListInvoiceItem)
        for item in indexItem:
                invoiceItemM = self.generateInvoiceItem(item)
                listItem.append(invoiceItemM)
        
        listPayment =[]
        indexPay = getItems(invoice,self.ListPayment)
        if len(indexPay) > 0:
            for item in indexPay:
                    PaymentM = self.generatePayment(item,vDate)
                    listPayment.append(PaymentM)
        if vDate == 1:
            date = invoice[1]
        elif vDate == 2 :
            date = str(invoice[1]).split('/')
            date = jdatetime.date(int(date[0]),int(date[1]),int(date[2])).togregorian()
        else:
            date = ""

        factor = {
                    "invoiceNumber" : str(invoice[0]),
                    "invoiceDate" : str(date),
                    "invoiceType" : invoice[2],
                    "invoicePattern" : invoice[3],
                    "invoiceSubject" : invoice[4],
                    "saleType" : invoice[5],
                    "referenceTaxSerialNumber" : invoice[6] if invoice[6] != "" else None,
                    "buyerType" : invoice[7] if invoice[7] != "" else None,
                    "buyerNationalCode" : invoice[8] if invoice[8] != "" else None,
                    "buyerEconomicCode" : invoice[9] if invoice[9] != "" else None,
                    "buyerPostalCode" : invoice[10] if invoice[10] != "" else None,
                    "paymentType" : invoice[11] if invoice[11] != "" else None,
                    "creditPaymentAmount" : invoice[12] if invoice[12] != "" else None,
                    "invoiceTime": invoice[13] if invoice[13] != "" else None,
                    "sellerCustomsLicenseNumber" :invoice[14] if invoice[14] != "" else None,
                    "sellerCustomsDeclarationNumber " :invoice[15] if invoice[15] != "" else None,
                    "sellerContractRegistrationNumber" :invoice[16] if invoice[16] != "" else None,
                    "sellerBranch":invoice[17] if invoice[17] != "" else None,
                    "buyerBranch":invoice[18] if invoice[18] != "" else None,
                    "tax17" : invoice[19] if invoice[19] != "" else None,
                    "description": invoice[20] if invoice[20] != "" else None,
                    "uniqueId": str(uuid.uuid4()),
                    "buyerCompanyName": None,
                    "buyerFirstName": None ,
                    "buyerLastName": None,
                    "buyerPassportNumber": None,
                    "buyerPhoneNumber": None ,
                    "flightType": None,
                    "billId": None,
                    "invoiceItems":  listItem,
                    "invoicePayments": listPayment,
                    "CooperationCode": "Eitak_" + VersionApp.version
                        

                }
        return factor
    
    def generateInvoiceNo2(self,invoice,vDate):
        getItems = lambda x, xs: [y for y in xs if x[0] == y[0] and x[1] == y[1]]
        
        listItem= []
        indexItem = getItems(invoice,self.ListInvoiceItem)
        for item in indexItem:
                invoiceItemM = self.generateInvoiceItem(item)
                listItem.append(invoiceItemM)
        
        listPayment =[]
        indexPay = getItems(invoice,self.ListPayment)
        if len(indexPay) > 0:
            for item in indexPay:
                    PaymentM = self.generateInvoiceItem(item)
                    listPayment.append(PaymentM)
        if vDate == 1:
            date = invoice[1]
        elif vDate == 2 :
            date = str(invoice[1]).split('/')
            date = jdatetime.date(int(date[0]),int(date[1]),int(date[2])).togregorian()
        else:
            date = ""

        factor = {
                    "uniqueId": str(uuid.uuid4()),
                    "invoiceNumber" : str(invoice[0]),
                    "invoiceDate" : str(date),
                    "invoiceType" : invoice[2],
                    "invoicePattern" : invoice[3],
                    "invoiceSubject" : invoice[4],
                    "saleType" : invoice[5] if invoice[5] != "" else None,
                    "referenceTaxSerialNumber" : invoice[6] if invoice[6] != "" else None,
                    "buyerType" : invoice[7] if invoice[7] != "" else None,
                    "buyerEconomicCode" : invoice[8] if invoice[8] != "" else None,
                    "buyerNationalCode" : invoice[9] if invoice[9] != "" else None,
                    "buyerPostalCode" : invoice[10] if invoice[10] != "" else None,
                    "buyerPassportNumber": invoice[11] if invoice[11] != "" else None,
                    "invoiceTime": str(invoice[12]) if invoice[12] != "" else None,
                    "sellerBranch":invoice[13] if invoice[13] != "" else None,
                    "buyerBranch":invoice[14] if invoice[14] != "" else None,
                    "flightType": invoice[15] if invoice[15] != "" else None,
                    "tax17" : invoice[16] if invoice[16] != "" else None,
                    "description": invoice[17] if invoice[17] != "" else None,
                    "paymentType" : 1,
                    "buyerCompanyName": None,
                    "buyerFirstName": None ,
                    "buyerLastName": None,
                    "buyerPhoneNumber": None ,
                    "sellerCustomsDeclarationNumber " :None,
                    "sellerCustomsLicenseNumber" :None,
                    "sellerContractRegistrationNumber" :None,
                    "billId": None,
                    "creditPaymentAmount" :None,
                    "CooperationCode": "Eitak_" + VersionApp.version,
                    "invoiceItems":  listItem,
                    "invoicePayments": listPayment
                        

                }
        return factor
    
    # def serializeFloat(self,number):
    #     try:
    #          num = float(number)
    #          text = math.modf(num)
    #          t1 = str(text[1])[:-2]
    #          t2 = str(text[0])[1:4]
    #          t = t1 + t2
    #          number = float(t)
    #          return number
    #     except:
    #          return None


class InvoiceRevoke():
    def __init__(self) -> None:
        pass
     
    def generatRevokeInvoiceApi(self,data,Vdate):
        if Vdate == 1:
            date = data[1]
        elif Vdate == 2 :
            date = str(data[1]).split('/')
            date = jdatetime.date(int(date[0]),int(date[1]),int(date[2])).togregorian()

        invoce = {
            "uniqueId" : str(uuid.uuid4()),
            "InvoiceNumber": data[0],
            "InvoiceDate": str(date),
            "invoiceType" : data[2],
            "invoicePattern" : data[3],
            "invoiceSubject" : data[4],
            "ReferenceTaxSerialNumber" : data[5] if data[5] != "" else None,
            "Description" : data[6] if data[6] != "" else None
        }

        return invoce
          

          

    
        