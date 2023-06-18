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
    version : str = "3.6.0"