import pandas as pd
import os

path = os.path.join(os.getcwd(),"dataTest\\testpython.xlsx") 

def newName_col():
    # if row == 1:
    #     return "invoice"
    # elif row == 2:
    #     return "invvoiceDate"
    # elif row == 3:
    #     return "InvicePattern"
    return["invoice", "invoiceDate", "invicePattern"]
    

df = pd.read_excel(path,sheet_name='Sheet1')
df = df.set_axis(newName_col(),axis='columns')

print (df)

# load data Csv file

isinstance