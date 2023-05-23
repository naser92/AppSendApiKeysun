import customtkinter as ck
import tkinter
from tkinter import filedialog as fd
from module.ExcellData import ExcellData
from module.InvoiceData import InvoiceData
from module.csvFile import CSVFile
from module.api import ApiKeysun
from cryptography.fernet import Fernet
from package.CTkMessagebox import CTkMessagebox
from model.formData import Patern
import hashlib
from model.setting import SettingData
from tkinter import ttk


api = ApiKeysun() 
setting = SettingData()

class FormSendInvoice():
    def __init__(self,frame:ck.CTkFrame,username,password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.username = username
        self.password = password

        self.patern = [
            Patern(0,"انتخاب الگو صورتحساب"),
            Patern(1,"نوع 1 الگوی 1 صورتحساب فروش همراه با اطلاعات خریدار"),
            Patern(2,"نوع 2 الگوی 1 صورتحساب فروش بدون اطلاعات خریدار")
        ]


       
        #radioButom:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_date.place(x=10,y=10)

        self.valDate = tkinter.IntVar()
        
        self.R2 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=2)
        self.R2.place(x=200,y=25)
        ck.CTkLabel(self.group_date,text="تاریخ ورودی شمسی",font=self.font).place(x=70,y=18)
        ck.CTkLabel(self.group_date,text="yyyy/mm/dd").place(x=105,y=45)

        self.R1 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=1)
        self.R1.place(x=410,y=25)
        ck.CTkLabel(self.group_date,text="تاریخ ورودی میلادی",font=self.font).place(x=290,y=18)
        ck.CTkLabel(self.group_date,text="yyyy-mm-dd").place(x=315,y=45)

        lbl_selectTypeDate = ck.CTkLabel(self.group_date,text=" :انتخاب نوع تاریخ",font=self.font)
        lbl_selectTypeDate.place(x=450,y=20)

        #inputfile
        self.group_file = ck.CTkFrame(self.frame,border_width=2, width=570, height=90)
        self.group_file.place(x=10,y=110)

        self.numberPatern = ck.CTkComboBox(self.group_file, width=400,font=self.font,dropdown_font=self.font12,state="readonly",
                                            values=[self.patern[0].string,self.patern[1].string,self.patern[2].string])
        
        self.numberPatern.place(x=70,y=10)
        self.numberPatern.set(self.patern[0].string)

        lbl_selectTypeDate = ck.CTkLabel(self.group_file,text=" :ورود فایل",font=self.font)
        lbl_selectTypeDate.place(x=480,y=25)

        self.lbl_path = ck.CTkLabel(self.group_file,bg_color="#ffffff",width=300,height=20,text="",text_color="#000000")
        self.lbl_path.place(x=170,y=50)

        
        self.btn_selectFile = ck.CTkButton(self.group_file,text="انتخاب فایل",font=self.font,command=self.select_file,width=60)
        self.btn_selectFile.place(x=70,y=45)

        #send element
        self.group_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_send.place(x=10,y=220)

        self.btn_sendInvoice = ck.CTkButton(self.group_send,text="ارسال صورتحساب",font=self.font,command=self.send_invoice)
        self.btn_sendInvoice.place(x=400,y=10)
        
        self.btn_reset = ck.CTkButton(self.group_send,text="کنسل",font=self.font,command=self.reset_form)
        self.btn_reset.place(x=20,y=10)

        self.progressbar =  ttk.Progressbar(self.group_send)
        self.progressbar.place(x=20,y=50,width=520)
        

        
        # ck.CTkLabel(self.frame,text="تعداد کل فاکتور ها",font=self.font12).place(x=355,y=270)
        # self.lbl_number_allFactor  =  ck.CTkLabel(self.frame,text="0")  405
        # self.lbl_number_allFactor.place(x=300,y=270)   
        ck.CTkLabel(self.frame,text="تعداد کل فاکتور ها",font=self.font12).place(x=455,y=320)
        self.lbl_number_allFactor  =  ck.CTkLabel(self.frame,text="0")  
        self.lbl_number_allFactor.place(x=350,y=320)   
        
        ck.CTkLabel(self.frame,text="تعداد فاکتور ارسالی",font=self.font12).place(x=450,y=350)  
        self.lbl_number_sendFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_sendFactor.place(x=350,y=350)   

        ck.CTkLabel(self.frame,text="فاکتور ثبت شده",font=self.font12).place(x=470,y=380)
        self.lbl_number_successFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_successFactor.place(x=350,y=380) 

        ck.CTkLabel(self.frame,text="فاکتور خطادار",font=self.font12).place(x=480,y=410)
        self.lbl_number_ErrorFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_ErrorFactor.place(x=350,y=410) 

        
        self.lbl_status = ck.CTkLabel(self.frame,text="فایل در دسترس نیست" ,bg_color="#ffffff",width=600, height=30,font=self.font,text_color="#000000")
        self.lbl_status.place(x=0,y=480)

    
        
    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
        )
        patern = Patern.getIndex(self.numberPatern.get(),self.patern)
        if patern != 0:
            self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
            self.lbl_path.configure(text=self.path_file)
            self.Excell = ExcellData(self.path_file)
            self.CSV = CSVFile(self.path_file)
            result = self.Excell.checkExcel(patern)
        
            if result == None:
                CTkMessagebox(title="خطا",message="فایل انتخابی مشکل دارد لطفا دوباره انتخاب کنید",icon="cancel")
                self.lbl_path.configure(text="")
            else:
                messageItem = ["صورتحساب","اقلام صورتحساب","پرداخت‌های صورتحساب"]
                self.status = True
                for i,r in enumerate(result):
                    if r == 0:  
                        CTkMessagebox(title="خطا", message=" تعداد ستون های" + " " + messageItem[i] + " " + "در الگوی انتخابی مقایرت دارد",icon="cancel")
                        self.status = False
                        self.lbl_status.configure(text="فایل خطا دار",bg_color="#a3001b")
                        self.lbl_path.configure(text="")
                if self.status : 
                    self.lbl_status.configure(text="دیتا آماده ارسال",bg_color="#08a300")
                    self.numberPatern.configure(state='disabled')
                
        else:
            CTkMessagebox(title='انتخاب الگو',message="نوع الگوی فاکتور را انتخاب کنید",icon="warning")

    def reset_form(self):
        self.lbl_status.configure(text="فایل در دسترس نیست",bg_color="#ffffff")
        self.lbl_path.configure(text="" )
        for child in self.group_date.winfo_children():
            child.configure(state='normal')
        
        for child in self.group_file.winfo_children():
            child.configure(state='normal')

        self.btn_selectFile.configure(state="normal")
        self.btn_reset.configure(state="normal")
    
    def checkToken(self,username):
        try:
            with open("string.txt", "rb") as f1, open("key.txt", "rb") as f2:
                token = f1.read()
                key = f2.read()

            f = Fernet(key)
            what_d = str(f.decrypt(token),'utf-8') 
            r = hashlib.md5(str.encode(username[:10]))
            if what_d != r.hexdigest():
                CTkMessagebox(title="دسترسی",message="نام کاربری مجاز نمیباشد",icon="cancel")
                return False
            else:
                return True
        except:
            CTkMessagebox(title="دسترسی",message="نام کاربری مجاز نمیباشد",icon="cancel")
            return False
    
    def LockElement(self):
        for child in self.group_date.winfo_children():
            child.configure(state='disable')
        
        for child in self.group_file.winfo_children():
            child.configure(state='disable')

        self.btn_selectFile.configure(state="disabled")
        self.btn_reset.configure(state="disabled")

    def send_invoice(self):
        self.lbl_number_allFactor.configure(text="0")
        self.lbl_number_ErrorFactor.configure(text="0")
        self.lbl_number_sendFactor.configure(text="0")
        self.lbl_number_successFactor.configure(text="0")
        str_usename = self.username
        str_password = self.password
        vdate = self.valDate.get()
        # today = date.today()
        
        if str_usename == '' or str_password == '':
            CTkMessagebox(title="ورود",message="نام کاربری ویا کلمه عبور را به درستی وارد کنید",icon="cancel")
        elif vdate == 0 :
            CTkMessagebox(title="نوع تاریخ",message="نوع ورودی تاریخ را مشخص نمایید",icon="cancel")
        else:
            c = self.checkToken(str_usename)
            if c:
                self.LockElement()
                self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")

                if self.status :
                    invoices = self.Excell.getInvoice()
                    items = self.Excell.getInvoiceItem()
                    payments = self.Excell.getPayment()
                    
                    
                    self.progressbar.configure(maximum=len(invoices))
                    sucessCount = 0
                    errorCount = 0
                    
                    
                    if len(invoices) <= 0:
                        CTkMessagebox(title="دیتا",message="تعداد صورتحساب ها صفر می باشد",icon="warning")
                    elif len(items) <= 0:
                        CTkMessagebox(title="دیتا",message="تعداد آیتم صورتحساب ها صفر می باشد",icon="warning")
                    else:
                        inD = InvoiceData(items,payments)
                        listInvoice = []
                        listIndex = []
                        counter = 0
                        patern = Patern.getIndex(self.numberPatern.get(),self.patern)
                        # if patern == 1:
                        #     self.Excell.preparationExcellN11()
                        # elif patern == 2:
                        #     self.Excell.preparationExcellN21()
                        self.lbl_number_allFactor.configure(text=str(len(invoices)))
                        self.frame.after(500)
                        self.frame.update()
                        
                        for index, invoice in enumerate(invoices):
                        
                        
                            if patern == 1:
                                i = inD.generateInvoiceNo1(invoice,vdate)
                                listInvoice.append(i)
                            elif patern == 2:
                                i = inD.generateInvoiceNo2(invoice,vdate)
                                listInvoice.append(i)
                            listIndex.append([index + 1 ,invoice[0],i['uniqueId']])
                            counter += 1
                            
                            if counter == setting.BatchSizeOfInvoices or  index ==  (len(invoices) - 1) :
                                # print (listIndex)
                                token = api.getToken(str_usename,str_password)
                                if token != "":
                                    # import json
                                    # json_object = json.dumps(listInvoice)
                                    # with open("sample1.json", "w") as outfile:
                                    #      outfile.write(json_object)
                                    result = api.sendInvoice(listInvoice,token)
                                    # curentTime = time.strftime("%H:%M:%S")
                                    if result[0] == 200:
                                        indexResult = lambda x,xy : [y for y in xy if y['uniqueId'] == x ] 
                                        data = result[1]['data']
                                        for invoiceItem in listIndex:
                                            dataResultPerInvoice = indexResult(invoiceItem[2],data)
                                            for i,d in enumerate(dataResultPerInvoice):
                                                if  d['status'] == 3:
                                                    try:
                                                        self.CSV.saveData([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status'],d['taxSerialNumber']])
                                                    except:
                                                         self.CSV.saveData([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status']])
                                                    sucessCount += 1
                                                else:
                                                    self.CSV.saveError([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status'],d['title'],d['description']])
                                                    if i == 0:
                                                        errorCount += 1
                                    
                                    else:
                                        for invoiceItem in listIndex: 
                                            self.CSV.saveError([invoiceItem[0],invoiceItem[1],invoiceItem[2],result[0],result[1]])
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
                            
                        CTkMessagebox(title="اتمام",message="تعداد %d فاکتور با موفقیت ارسال گردید میتوانید نتیجه را در دو فایل خطا و ثبت موفقیت در مکان فایل اصلی مشاهده نمایید"%len(invoices),icon="info")
                else:
                    CTkMessagebox(title="بارگزاری اکسل",message="لطفاً فایل را به درستی در قالب مناسب بارگزاری نمایید.",icon="cancel")
                self.reset_form()