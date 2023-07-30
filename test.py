# import requests as r
# import json
# response   = r.get("https://files.mizeonline.ir/tps/assets/Eitak/eitak.json")
# if response.status_code == 200:
#     data = response.json()
# a = data['version']
# print (a)



# test = [0, 1, 2, 3, 4, 5, 6]
# print(test.pop(0))
# test.append(18)
# print(test)
# print(test.pop(0))


# import jdatetime
# date = str("1402/03/12").split('/')
# date = jdatetime.date(int(date[0]),int(date[1]),int(date[2])).togregorian()
# print(date)

# import tkinter as tk
# from tkinter import messagebox
import configparser

# # Create the frm_login window
# class LoginWindow:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Login")

#         # Create the username label and entry
#         tk.Label(self.master, text="Username").grid(row=0, column=0)
#         self.username_entry = tk.Entry(self.master)
#         self.username_entry.grid(row=0, column=1)

#         # Create the password label and entry
#         tk.Label(self.master, text="Password").grid(row=1, column=0)
#         self.password_entry = tk.Entry(self.master, show="*")
#         self.password_entry.grid(row=1, column=1)

#         # Create the login button
#         tk.Button(self.master, text="Login", command=self.login).grid(row=2, column=1)

#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()

#         # Verify the login credentials
#         if username == "admin" and password == "password":
#             # Store the login status in a configuration file
#             config = configparser.ConfigParser()
#             config['DEFAULT'] = {'LoggedIn': 'True'}
#             with open('config.ini', 'w') as f:
#                 config.write(f)

#             # Close the frm_login window
#             self.master.destroy()
#         else:
#             messagebox.showerror("Error", "Invalid login credentials")

# # Create the frm_version window
# class VersionWindow:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Version")
#         tk.Label(self.master, text="Version 1.0").pack()

# # Create the frm_main window
# class MainWindow:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Main")

#         # Check the login status in the configuration file
#         config = configparser.ConfigParser()
#         config.read('config.ini')
#         if config['DEFAULT'].getboolean('LoggedIn', fallback=False):
#             # Show the frm_version window
#             VersionWindow(tk.Toplevel(self.master))
#         else:
#             # Show the frm_login window
#             LoginWindow(tk.Toplevel(self.master))

# # Create the main Tkinter window
# root = tk.Tk()
# MainWindow(root)
# root.mainloop()

from model.invoiceModel import InvoiceData
import pandas as pd
class InvoiceGenerator():
    def __init__(self, path) -> None:
        self.path = path

    def checkExcell(self,type,pattern):
        excellFile = pd.ExcelFile(self.path)
        self.data = pd.read_excel(self.path,sheet_name=None)
        self.sheetName = excellFile.sheet_names
        result = []
        for  index,(sheet_name, df) in enumerate(self.data.items()):
            # df = pd.read_excel(excellFile,sheet_name=sheet_name)
            df_cols = len(df.columns)
            cols = InvoiceData(type,pattern,index)

            if df_cols == cols.colum:
                result.append(1)
            else: result.append(0) 

    
    def data_generator(self, batch_size):
        df = self.data
        invoice = df[self.sheetName[0]].set_index(self.data[self.sheetName[0]].columns[0])
        # invoiceItem = df[self.sheetName[1]].set_index(self.data[self.sheetName[1]].columns[0])
        # payment = df[self.sheetName[2]].set_index(self.data[self.sheetName[2]].columns[0])

        # df_merge = pd.merge(invoice,invoiceItem,payment,on = self.data[self.sheetName[0]].columns[0])

        # groupItem = invoiceItem.groupby(self.data[self.sheetName[1]].columns[0])
        # groupPayment = payment.groupby(self.data[self.sheetName[2]].columns[0])

        keys = set(invoice.index)
        for i, key in enumerate(keys):
            if i % batch_size == 0:
                if i > 1:
                    yield batch
                batch = []
            # a = groupItem.get_group()
            data = [invoice.loc[key].to_dict()]
            batch.append(data)
        yield batch

if __name__ == "__main__":
    ed = InvoiceGenerator("./dataTest/Invoice_InvoicePatternId.xlsx")
    a = ed.checkExcell(1,1)
    q = [1,1,1,1,1]
    get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
    trueIndex = get_indexes(0,q)

    if len(trueIndex) > 0:
        print("ok")

    for batch_data in ed.data_generator(batch_size=10):
        print (batch_data)