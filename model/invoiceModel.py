from dataclasses import dataclass


@dataclass
class InvoiceData:
    Type : int
    pattern : int
    index : int
    colum : int = None


    def __post_init__(self):
        if self.Type == 1:
            if self.pattern == 1:
                self.colum = 21 if self.index == 0 else  21 if self.index == 1 else  11           
            elif self.pattern == 3:
                self.colum = 19 if self.index == 0 else  24 if self.index == 1 else  11
        
        elif self.Type == 2:
            if self.pattern == 1:
                self.colum = 18 if self.index == 0 else  21 if self.index == 1 else  11
            elif self.pattern == 3:
                self.colum = 16 if self.index == 0 else 24


@dataclass
class InvoiceInvalid:
    invoce: object
    error : bool
    message : str



@dataclass
class InvoiceEleman:
    key: str
    Value : str
    Type : str

    def __init__(self,key,type):
        self.key = key
        self.Type = type
    
    def setValue(self,value):
        self.Value = value
       

@dataclass
class InvoiceModel:
    InvoiceNumber : InvoiceEleman



