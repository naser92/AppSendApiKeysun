import pandas as pd
import numpy as np
import xlsxwriter
import openpyxl


class ExcellData ():
    def __init__(self, path) -> None:
        self.path = path

    
    def getInvoice(self):
        try:
            data = pd.read_excel(self.path,sheet_name=self.name_column_invoice, dtype=str)
            data = data.replace(np.nan, '')
            invoice = np.array(data)
            return invoice
        except:
            return []

    def getInvoiceItem(self):
        try:
            data = pd.read_excel(self.path,sheet_name= self.name_column_invoiceItem, dtype=str)
            data = data.replace(np.nan, '')
            item = np.array(data)
            return item
        except:
            return []
    
    def getPayment(self):
        try:
            data = pd.read_excel(self.path,sheet_name=self.name_column_payment, dtype=str)
            data = data.replace(np.nan, '')
            pay = np.array(data)
            return pay
        except:
            return []
        
    
        
    def checkExcel(self, paternType:int):
        data = openpyxl.load_workbook(self.path)
        result = []
        if len(data.sheetnames) > 3 or len(data.sheetnames) < 1:
            return result
        
        index = 0
        for sheet in data.sheetnames:
            columns = data.get_sheet_by_name(sheet)
            if index == 0 and paternType == 1:
                if columns.max_column == 21 : 
                    result.append(1) 
                    self.name_column_invoice = sheet
                else: result.append(0) 
            elif index == 0 and paternType == 2:
                if columns.max_column == 16 : 
                    result.append(1) 
                    self.name_column_invoice = sheet
                else: result.append(0) 
            elif index == 1 :
                if columns.max_column == 20 : 
                    result.append(1) 
                    self.name_column_invoiceItem = sheet
                else: result.append(0) 
            elif index == 2 : 
                if columns.max_column == 11 : 
                    result.append(1) 
                    self.name_column_payment =sheet
                else: result.append(0) 
            
            index =+ 1
        return result
        # if len(data.sheetnames) == 3:
        #     self.name_column_invoice = data.sheetnames[0]
        #     self.name_column_invoiceItem = data.sheetnames[1]
        #     self.name_column_payment = data.sheetnames[2]
        #     if paternType == 1:
        #         c = data.get_sheet_by_name(self.name_column_invoice)
        #         print(c)  
        # elif len(data.sheetnames) == 2:
        #     self.name_column_invoice = data.sheetnames[0]
        #     self.name_column_invoiceItem = data.sheetnames[1]
        #     if paternType == 1:
        #         c = data.get_sheet_by_name(self.name_column_invoice)
        #         print(c.max_column)  
        # else:
        #     return False
        # data._sheets[0]._parent.worksheets[0].max_column

    def gettestdata(self):
        wb = openpyxl.load_workbook(self.path)
        data = pd.read_excel(self.path,sheet_name=None, dtype=str)
        data = data.replace(np.nan, '')
        item = np.array(data)

    

if __name__ == "__main__":
    ed = ExcellData("./data/sampel11.xlsx")
    a = ed.checkExcel(2)
    print (a)