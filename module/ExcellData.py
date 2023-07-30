import pandas as pd
import numpy as np
import xlsxwriter
import openpyxl
from openpyxl.utils import get_column_letter
import shutil
import os
from model.invoiceModel import InvoiceData


class ExcellData ():
    def __init__(self, path) -> None:
        self.path = path
          
    
    def getInvoice(self):
        try:
            data = pd.read_excel(self.path,sheet_name=self.sheetNames[0], dtype=str)
            data = data.replace(np.nan, '')
            invoice = np.array(data)
            return invoice
        except:
            return []

    def getInvoiceItem(self):
        try:
            data = pd.read_excel(self.path,sheet_name= self.sheetNames[1], dtype=str)
            data = data.replace(np.nan, '')
            item = np.array(data)
            return item
        except:
            return []
    
    def getPayment(self):
        try:
            data = pd.read_excel(self.path,sheet_name=self.sheetNames[2], dtype=str)
            data = data.replace(np.nan, '')
            pay = np.array(data)
            return pay
        except:
            return []
        
    def getRevokeInvoice(self):
        try:
            data = pd.read_excel(self.path,sheet_name=self.name_column_revoke, dtype=str)
            data = data.replace(np.nan, '')
            pay = np.array(data)
            return pay
        except:
            return []
        
    def getDeleteUniquId(self):
        try:
            data = pd.read_excel(self.path,sheet_name=self.name_column_delete, dtype=str)
            data = data.replace(np.nan, '')
            pay = np.array(data)
            return pay
        except:
            return []
        
        
    def getBillInvoice(self):
        try:
            data = pd.read_excel(self.path,sheet_name=self.name_column_Bill, dtype=str)
            data = data.replace(np.nan, '')
            pay = np.array(data)
            return pay
        except:
            return []
    
        
    def checkExcel(self, paternType:int):
        try:
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
                        sh = data.active
                        self.invoiceFactorNumber = sh['A1'].value
                    else: result.append(0) 
                elif index == 0 and paternType == 2:
                    if columns.max_column == 18 : 
                        result.append(1) 
                        self.name_column_invoice = sheet
                        sh = data.active
                        self.invoiceFactorNumber = sh['A1'].value
                    else: result.append(0) 
                elif index == 1 :
                    if columns.max_column == 21 : 
                        result.append(1) 
                        self.name_column_invoiceItem = sheet
                        sh = data.active
                        self.invoiceItemFactorNumber = sh['A1'].value
                    else: result.append(0) 
                elif index == 2 and paternType == 1 : 
                    if columns.max_column == 11 : 
                        result.append(1) 
                        self.name_column_payment = sheet
                        sh = data.active
                        self.PaymentFactorNumber = sh['A1'].value
                    else: result.append(0) 
                
                index += 1
            return result
        except:
            return None
        
    def excelCheckRevok(self):
        try:
            data = openpyxl.load_workbook(self.path)
            flag = False
            if len(data.sheetnames) > 1:
                return flag
            sheet = data.sheetnames[0]
            columns = data.get_sheet_by_name(sheet)
            if columns.max_column == 7:
                self.name_column_revoke = sheet
                flag = True
            
            return flag

        except:
            return False
        
    def excelCheckBill(self):
        try:
            data = openpyxl.load_workbook(self.path)
            flag = False
            if len(data.sheetnames) < 1:
                return flag
            sheet = data.sheetnames[0]
            columns = data.get_sheet_by_name(sheet)
            if columns.max_column == 16:
                self.name_column_Bill = sheet
                flag = True
            
            return flag

        except:
            return False
        
    def excelCheckDelete(self):
        try:
            data = openpyxl.load_workbook(self.path)
            flag = False
            sheet = data.sheetnames[0]
            columns = data.get_sheet_by_name(sheet)
            if columns.max_column == 1:
                self.name_column_delete = sheet
                flag = True
            return flag
        except:
            return False
    
    @classmethod
    def getLetter(col):
        return get_column_letter(col)
    
    def copyFile(self,path):
        try:
            new  = path[:-5] + "_read.xlsx"
            result = path[:-5] + "_result.xlsx"
            shutil.copyfile(path, new,follow_symlinks=True)
            shutil.copyfile(path, result,follow_symlinks=True)
            os.remove(path)
            self.path = result
        except:
            self.path = path
    
    def preparationExcellN11(self):
        self.copyFile(self.path)
        workbook = openpyxl.load_workbook(self.path)
        worksheet = workbook[self.name_column_invoice]
        worksheet[get_column_letter(22)+'1'] = "uniqueId"
        worksheet[get_column_letter(23)+'1'] = "Status Request Server"
        worksheet[get_column_letter(24)+'1'] = "taxSerialNumber"
        worksheet[get_column_letter(25)+'1'] = "message"
        worksheet[get_column_letter(26)+'1'] = "FieldError"
        workbook.save(self.path)



    def preparationExcellN21(self):
        self.copyFile(self.path)
        workbook = openpyxl.load_workbook(self.path)
        worksheet = workbook[self.name_column_invoice]
        worksheet[get_column_letter(17)+'1'] = "uniqueId"
        worksheet[get_column_letter(18)+'1'] = "Status Request Server"
        worksheet[get_column_letter(19)+'1'] = "taxSerialNumber"
        worksheet[get_column_letter(20)+'1'] = "message"
        worksheet[get_column_letter(21)+'1'] = "FieldError"
        workbook.save(self.path)
        
    def SaveResultN11(self,data,index):
        workbook = openpyxl.load_workbook(self.path)
        worksheet = workbook[self.name_column_invoice]
        worksheet[get_column_letter(22)+str(index+1)] = data[0]#"uniqueId"
        worksheet[get_column_letter(23)+str(index+1)] = data[1]#"Status Request Server"
        worksheet[get_column_letter(24)+str(index+1)] = data[2]#"taxSerialNumber"
        worksheet[get_column_letter(25)+str(index+1)] = data[3]#"message"
        worksheet[get_column_letter(26)+str(index+1)] = data[4]#"FieldError"
        workbook.save(self.path)

    def SaveResultN21(self,data,index):
        workbook = openpyxl.load_workbook(self.path)
        worksheet = workbook[self.name_column_invoice]
        worksheet[get_column_letter(17)+str(index+1)] = data[0]#"uniqueId"
        worksheet[get_column_letter(18)+str(index+1)] = data[1]#"Status Request Server"
        worksheet[get_column_letter(19)+str(index+1)] = data[2]#"taxSerialNumber"
        worksheet[get_column_letter(20)+str(index+1)] = data[3]#"message"
        worksheet[get_column_letter(21)+str(index+1)] = data[4]#"FieldError
        workbook.save(self.path)
    

    def data_generator(self, batch_size):
        df = pd.read_excel(self.path,sheet_name=None)
        invoice = df[self.name_column_invoice].set_index(self.invoiceFactorNumber)
        invoiceItem = df[self.name_column_invoiceItem].set_index(self.invoiceItemFactorNumber)
        payment = df[self.name_column_payment].set_index(self.PaymentFactorNumber)

        groupItem = invoiceItem.groupby(self.invoiceItemFactorNumber)
        groupPayment = payment.groupby(self.PaymentFactorNumber)

        keys = set(invoice.index).union(set(invoiceItem)).union(set(payment.index))

        for i, key in enumerate(keys):
            if i % batch_size == 0:
                if i > 1:
                    yield batch
                batch = []
            # a = groupItem.get_group()
            data = [invoice.loc[key].to_dict()]
            batch.append(data)
        yield batch

    
    def checkExcellNew(self,type,pattern):
        try:
            excellFile = pd.ExcelFile(self.path)
            self.data = pd.read_excel(self.path,sheet_name=None)
            self.sheetNames = excellFile.sheet_names
            result = []
            for  index,(sheet_name, df) in enumerate(self.data.items()):
                df_cols = len(df.columns)
                cols = InvoiceData(type,pattern,index)
                if df_cols == cols.colum:
                    result.append(1)
                else: result.append(0) 
            return result
        except:
            return None


if __name__ == "__main__":
    ed = ExcellData("./dataTest/Invoice_InvoicePatternId.xlsx")
    # a = ed.checkExcel(2)
    a = ed.checkExcel(1)

    for batch_data in ed.data_generator(batch_size=10):
        print (batch_data)
    # p = "./data/sampel11.xlsx"
    # p = p[:-5] + "_result.xlsx"  
    # print (p)