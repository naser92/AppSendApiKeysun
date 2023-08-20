class NameColumnsInvoic:
    def __init__(self):
        pass

    def invoiceType11(self,row) -> str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "invoiceType"
        if row == 3:
            return "invoicePattern"
        if row == 4:
            return "invoiceSubject"
        if row == 5:
            return "saleType"
        if row == 6:
            return "referenceTaxSerialNumber"
        if row == 7:
            return "buyerType"
        if row == 8:
            return "buyerNationalCode"
        if row == 9:
            return "buyerEconomicCode"
        if row == 10:
            return "buyerPostalCode"
        if row == 11:
            return "paymentType"
        if row == 12:
            return  "creditPaymentAmount"
        if row == 13:
            return "invoiceTime"
        if row == 14:
           return "sellerCustomsLicenseNumber"
        if row == 15:
            return "sellerCustomsDeclarationNumber"
        if row == 16:
            return "sellerContractRegistrationNumber"
        if row == 17:
            return "sellerBranch"
        if row == 18:
            return  "buyerBranch"
        if row == 19:
            return "tax17"
        if row == 20:
            return "description"


    def invoiceType21(self,row) -> str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "invoiceType"
        if row == 3:
            return "invoicePattern"
        if row == 4:
            return "invoiceSubject"
        if row == 5:
            return "saleType"
        if row == 6:
            return "referenceTaxSerialNumber"
        if row == 7:
            return "buyerType"
        if row == 8:
            return "buyerNationalCode"
        if row == 9:
            return "buyerEconomicCode"
        if row == 10:
            return "buyerPostalCode"
        if row == 11:
            return "buyerPassportNumber"
        if row == 12:
            return  "invoiceTime"
        if row == 13:
            return "sellerBranch"
        if row == 14:
           return "buyerBranch"
        if row == 15:
            return "flightType"
        if row == 16:
            return "tax17"
        if row == 17:
            return "description"


    def invoiceType13(self, row) -> str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "invoiceType"
        if row == 3:
            return "invoicePattern"
        if row == 4:
            return "invoiceSubject"
        if row == 5:
            return "saleType"
        if row == 6:
            return "referenceTaxSerialNumber"
        if row == 7:
            return "buyerType"
        if row == 8:
            return "buyerNationalCode"
        if row == 9:
            return "buyerEconomicCode"
        if row == 10:
            return "buyerPostalCode"
        if row == 11:
            return "paymentType"
        if row == 12:
            return  "creditPaymentAmount"
        if row == 13:
            return "invoiceTime"
        if row == 14:
           return "sellerContractRegistrationNumber"
        if row == 15:
            return "sellerBranch"
        if row == 16:
            return "buyerBranch"
        if row == 17:
            return "tax17"
        if row == 18:
            return  "description"
     

    def invoiceType23(self, row) -> str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "invoiceType"
        if row == 3:
            return "invoicePattern"
        if row == 4:
            return "invoiceSubject"
        if row == 5:
            return "saleType"
        if row == 6:
            return "referenceTaxSerialNumber"
        if row == 7:
            return "buyerType"
        if row == 8:
            return "buyerNationalCode"
        if row == 9:
            return "buyerEconomicCode"
        if row == 10:
            return "buyerPostalCode"
        if row == 11:
            return "invoiceTime"
        if row == 12:
            return  "sellerBranch"
        if row == 13:
            return "buyerBranch"
        if row == 14:
           return "tax17"
        if row == 15:
            return "description"


    def invoiceItemsGeneral(self, row) ->str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "commodityCode"
        if row == 3:
            return "unitType"
        if row == 4:
            return "amount"
        if row == 5:
            return "moneyType"
        if row == 6:
            return "equivalentToRial"
        if row == 7:
            return "unitPrice"
        if row == 8:
            return "discount"
        if row == 9:
            return "taxPercent"
        if row == 10:
            return "taxPrice"
        if row == 11:
            return "dutyPercent"
        if row == 12:
            return  "dutyPrice"
        if row == 13:
            return "dutyTitle"
        if row == 14:
           return "otherLegalFundsPercent"
        if row == 15:
            return "otherLegalFundsPrice"
        if row == 16:
            return "otherLegalFundsTitle"
        if row == 17:
            return "brokerContractNumber"
        if row == 18:
            return  "exchangeContractNumber"
        if row == 19:
            return "exchangeContractDate"
        if row == 20:
            return "ExtendStuffTitle"


    def invoiceItemstype13(self, row) ->str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "commodityCode"
        if row == 3:
            return "unitType"
        if row == 4:
            return "amount"
        if row == 5:
            return "moneyType"
        if row == 6:
            return "equivalentToRial"
        if row == 7:
            return "unitPrice"
        if row == 8:
            return "constructionWages"
        if row == 9:
            return "saleProfit"
        if row == 10:
            return "brokerCommission"
        if row == 11:
            return "discount"
        if row == 12:
            return  "taxPercent"
        if row == 13:
            return "taxPrice"
        if row == 14:
           return "dutyPercent"
        if row == 15:
            return "dutyPrice"
        if row == 16:
            return "dutyTitle"
        if row == 17:
            return "otherLegalFundsPercent"
        if row == 18:
            return  "otherLegalFundsPrice"
        if row == 19:
            return "otherLegalFundsTitle"
        if row == 20:
            return "brokerContractNumber"
        if row == 21:
            return "exchangeContractNumber"
        if row == 22:
            return "exchangeContractDate"
        if row == 23:
            return "ExtendStuffTitle"


    def invoiceItemstype23(self, row) ->str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "commodityCode"
        if row == 3:
            return "unitType"
        if row == 4:
            return "amount"
        if row == 5:
            return "moneyType"
        if row == 6:
            return "equivalentToRial"
        if row == 7:
            return "unitPrice"
        if row == 8:
            return "constructionWages"
        if row == 9:
            return "saleProfit"
        if row == 10:
            return "brokerCommission"
        if row == 11:
            return "discount"
        if row == 12:
            return  "taxPercent"
        if row == 13:
            return "taxPrice"
        if row == 14:
           return "dutyPercent"
        if row == 15:
            return "dutyPrice"
        if row == 16:
            return "dutyTitle"
        if row == 17:
            return "otherLegalFundsPercent"
        if row == 18:
            return  "otherLegalFundsPrice"
        if row == 19:
            return "otherLegalFundsTitle"
        if row == 20:
            return "brokerContractNumber"
        if row == 21:
            return "exchangeContractNumber"
        if row == 22:
            return "exchangeContractDate"
        if row == 23:
            return "ExtendStuffTitle"
        

    def paymentGeneral(self, row) -> str:
        if row == 0:
            return "invoiceNumber"
        if row == 1:
            return "invoiceDate"
        if row == 2:
            return "paymentMethod"
        if row == 3:
            return "paymentAmount"
        if row == 4:
            return "paymentDate"
        if row == 5:
            return "switchNumber"
        if row == 6:
            return "acceptanceNumber"
        if row == 7:
            return "terminalNumber"
        if row == 8:
            return "traceNumber"
        if row == 9:
            return "payerCardNumber"
        if row == 10:
            return "payerNationalCode"