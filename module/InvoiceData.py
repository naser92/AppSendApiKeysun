import uuid
import jdatetime
import math
class InvoiceData():
    def __init__(self,listInvoiceItem,listPayment) -> None:
        self.ListInvoiceItem = listInvoiceItem
        self.ListPayment = listPayment

    
    def generateInvoiceItem(self,data):
        invoiceItems = {
            "commodityType": 1,
            "commodityCode": data[2],
            "unitType":data[3],
            "amount": data[4],
            "moneyType": data[5],
            "equivalentToRial": data[6],
            "unitPrice": data[7],
            "discount": data[8],
            "taxPercent": data[9],
            "taxPrice":  data[10],
            "dutyPercent": data[11],
            "dutyPrice": data[12],
            "dutyTitle": data[13],
            "otherLegalFundsPercent":data[14],
            "otherLegalFundsPrice": data[15],
            "otherLegalFundsTitle": data[16],
            "brokerContractNumber": data[17],
            "exchangeContractNumber": data[18],
            "exchangeContractDate": data[19],
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
            "paymentMethod":data[2],
            "paymentAmount":data[3],
            "paymentDate": str(date),
            "switchNumber": data[5],
            "acceptanceNumber": data[6],
            "terminalNumber": data[7],
            "traceNumber": data[8],
            "payerCardNumber": data[9],
            "payerNationalCode": data[10]
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
                    "referenceTaxSerialNumber" : invoice[6],
                    "buyerNationalCode" : invoice[8],
                    "buyerEconomicCode" : invoice[9],
                    "buyerPostalCode" : invoice[10],
                    "buyerType" : invoice[7],
                    "paymentType" : invoice[11],
                    "creditPaymentAmount" : invoice[12],
                    "invoiceTime": invoice[13],
                    "sellerCustomsLicenseNumber" :invoice[14],
                    "sellerCustomsDeclarationNumber " :invoice[15],
                    "sellerContractRegistrationNumber" :invoice[16],
                    "sellerBranch":invoice[17],
                    "buyerBranch":invoice[18],
                    "tax17" : invoice[19],
                    "uniqueId": str(uuid.uuid4()),
                    "description": invoice[20],
                    "buyerCompanyName": None,
                    "buyerFirstName": None ,
                    "buyerLastName": None,
                    "buyerPassportNumber": None,
                    "buyerPhoneNumber": None ,
                    "flightType": None,
                    "billId": None,
                    "invoiceItems":  listItem,
                    "invoicePayments": listPayment
                        

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
                    "saleType" : invoice[5],
                    "referenceTaxSerialNumber" : invoice[6],
                    "buyerType" : invoice[7],
                    "buyerEconomicCode" : invoice[8] if invoice[8] != "" else None,
                    "buyerNationalCode" : invoice[9] if invoice[9] != "" else None,
                    "buyerPostalCode" : invoice[10] if invoice[10] != "" else None,
                    "buyerPassportNumber": invoice[11] if invoice[11] != "" else None,
                    "invoiceTime": str(invoice[12]) if invoice[12] != "" else None,
                    "sellerBranch":invoice[13],
                    "buyerBranch":invoice[14],
                    "flightType": invoice[15],
                    "tax17" : invoice[16],
                    "description": invoice[17],
                    "paymentType" : 1,
                    "buyerCompanyName": None,
                    "buyerFirstName": None ,
                    "buyerLastName": None,
                    "buyerPhoneNumber": None ,
                    "sellerCustomsDeclarationNumber " :None,#invoice[15],
                    "sellerCustomsLicenseNumber" :None,#invoice[14],
                    "sellerContractRegistrationNumber" :None,#invoice[16],
                    "billId": None,
                    "creditPaymentAmount" :None,# invoice[12],
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
            "ReferenceTaxSerialNumber" : data[5],
            "Description" : data[6]
        }

        return invoce
          

          

    
        