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
            "taxPercent": self.serializeFloat(data[9]),
            "taxPrice":  data[10],
            "dutyPercent": self.serializeFloat(data[11]),
            "dutyPrice": data[12],
            "dutyTitle": data[13],
            "otherLegalFundsPercent": data[14],
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
    
    def generatePayment(self,data):
        payment =    {
            "paymentMethod":data[2],
            "paymentAmount":data[3],
            "paymentDate": data[4],
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
                    "invoiceNumber" : str(invoice[0]),
                    "invoiceDate" : str(date),
                    "invoiceTime": None,
                    "invoiceType" : invoice[2],
                    "saleType" : 1,
                    "referenceTaxSerialNumber" : invoice[6],
                    "invoicePattern" : invoice[3],
                    "invoiceSubject" : invoice[4],
                    "paymentType" : invoice[11],
                    "uniqueId": str(uuid.uuid4()),
                    "buyerType" : invoice[7],
                    "buyerCompanyName": None,
                    "buyerFirstName": None ,
                    "buyerLastName": None,
                    "buyerNationalCode" : invoice[8],
                    "buyerEconomicCode" : invoice[9],
                    "buyerPassportNumber": None,
                    "buyerPostalCode" : invoice[10],
                    "buyerPhoneNumber": None ,
                    "sellerCustomsDeclarationNumber " :invoice[15],
                    "sellerCustomsLicenseNumber" :invoice[14],
                    "sellerContractRegistrationNumber" :invoice[16],
                    "flightType": None,
                    "billId": None,
                    "tax17" : invoice[19],
                    "creditPaymentAmount" : invoice[12],
                    "description": invoice[20],
                    "sellerBranch":invoice[12],
                    "buyerBranch":invoice[13],
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
                    "invoiceNumber" : str(invoice[0]),
                    "invoiceDate" : str(date),
                    "invoiceTime": str(invoice[11]) if invoice[11] != "" else None,#None,
                    "invoiceType" : invoice[2],
                    "saleType" : invoice[5],
                    "referenceTaxSerialNumber" : invoice[6],
                    "invoicePattern" : invoice[3],
                    "invoiceSubject" : invoice[4],
                    "paymentType" : 1,#invoice[11],
                    "uniqueId": str(uuid.uuid4()),
                    "buyerType" : invoice[7],
                    "buyerCompanyName": None,
                    "buyerFirstName": None ,
                    "buyerLastName": None,
                    "buyerNationalCode" : invoice[8] if invoice[8] != "" else None,
                    "buyerEconomicCode" : invoice[9] if invoice[9] != "" else None,
                    "buyerPassportNumber": None,
                    "buyerPostalCode" : invoice[10] if invoice[10] != "" else None,
                    "buyerPhoneNumber": None ,
                    "sellerCustomsDeclarationNumber " :None,#invoice[15],
                    "sellerCustomsLicenseNumber" :None,#invoice[14],
                    "sellerContractRegistrationNumber" :None,#invoice[16],
                    "flightType": None,
                    "billId": None,
                    "tax17" : invoice[14],
                    "creditPaymentAmount" :None,# invoice[12],
                    "description": invoice[15],
                    "invoiceItems":  listItem,
                    "invoicePayments": listPayment
                        

                }
        return factor
    
    def serializeFloat(self,number):
        try:
             text = math.modf(number)
             t1 = str(text[1])[:-2]
             t2 = str(text[0])[1:4]
             t = t1 + t2
             number = float(t)
             return number
        except:
             return None