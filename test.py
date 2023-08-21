import pandas as pd
import os

path = os.path.join(os.getcwd(),"dataTest\\testpython.xlsx") 

def newName_col(row):
    if row == 1:
        return "invoice"
    elif row == 2:
        return "invvoiceDate"
    elif row == 3:
        return "InvicePattern"
    

df = pd.read_excel(path,sheet_name='Sheet1')
df.columns = df.apply(newName_col)

print (df)


isinstance