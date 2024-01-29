class Patern:
    def __init__(self,value:int,string:str) -> None:
        self.value = value
        self.string = string

    def __repr__(self) -> str:
        return f"Patern(value={self.value},strng={self.strng})"
    
    @classmethod
    def getIndex(cls, query, paterns) -> int:
        for p in paterns:
            if query in p.string:
                return p.value
            
class SelectionItems:
    def __init__(self,value:int,string:str) -> None:
        self.value = value
        self.string = string

    def __repr__(self) -> str:
        return f"Patern(value={self.value},strng={self.strng})"
    
    @classmethod
    def getIndex(cls, query, paterns) -> int:
        for p in paterns:
            if query in p.string:
                return p.value
            

class TypeInvoice_SendInvoice:
    def __init__(self,typeId:int, PatternId:int, stringValue:str):
        self.typeId = typeId
        self.PatternId = PatternId
        self.stringValue = stringValue

    @classmethod
    def getIndex(cls, query, allType) -> list[int]:
        for a in allType:
            if query in a.stringValue:
                return [a.typeId,a.PatternId]
            
class BillType_combo:
    def __init__(self, typeId:int, patternId:int, stringValue:str, stringViwe:str):
        self.typeId = typeId
        self.PatternId = patternId
        self.stringValue = stringValue
        self.stringViwe = stringViwe

    @classmethod
    def getIndex(cls, query, allType):
        for a in allType:
            if query in a.stringViwe:
                return [a.typeId,a.PatternId,a.stringValue]