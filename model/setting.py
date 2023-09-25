from dataclasses import dataclass
import json

@dataclass
class SettingData:
    BatchSizeOfInvoices: int

    def __init__(self) -> None:
        try:
            with open("applicationSetting.json") as jsonfile:
                data = json.load(jsonfile)
                self.BatchSizeOfInvoices = data["BatchSizeOfInvoices"]
        except:
            self.BatchSizeOfInvoices = 10

@dataclass
class VersionApp:
    version : str = "6.4.5"


@dataclass
class Location:
    x: int
    y: int
    BX : int
    BY: int

    def __init__(self, StartX, StartY , BetWeenX, BetWeenY) -> None:
        self.x = StartX
        self.y = StartY
        self.BX = BetWeenX 
        self.BY = BetWeenY

    def setRowLocation(self,rowNumber) -> int:
        return self.y + (self.BY * rowNumber )

 
    def setColLocation(self,colNumber) -> int:
        return self.x + (self.BX * colNumber)
        