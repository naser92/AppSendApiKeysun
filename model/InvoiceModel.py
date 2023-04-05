from dataclasses import dataclass


@dataclass
class Invoice:
    Index: int = None
    invoiceNumber: str = None
    invoiceDate : str= None
    invoiceType : int= None
    invoicePattern: int= None
    invoiceSubject : int= None
    paymentType: int= None
    uniqueId : str= None
    referenceTaxSerialNumber: str= None
    buyerType : int= None
    buyerNationalCode: int= None