import customtkinter as ck
import tkinter
from tkinter import filedialog as fd
from module.ExcellData import ExcellData
from module.InvoiceData import InvoiceRevoke
from module.csvFile import CSVFile
from module.api import ApiKeysun
from tkinter import ttk
from model.setting import SettingData
from cryptography.fernet import Fernet
import hashlib
from package.CTkMessagebox import CTkMessagebox

api = ApiKeysun() 
setting = SettingData()
class FormDeleteInvoice():
    def __init__(self,frame:ck.CTkFrame,username, password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.status = False
        self.username = username
        self.passwoerd = password

        #input data
        self.frame_data = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_data.place(x=10,y=10)

        lbl_input = ck.CTkLabel(self.frame_data,text=" :ورود فایل",font=self.font)
        lbl_input.place(x=480,y=25)

        self.lbl_path = ck.CTkLabel(self.frame_data,bg_color="#ffffff",width=275,height=20,text="",text_color="#000000")
        self.lbl_path.place(x=180,y=30)

        self.btn_selectFile = ck.CTkButton(self.frame_data,text="انتخاب فایل",font=self.font,command=self.select_file)
        self.btn_selectFile.place(x=20,y=25)

        #warning:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80,fg_color="#ffbe76")
        self.group_date.place(x=10,y=100)

        lbl_war = ck.CTkLabel(self.group_date,text="که قبلا برای ثبت صورت حساب تولید شده استفاده نمایید UniqeId برای پاک کردن صورتحساب باید از  ",font=self.font12,text_color="#000")
        lbl_war.place(x=35,y=10)
        lbl_war2 = ck.CTkLabel(self.group_date,text="برای استفاده ز این قسمت تمامی آی دی در قالب یک فایل اکسل تک ستونه قرار دهید",font=self.font12,text_color="#000")
        lbl_war2.place(x=60,y=45)


    

        #send element
        self.group_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_send.place(x=10,y=220)

        self.btn_sendInvoice = ck.CTkButton(self.group_send,text="پاک کردن صورتحساب",font=self.font,command=self.deleteInvoice)
        self.btn_sendInvoice.place(x=400,y=10)
        
        self.progressbar = ttk.Progressbar(self.group_send)
        self.progressbar.place(x=20,y=50,width=520)



        #Result
        ck.CTkLabel(self.frame,text="تعداد کل فاکتور ها",font=self.font12).place(x=455,y=320)
        self.lbl_number_allFactor  =  ck.CTkLabel(self.frame,text="0")  
        self.lbl_number_allFactor.place(x=350,y=320)   
        
        ck.CTkLabel(self.frame,text="تعداد فاکتور ارسالی",font=self.font12).place(x=450,y=350)  
        self.lbl_number_sendFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_sendFactor.place(x=350,y=350)   

        ck.CTkLabel(self.frame,text="فاکتور پاک شده",font=self.font12).place(x=470,y=380)
        self.lbl_number_successFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_successFactor.place(x=350,y=380) 

        ck.CTkLabel(self.frame,text="فاکتور خطادار",font=self.font12).place(x=480,y=410)
        self.lbl_number_ErrorFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_ErrorFactor.place(x=350,y=410) 



    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
        )
        self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_path.configure(text=self.path_file)
        self.Excell = ExcellData(self.path_file)
        self.CSV = CSVFile(self.path_file)
        result = self.Excell.excelCheckDelete()
        if result:
            self.status =True
        else:
            CTkMessagebox(title="خطا",message="فایل انتخابی در قالب اکسل مورد نیاز پاک کردن صورتحساب نمی باشد لطفا دوباره انتخاب کنید",icon="cancel")
            self.lbl_path = None


    def lock_element(self):
        for child in self.frame_data.winfo_children():
            child.configure(state='disable')
        
        for child in self.group_date.winfo_children():
            child.configure(state='disable')
        
        self.btn_selectFile.configure(state='disabled')
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()
    
    def reset_element(self):
        for child in self.frame_data.winfo_children():
            child.configure(state='normal')
        
        for child in self.group_date.winfo_children():
            child.configure(state='normal')
        
        self.btn_selectFile.configure(state='normal')
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()

    def deleteInvoice(self):
        if self.path_file == None:
            CTkMessagebox(title="انتخاب فایل",message="فایل را انتخاب کنید",icon="cancel")
        else:
            self.lock_element()
            if self.status:
                uniqeIds = self.Excell.getDeleteUniquId()
                self.progressbar.configure(maximum=len(uniqeIds))
                sucessCount = 0
                errorCount = 0

                if len(uniqeIds) <= 0 :
                    CTkMessagebox(title="دیتا",message="تعداد صورتحساب ها صفر می باشد",icon="warning")
                # inD = InvoiceRevoke()
                listInvoice = []
                listIndex = []
                counter = 0
                self.lbl_number_allFactor.configure(text=str(len(uniqeIds)))
                
                self.frame.after(500)
                self.frame.update()

                for index ,uniqeId in enumerate(uniqeIds):
                    # i = inD.generatRevokeInvoiceApi(revoke,valDateType)
                    uniqeId = uniqeId[0]
                    listIndex.append([index + 1 ,uniqeId])
                    listInvoice.append(uniqeId)
                    counter += 1
                    if counter == setting.BatchSizeOfInvoices or  index ==  (len(uniqeIds) - 1) :
                        token = api.getToken(self.username, self.passwoerd)

                        if token != "":
                            result = api.deleteInvoice(listInvoice,token)
                            if result[0] == 200:
                                indexResult = lambda x,xy : [y for y in xy if y['uniqueId'] == x ] 
                                data = result[1]['data']
                                for invoiceItem in listIndex:
                                    dataResultPerInvoice = indexResult(invoiceItem[1],data)
                                    for i,d in enumerate(dataResultPerInvoice):
                                        if  d['status'] == 3:
                                            try:
                                                self.CSV.saveDataDelete([invoiceItem[0],d['uniqueId'],d['status'],d['description']])
                                            except:
                                                 self.CSV.saveDataDelete([invoiceItem[0],d['uniqueId'],d['status'],d['description']])
                                            sucessCount += 1
                                        else:
                                            self.CSV.saveErrordelete([invoiceItem[0],d['uniqueId'],d['status'],d['description']])
                                            if i == 0:
                                                errorCount += 1
                            else:
                                for invoiceItem in listIndex: 
                                    self.CSV.saveErrordelete([invoiceItem[0],invoiceItem[1],result[0],result[1]])
                                    errorCount += 1
                        else:                    
                            print("login Faild")
                        
                        counter = 0
                        listInvoice = []
                        listIndex = []
                        self.lbl_number_sendFactor.configure(text=str(index+1))
                        self.frame.update_idletasks()
                        self.frame.after(500)
                        self.frame.update()
                
                self.lbl_number_ErrorFactor.configure(text=str(errorCount))
                self.lbl_number_successFactor.configure(text=str(sucessCount))
                self.progressbar['value'] = index+1
                self.progressbar.update()
                self.frame.update_idletasks()
                self.frame.after(500)
                self.frame.update()
            else:
                CTkMessagebox(title="بارگزاری اکسل",message="لطفاً فایل را به درستی در قالب مناسب بارگزاری نمایید.",icon="cancel")
            self.reset_element()
            CTkMessagebox(title="اتمام",message="عملیات با موفقیت به پایان رسید",icon="info")


