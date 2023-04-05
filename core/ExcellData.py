import pandas as pd
import numpy as np
import xlsxwriter


class ExcellData ():
    def __init__(self, path) -> None:
        self.path = path
    
    def getInvoice(self):
        data = pd.read_excel(self.path,sheet_name="invoice", dtype=str)
        data = data.replace(np.nan, '')
        invoice = np.array(data)
        return invoice

    def getInvoiceItem(self):
        data = pd.read_excel(self.path,sheet_name="itemInvoice", dtype=str)
        data = data.replace(np.nan, '')
        item = np.array(data)
        return item
    
    def getPayment(self):
        data = pd.read_excel(self.path,sheet_name="payment", dtype=str)
        data = data.replace(np.nan, '')
        pay = np.array(data)
        return pay