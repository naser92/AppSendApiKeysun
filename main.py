from model.InvoiceModel import Invoice
from core.ExcellData import ExcellData
from core.InvoiceData import InvoiceData

excelData = ExcellData("./data/1.xlsx")

listInvoice = excelData.getInvoice()
allItemInvoice = excelData.getInvoiceItem()
allPayment = excelData.getPayment

invoiceData = InvoiceData(allItemInvoice,allPayment)

listInvoice = []
for i,ItemList in enumerate(listInvoice):
    invoice = invoiceData.generateInvoice(ItemList)
    listInvoice.append(invoice)

    

