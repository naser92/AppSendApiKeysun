from dataclasses import dataclass


@dataclass
class InvoiceData:
    Type : int
    pattern : int
    index : int
    colum : int = None
    extend : str = None


    def __post_init__(self):
        if self.Type == 1:
            if self.pattern == 1:
                self.colum = 21 if self.index == 0 else  21 if self.index == 1 else  11           
            elif self.pattern == 3:
                self.colum = 19 if self.index == 0 else  25 if self.index == 1 else  11
            #قبض    
            elif self.pattern == 5:
                if self.extend == None:
                    self.colum = 16 if self.index == 0 else 17 if self.index == 1 else 11

        
        elif self.Type == 2:
            if self.pattern == 1:
                self.colum = 18 if self.index == 0 else  21 if self.index == 1 else  11
            elif self.pattern == 3:
                self.colum = 16 if self.index == 0 else 25


@dataclass
class InvoiceInvalid:
    invoceRow: int
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

@dataclass
class ColumnType:
    columns : list[str]
    typeCol : str

