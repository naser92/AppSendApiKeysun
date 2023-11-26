import numpy as np
import pandas as pd
from csv import writer
from datetime import date
import time
from pathlib import Path

class CSVFile():
    def __init__(self,path:str) -> None:
        self.mainpath = path
        split_str = path.split("/")
        name_file = split_str[-1]
        path_file = split_str[:-1]
        name_file = name_file.split(".")
        name_file = name_file[:-1]
        self.fileName = ".".join(name_file)
        self.path = "/".join(path_file) + "/"
        self.curentTime = str(time.strftime("%H-%M"))
        self.today = date.today()
        self.fileSuccessSendInvoice = ""
        self.FileErrorSendInvoice = ""


    def saveData(self,data):
        file = self.path + self.fileName + "_success_" + str(self.today) + "_" + self.curentTime + ".csv" 
        self.fileSuccessSendInvoice = file
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","InvoiceNumber","uniqueId","status","taxSerialNumber"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
    
    def saveDataDelete(self,data):
        file = self.path + self.fileName + "_success_delete_" + str(self.today) + "_" + self.curentTime + ".csv" 
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","uniqueId","status","description"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
    
    def saveDatainquiry2(self,data):
        file = self.path + self.fileName + "_inquiry_" + str(self.today) + "_" + self.curentTime + ".csv" 
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["uniqueId","trackingId","taxSerialNumber","statusCode","statusTitle"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()


    def saveDatainquiry4(self,data):
        file = self.path + self.fileName + "_inquiry_" + str(self.today) + "_" + self.curentTime + ".csv" 
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["trackingId","taxSerialNumber","statusCode","statusTitle"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
        
    def saveError(self,data:list) -> None:
        file = self.path + self.fileName + "_error_" + str(self.today) +"_" + self.curentTime + ".csv" 
        self.FileErrorSendInvoice = file
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","InvoiceNumber","uniqueId","status","title","description"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
        
    def saveErrordelete(self,data):
        file = self.path + self.fileName + "_error_delete_" + str(self.today) +"_" + self.curentTime + ".csv" 
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","uniqueId","status","description"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()

    def read_file_inquiry(self,numberCoulum):
        path = self.path + self.fileName + ".csv"
        df = pd.read_csv(path, sep=',')
        data = df.replace(np.nan, None)
        data = np.array(data)
        taxSerialNumber = []
        for row in data:
            taxSerialNumber.append(row[numberCoulum])

        return taxSerialNumber
    
    def getFileSuccessSendInvoiceName (self):
        return self.fileSuccessSendInvoice
    
    def getFileErrorSendInvoiceName(self):
        return self.FileErrorSendInvoice
    
    ###New function  
    def SaveSuccessSendInvoice(self,data):
        data = np.array(data)
        file = self.path + self.fileName + "_success_" + str(self.today) + "_" + self.curentTime + ".csv" 
        self.fileSuccessSendInvoice = file
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","InvoiceNumber","uniqueId","status","trakingId","taxSerialNumber"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerows(data)
            f_object.close()

    def SaveErrorSendInvoice(self,data):
        data = np.array(data)
        file = self.path + self.fileName + "_error_" + str(self.today) +"_" + self.curentTime + ".csv" 
        self.FileErrorSendInvoice = file
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","InvoiceNumber","uniqueId","status","description","title","CommodityCode"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerows(data)
            f_object.close()

    def SaveErrorSendCommodity(self,data):
        data = np.array(data)
        file = self.path + self.fileName + "_error_" + str(self.today) +"_" + self.curentTime + ".csv" 
        self.FileErrorSendInvoice = file
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","CommodityCode","status","description","title"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerows(data)
            f_object.close()

    def SaveSuccessSendCommodity(self,data):
        data = np.array(data)
        file = self.path + self.fileName + "_success_" + str(self.today) + "_" + self.curentTime + ".csv" 
        self.fileSuccessSendInvoice = file
        p = Path(file)
        check = p.is_file()
        if check == False:
            d = (["ExcelRowNumber","commodityCode","status","description"])
            with open(file, 'a',encoding="utf-8",newline='') as f_object:
                writer_object = writer(f_object)
                writer_object.writerow(d)
                f_object.close()
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerows(data)
            f_object.close()

if __name__ == "__main__":
    import time
    print (time.strftime("%H:%M"))