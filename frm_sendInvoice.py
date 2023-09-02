import customtkinter as ck
import tkinter
from tkinter import filedialog as fd
from module.ExcellData import ExcellData
from module.InvoiceData import InvoiceData
from module.csvFile import CSVFile
from module.api import ApiKeysun
from cryptography.fernet import Fernet
from package.CTkMessagebox import CTkMessagebox
import hashlib
from model.setting import SettingData
from tkinter import ttk
from frm_log import FormLog
import threading
import time
from model.formData import TypeInvoice_SendInvoice
from module.resultProcess import CheckResult,FackeRecord
from module.connection import CheckInternet
import math
import concurrent.futures
from functools import partial   
api = ApiKeysun() 
import pandas as pd
setting = SettingData()

class FormSendInvoice():
    def __init__(self,frame:ck.CTkFrame,username,password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.username = username
        self.password = password
        self.fileSuccess = None # مخصوص لاگ
        self.fileError = None
        self.patern = [
            TypeInvoice_SendInvoice(0,0,"انتخاب الگو صورتحساب"),
            TypeInvoice_SendInvoice(1,1,"نوع 1 الگوی 1 صورتحساب فروش همراه با اطلاعات خریدار"),
            TypeInvoice_SendInvoice(2,1,"نوع 2 الگوی 1 صورتحساب فروش بدون اطلاعات خریدار"),
            TypeInvoice_SendInvoice(1,3,"نوع 1 الگو 3 صورتحساب فروش با اطلاعات خریدار طلا و جواهرات"),
            TypeInvoice_SendInvoice(2,3,"نوع 2 الگو 3 صورتحساب فروش بدون اطلاعات خریدار طلا و جواهرات")
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

        self.numberPatern = ck.CTkComboBox(self.group_file, width=450,font=self.font,dropdown_font=self.font12,state="readonly",
                                            values=[self.patern[0].stringValue,self.patern[1].stringValue,self.patern[2].stringValue,self.patern[3].stringValue,self.patern[4].stringValue])
        
        self.numberPatern.place(x=20,y=10)
        self.numberPatern.set(self.patern[0].stringValue)

        lbl_selectTypeDate = ck.CTkLabel(self.group_file,text=" :ورود فایل",font=self.font)
        lbl_selectTypeDate.place(x=480,y=25)

        self.lbl_path = ck.CTkLabel(self.group_file,bg_color="#ffffff",width=350,height=20,text="",text_color="#000000")
        self.lbl_path.place(x=120,y=50)

        
        self.btn_selectFile = ck.CTkButton(self.group_file,text="انتخاب فایل",font=self.font,command=self.select_file,width=60)
        self.btn_selectFile.place(x=20,y=45)

        #send element
        self.group_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_send.place(x=10,y=220)

        self.btn_sendInvoice = ck.CTkButton(self.group_send,text="ارسال صورتحساب",font=self.font,command=self.thread_send_invoice)
        self.btn_sendInvoice.place(x=400,y=10)
        
        self.btn_reset = ck.CTkButton(self.group_send,text="کنسل",font=self.font,command=self.reset_form)
        self.btn_reset.place(x=20,y=10)

        self.progressbar =  ttk.Progressbar(self.group_send)
        self.progressbar.place(x=20,y=50,width=520)

        
        self.btn_ErrorLog = ck.CTkButton(self.frame,text="لاگ خطا",font=self.font,command=self.openFormLogError)
        self.btn_ErrorLog.place(x=20,y=320)
        self.btn_ErrorLog.configure(state="disabled")

        
        self.btn_successLog = ck.CTkButton(self.frame,text="لاگ موفقیت",font=self.font,command=self.openFromLogSuccess)
        self.btn_successLog.place(x=20,y=350)
        self.btn_successLog.configure(state="disabled")
        
        

        
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

    def openFormLogError(self):
        self.sendInvoice_tread.join()
        if self.fileError != None or self.fileError != "":
            frm = FormLog(self.fileError,self.frame)
            frm.show()
        else:
            CTkMessagebox(title="خطای فایل",message="فایل لاگ برای خطا ساخته نشده است",icon="cancel")
    
    def openFromLogSuccess(self):
        self.sendInvoice_tread.join()
        if self.fileSuccess != None or self.fileSuccess != "":
            frm = FormLog(self.fileSuccess,self.frame)
            frm.show()
        else:
            CTkMessagebox(title="خطای فایل",message="فایل لاگ برای درخواست های موفق ساخته نشده است",icon="cancel")

    def thread_send_invoice(self):
        self.sendInvoice_tread = threading.Thread(target=self.send_invoice)
        self.sendInvoice_tread.daemon = True
        self.sendInvoice_tread.start()

    
    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
        )
        patern = TypeInvoice_SendInvoice.getIndex(self.numberPatern.get(),self.patern)
        
        if patern[0] != 0:
            self.lbl_status.configure(text="درحال پردازش اطلاعات لطفاً صبرکنید",bg_color="#34495e")
            self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
            self.lbl_path.configure(text=self.path_file)
            self.Excell = ExcellData(self.path_file)
            self.CSV = CSVFile(self.path_file)
            result = self.Excell.checkExcellNew(patern[0],patern[1])
        
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


    def check_connection(self):
        internet = CheckInternet()
        if internet.checkServerConnection():
            self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")
            return True
        else:
            self.lbl_status.configure(text="ارتباط با سرور قطع میباشد",bg_color="#a3001b")
            return False

    def checkPermissions(self,token) -> bool:
        info = api.checkPakage(token)
        try:
            if info['basePackageTypeId'] == 1:
                return True
            elif info['basePackageTypeId'] != 0:
                CTkMessagebox(title="دسترسی",message="فقط کاربران طرح طلایی می توانند از این برنامه استفاده کنند",icon="warning")
                return False
            else:
                CTkMessagebox(title="ارتباط",message="ارتباط با سرور قطع میباشد لطفاً ارتباط به اینترنت را بررسی نمایید",icon="warning")
                return False
        except:
                CTkMessagebox(title="دسترسی",message="درحال حاضر هیچ طرحی برای کاربری شما ایجاد نشده است",icon="warning")
   
    def getIndexRow(self,invoices: pd.DataFrame ,uniqueId) -> int:
        row = invoices.loc[invoices['uniqueId'] == uniqueId ]

    def send_invoice(self):
        self.lbl_number_allFactor.configure(text="0")
        self.lbl_number_ErrorFactor.configure(text="0")
        self.lbl_number_sendFactor.configure(text="0")
        self.lbl_number_successFactor.configure(text="0")
        str_usename = self.username
        str_password = self.password
        vdate = self.valDate.get()
        self.fileError = ""
        self.fileError = ""
        self.btn_successLog.configure(state="disabled")
        self.btn_ErrorLog.configure(state="disabled")
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()

        # today = date.today()
        
        if str_usename == '' or str_password == '':
            CTkMessagebox(title="ورود",message="نام کاربری ویا کلمه عبور را به درستی وارد کنید",icon="cancel")
        elif vdate == 0 :
            CTkMessagebox(title="نوع تاریخ",message="نوع ورودی تاریخ را مشخص نمایید",icon="cancel")
        else:
            # c = self.checkToken(str_usename)
            token = api.getToken(str_usename,str_password)
            if token != "":
                if True:#self.checkPermissions(token):
                    self.LockElement()
                    self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")

                    if self.status:
                        patern = TypeInvoice_SendInvoice.getIndex(self.numberPatern.get(),self.patern)
                        typeId = patern[0]
                        patternId = patern[1]
                        invoices = self.Excell.readExcelSheet(typeId,patternId,0,vdate)
                        invoiceItems = self.Excell.readExcelSheet(typeId,patternId,1,vdate)
                        invoicePayments = self.Excell.readExcelSheet(typeId,patternId,2,vdate)
                        invoiceByIndex = self.Excell.invoiceByRowExcell(invoices)

                        self.progressbar.configure(maximum=len(invoices))
                        sucessCount = 0
                        errorCount = 0
                        
                        if len(invoices) <= 0:
                            CTkMessagebox(title="دیتا",message="تعداد صورتحساب ها صفر می باشد",icon="warning")
                        elif len(invoiceItems) <= 0:
                            CTkMessagebox(title="دیتا",message="تعداد آیتم صورتحساب ها صفر می باشد",icon="warning")
                        else:
                            self.lbl_number_allFactor.configure(text=str(len(invoices)))
                            self.frame.after(500)
                            self.frame.update()

                            if len(invoicePayments) == 0 :
                                invoicePayments = None

                            # num_threads = concurrent.futures.cpu_count() 
                            batch_size = 10
                            # with concurrent.futures.ThreadPoolExecutor() as executor:
                                
                            #     prepared_data = list(executor.map(self.Excell.PreparationData,[invoices,invoiceItems]))

                            #     for data in zip(*[iter(prepared_data)] * batch_size):



                            # Alldata = self.Excell.PreparationData(invoices,invoiceItems,invoicePayments)
                            total_batches = math.ceil(len(invoices) / batch_size)
                            # data_baches = [Alldata[i * batch_size:(i + 1) * batch_size] for i in range(total_batches)]
                            data_baches = [invoices[i * batch_size:(i + 1) * batch_size] for i in range(total_batches)]
                            # invoice_baches = [invoiceByIndex[i * batch_size:(i + 1) * batch_size] for i in range(total_batches)]
                            
                            for  data_b in data_baches:
                                # try:

                                    df_item = invoiceItems[(invoiceItems['invoiceNumber'].isin(data_b['invoiceNumber'])) & (invoiceItems['invoiceDate'].isin(data_b['invoiceDate']))]  
                                    if invoicePayments == None:
                                        df_pay = None
                                    else:
                                        df_pay = invoicePayments[(invoicePayments['invoiceNumber'].isin(data_b['invoiceNumber'])) & (invoicePayments['invoiceDate'].isin(data_b['invoiceDate']))]
                                    
                                    data = self.Excell.PreparationData(data_b,df_item,df_pay)
                                    # print (df_item)                                  
                                    repeat = True
                                    while repeat:
                                        repeat = not self.check_connection()
                                        token = ""

                                        if repeat == False :
                                            token = api.getToken(str_usename,str_password)

                                        if token != "" and repeat == False:
                                            result = api.SendInvoiceNew(data,token)
                                            if result[0] == 200 and result[1]['error'] == False:
                                                check = CheckResult(result[1]['data'],data_b)
                                                if check.countSuceeded() > 0 : 
                                                    r = check.getSuccessResult()
                                                    self.CSV.SaveSuccessSendInvoice(r)
                                                if check.countFailed() > 0 : 
                                                    r = check.getErrorResult()
                                                    self.CSV.SaveErrorSendInvoice(r)
                                                errorCount += check.countFailed()
                                                sucessCount += check.countSuceeded()
                                                repeat = False
                                            elif   result[0] == 200:
                                                fakeRecord = FackeRecord(data_b,result[1]['traceId'],result[1]['message'])
                                                recordData = fakeRecord.get_data()
                                                self.CSV.SaveErrorSendInvoice(recordData)
                                                errorCount += len(data) 
                                                repeat = False
                                               
                                            elif result[0] == 500:
                                                repeat = True
                                            
                                            else:
                                                try:
                                                    fakeRecord = FackeRecord(data_b,result[0],result[1])
                                                    recordData = fakeRecord.get_data()
                                                    self.CSV.SaveErrorSendInvoice(recordData)
                                                    errorCount += len(data) 
                                                    repeat = False
                                                except:
                                                    time.sleep(50)
                                                    errorCount += len(data) 
                                                    repeat = False
                                                    continue
                                        else:
                                            repeat = True
                            
                                    self.lbl_number_sendFactor.configure(text=str(errorCount+sucessCount))
                                    self.frame.update_idletasks()
                                    self.frame.after(500)
                                    self.frame.update()

                                    # set address error file log
                                    if self.fileError == None or self.fileError == "":
                                        self.fileError = self.CSV.getFileErrorSendInvoiceName()    
                                    
                                    self.lbl_number_ErrorFactor.configure(text=str(errorCount))
                                    self.lbl_number_successFactor.configure(text=str(sucessCount))
                                    value = errorCount + sucessCount
                                    self.progressbar['value'] = value
                                    self.progressbar.update()
                                    self.frame.update_idletasks()
                                    self.frame.after(500)
                                    self.frame.update()
                                # except Exception as e:
                                #     fakeRecord = FackeRecord(invoices,data,"system_error",str(e))
                                #     recordData = fakeRecord.get_data()
                                #     self.CSV.SaveErrorSendInvoice(recordData)
                                #     continue
                        #end For invocie    
                        if self.fileSuccess != None and self.fileSuccess != "":
                            self.btn_successLog.configure(state = "normal")   
                        
                        if self.fileError != None and self.fileError != "":
                            self.btn_ErrorLog.configure(state = "normal")

                        CTkMessagebox(title="اتمام",message="تعداد %d فاکتور با موفقیت ارسال گردید میتوانید نتیجه را در دو فایل خطا و ثبت موفقیت در مکان فایل اصلی مشاهده نمایید"%len(invoices),icon="info")
                # else:
                    # CTkMessagebox(title="بارگزاری اکسل",message="لطفاً فایل را به درستی در قالب مناسب بارگزاری نمایید.",icon="cancel")
                self.reset_form()
            else:
                CTkMessagebox(title="ارتباط با سرور",message="ممکن است ارتباط اینترنت و یا مشکلی در سرور رخ داده باشد لطفاً دوباره امتحان نمایید",icon="cancel")

