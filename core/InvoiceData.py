import uuid

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
            "taxPrice": data[10],
            "dutyPercent": data[11],
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

    def generateInvoiceNo1(self,invoice):
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

        factor = {
                    "invoiceNumber" : str(invoice[0]),
                    "invoiceDate" : invoice[1],#str(date),#invoice[1],
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
                    "invoiceItems":  listItem,
                    "invoicePayments": listPayment
                        

                }
        return factor
