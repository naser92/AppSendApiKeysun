import sys
import os
sys.path.append(os.getcwd())
from model.invoiceModel import InvoiceInvalid,InvoiceModel
from datetime import datetime


class Validation:
    def __init__(self):
        pass

    def invalidInvoiceData(self, invoice):
        result = []


    def DateCheck(self, input, typeDate) -> bool:
        if typeDate == 1 :
            try:
                datetime.strptime(input, '%Y-%m-%d')
                return True
            except:
                return False
        if typeDate == 2 :
            try:
                datetime.strptime(input, '%Y/%m/%d')
                return True
            except:
                return False
            
    def StringCheck(self, input) -> bool:
        if input == None or input == "":
            return False
        else:
            return True 

    def NumberCheck(self, inputStr:str) -> bool:
        if inputStr.isdigit() : 
            return True
        else: 
            return False
            

if __name__ == '__main__':
    v = Validation()
    invoice = ["21313"]
    e = InvoiceModel
    # e.InvoiceNumber = 

    print (v.DateCheck("1399/11/03",2))
    

