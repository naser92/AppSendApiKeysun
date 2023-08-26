# import pandas as pd
# import os

# path = os.path.join(os.getcwd(),"dataTest\\testpython.xlsx") 

# def newName_col():
#     # if row == 1:
#     #     return "invoice"
#     # elif row == 2:
#     #     return "invvoiceDate"
#     # elif row == 3:
#     #     return "InvicePattern"
#     return["invoice", "invoiceDate", "invicePattern"]
    

# df = pd.read_excel(path,sheet_name='Sheet1')
# df = df.set_axis(newName_col(),axis='columns')

# print (df)

# # load data Csv file

# isinstance
import math
Alldata = [12,112,47,445,95,48949,494,464,84,4,48,454,64,84,4,4,54,4,54,584,54,87,24,42,42,29,464,4,3,46,4,4,5,4,54,3,8548,987,84]
batch_size = 10
total_batches = math.ceil(len(Alldata) / batch_size)
data_baches = [Alldata[i * batch_size:(i + 1) * batch_size] for i in range(total_batches)]
for data in data_baches:
    print (data)