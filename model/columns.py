from dataclasses import dataclass

class NameColumnsInvoic:
    def __init__(self):
        pass

    def invoiceType11(self) -> list[str]:
        
        return ["invoiceNumber","invoiceDate","invoiceType", "invoicePattern","invoiceSubject", "saleType", "referenceTaxSerialNumber", "buyerType",
        "buyerNationalCode", "buyerEconomicCode", "buyerPostalCode","paymentType", "creditPaymentAmount","invoiceTime","sellerCustomsLicenseNumber", 
        "sellerCustomsDeclarationNumber","sellerContractRegistrationNumber", "sellerBranch",  "buyerBranch","tax17","description"]


    def invoiceType21(self) ->  list[str]:
        return ["invoiceNumber", "invoiceDate", "invoiceType","invoicePattern", "invoiceSubject"
        , "saleType", "referenceTaxSerialNumber", "buyerType", "buyerNationalCode","buyerEconomicCode"
       , "buyerPostalCode","buyerPassportNumber",  "invoiceTime","sellerBranch","buyerBranch", "flightType"
       ,"tax17", "description"]


    def invoiceType13(self) ->  list[str]:
        return ["invoiceNumber", "invoiceDate", "invoiceType", "invoicePattern","invoiceSubject", "saleType"
        , "referenceTaxSerialNumber","buyerType","buyerNationalCode","buyerEconomicCode", "buyerPostalCode"
       ,"paymentType", "creditPaymentAmount", "invoiceTime", "sellerContractRegistrationNumber", "sellerBranch"
        , "buyerBranch","tax17", "description"]
     

    def invoiceType23(self) ->  list[str]:
        return ["invoiceNumber", "invoiceDate", "invoiceType", "invoicePattern", "invoiceSubject", "saleType"
        , "referenceTaxSerialNumber", "buyerType", "buyerNationalCode", "buyerEconomicCode", "buyerPostalCode"
        , "invoiceTime", "sellerBranch","buyerBranch", "tax17","description"]


    def invoiceItemsGeneral(self) -> list[str]:
        return ["invoiceNumber", "invoiceDate","commodityCode","unitType", "amount", "moneyType", "equivalentToRial", "unitPrice", "discount", "taxPercent", "taxPrice", "dutyPercent", "dutyPrice",
         "dutyTitle", "otherLegalFundsPercent", "otherLegalFundsPrice", "otherLegalFundsTitle", "brokerContractNumber", "exchangeContractNumber", "exchangeContractDate", "ExtendStuffTitle"]


    def invoiceItemstype13(self) -> list[str]:
        return ["invoiceNumber", "invoiceDate", "commodityCode", "unitType", "amount", "moneyType"
        ,"equivalentToRial", "unitPrice", "constructionWages", "saleProfit","brokerCommission", "discount"
        , "taxPercent", "taxPrice", "dutyPercent", "dutyPrice", "dutyTitle","otherLegalFundsPercent"
        , "otherLegalFundsPrice","otherLegalFundsTitle","brokerContractNumber", "exchangeContractNumber"
       ,"exchangeContractDate", "ExtendStuffTitle"]


    def invoiceItemstype23(self) ->list[str]:
        return ["invoiceNumber", "invoiceDate", "commodityCode", "unitType", "amount","moneyType"
        , "equivalentToRial", "unitPrice", "constructionWages", "saleProfit", "brokerCommission"
        ,"discount",  "taxPercent", "taxPrice", "dutyPercent", "dutyPrice", "dutyTitle", "otherLegalFundsPercent"
        , "otherLegalFundsPrice", "otherLegalFundsTitle", "brokerContractNumber","exchangeContractNumber"
        , "exchangeContractDate", "ExtendStuffTitle"]
        

    def paymentGeneral(self) -> list[str]:
        return ["invoiceNumber", "invoiceDate", "paymentMethod", "paymentAmount", "paymentDate"
        , "switchNumber", "acceptanceNumber", "terminalNumber", "traceNumber", "payerCardNumber"
        , "payerNationalCode"]


@dataclass
class Columns:
    Type: int
    pattern: int
    indexSheet : int
    columnsNames : list[str] = None

    def __post_init__(self):
        c = NameColumnsInvoic()
        if self.indexSheet == 0:
            if self.Type == 1:
                if self.pattern == 1:
                    self.columnsNames = c.invoiceType11()           
                elif self.pattern == 3:
                    self.columnsNames = c.invoiceType13()
            
            elif self.Type == 2:
                if self.pattern == 1:
                    self.columnsNames = c.invoiceType21()
                elif self.pattern == 3:
                    self.columnsNames = c.invoiceItemstype23
        elif self.indexSheet == 1:
            if self.pattern == 1:
                self.columnsNames = c.invoiceItemsGeneral()
            elif self.pattern == 3:
                if self.Type == 1:
                    self.columnsNames = c.invoiceItemstype13()
                elif self.Type == 2:
                    self.columnsNames = c.invoiceItemstype23()
        elif self.indexSheet == 2:
            self.columnsNames = c.paymentGeneral()
       

