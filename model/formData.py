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