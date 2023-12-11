import os
import sys
sys.path.append(os.getcwd())
import customtkinter as ck
from tkinter import filedialog as fd
from module.ExcellData import ExcellData
from module.InvoiceData import InvoiceBill
from module.csvFile import CSVFile
from module.api import ApiKeysun
from cryptography.fernet import Fernet
from package.CTkMessagebox import CTkMessagebox
from model.formData import SelectionItems
import hashlib
from model.setting import SettingData
from tkinter import ttk
import time


api = ApiKeysun() 
setting = SettingData()

class FormBill():
    def __init__(self,frame:ck.CTkFrame,username,password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.username = username
        self.password = password
        self.fileSuccess = None # مخصوص لاگ
        self.fileError = None
        self.TypeInvoiceItems = [
            SelectionItems(0,"انتخاب الگو صورتحساب"),
            SelectionItems(1,"نوع صورتحساب 1 همراه با اطلاعات خریدار"),
            SelectionItems(2,"نوع صورتحساب 2 بدون اطلاعات خریدار")
        ]

        self.paternInvoiceItems = [
            SelectionItems(1,"فروش")
        ]

        self.SubjectInvoiceItems = [
            SelectionItems(1,"اصلی"),
            SelectionItems(2,"اصلاح"),
            SelectionItems(3,"ابطال"),
        ]


       
        #selection items:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=130)
        self.group_date.place(x=10,y=10)

       
        lbl_InvoiceType = ck.CTkLabel(self.group_date,text=" :  نوع صورتحساب ها",font=self.font)
        lbl_InvoiceType.place(x=400,y=10)

        self.InvoiceType = ck.CTkComboBox(self.group_date, width=300,font=self.font,dropdown_font=self.font12,state="readonly",
                                            values=[self.TypeInvoiceItems[0].string,self.TypeInvoiceItems[1].string,self.TypeInvoiceItems[2].string])
        self.InvoiceType.place(x=80,y=10)
        self.InvoiceType.set(self.TypeInvoiceItems[2].string)
        self.InvoiceType.configure(state='disable')

        ################################
        lbl_InvoicePatern = ck.CTkLabel(self.group_date,text=" :  الگو صورتحساب ها",font=self.font)
        lbl_InvoicePatern.place(x=400,y=50)

        self.InvoicePatern = ck.CTkComboBox(self.group_date, width=300,font=self.font,dropdown_font=self.font12,state="readonly",
                                            values=[self.paternInvoiceItems[0].string])
        self.InvoicePatern.place(x=80,y=50)
        self.InvoicePatern.set(self.paternInvoiceItems[0].string)
        self.InvoicePatern.configure(state='disable')


        ################################
        lbl_InvoiceSubject = ck.CTkLabel(self.group_date,text=" : موضوع صورتحساب ها",font=self.font)
        lbl_InvoiceSubject.place(x=400,y=90)

        self.InvoiceSubject = ck.CTkComboBox(self.group_date, width=300,font=self.font,dropdown_font=self.font12,state="readonly",
                                            values=[self.SubjectInvoiceItems[0].string,self.SubjectInvoiceItems[1].string,self.SubjectInvoiceItems[2].string])
        
        self.InvoiceSubject.place(x=80,y=90)
        self.InvoiceSubject.set(self.SubjectInvoiceItems[0].string)

        #select File 

        self.group_file = ck.CTkFrame(self.frame,border_width=2, width=570, height=50)
        self.group_file.place(x=10,y=150)

        lbl_selectTypeDate = ck.CTkLabel(self.group_file,text=" :ورود فایل",font=self.font)
        lbl_selectTypeDate.place(x=480,y=10)

        self.lbl_path = ck.CTkLabel(self.group_file,bg_color="#ffffff",width=350,height=20,text="",text_color="#000000")
        self.lbl_path.place(x=120,y=15)

        
        self.btn_selectFile = ck.CTkButton(self.group_file,text="انتخاب فایل",font=self.font,command=self.select_file,width=60)
        self.btn_selectFile.place(x=20,y=10)
        
        # self.valDate = tkinter.IntVar()
        
        # self.R2 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=2)
        # self.R2.place(x=200,y=25)
        # ck.CTkLabel(self.group_date,text="تاریخ ورودی شمسی",font=self.font).place(x=70,y=18)
        # ck.CTkLabel(self.group_date,text="yyyy/mm/dd").place(x=105,y=45)

    #     self.R1 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=1)
    #     self.R1.place(x=410,y=25)
    #     ck.CTkLabel(self.group_date,text="تاریخ ورودی میلادی",font=self.font).place(x=290,y=18)
    #     ck.CTkLabel(self.group_date,text="yyyy-mm-dd").place(x=315,y=45)

    #     lbl_selectTypeDate = ck.CTkLabel(self.group_date,text=" :انتخاب نوع تاریخ",font=self.font)
    #     lbl_selectTypeDate.place(x=450,y=20)

        #inputfile

    #     self.numberPatern = ck.CTkComboBox(self.group_file, width=450,font=self.font,dropdown_font=self.font12,state="readonly",
    #                                         values=[self.patern[0].string,self.patern[1].string,self.patern[2].string])
        
    #     self.numberPatern.place(x=20,y=10)
    #     self.numberPatern.set(self.patern[0].string)

        #send element
        self.group_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_send.place(x=10,y=220)

        self.btn_sendInvoice = ck.CTkButton(self.group_send,text="ارسال صورتحساب",font=self.font,command=self.send_invoice)
        self.btn_sendInvoice.place(x=400,y=10)
        
    #     self.btn_reset = ck.CTkButton(self.group_send,text="کنسل",font=self.font,command=self.reset_form)
    #     self.btn_reset.place(x=20,y=10)

        self.progressbar =  ttk.Progressbar(self.group_send)
        self.progressbar.place(x=20,y=50,width=520)

        
    #     self.btn_ErrorLog = ck.CTkButton(self.frame,text="لاگ خطا",font=self.font,command=self.openFormLogError)
    #     self.btn_ErrorLog.place(x=20,y=320)
    #     self.btn_ErrorLog.configure(state="disabled")

        
    #     self.btn_successLog = ck.CTkButton(self.frame,text="لاگ موفقیت",font=self.font,command=self.openFromLogSuccess)
    #     self.btn_successLog.place(x=20,y=350)
    #     self.btn_successLog.configure(state="disabled")
        
        

        
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
        self.lbl_status.place(x=0,y=580)

    # def openFormLogError(self):
    #     self.sendInvoice_tread.join()
    #     if self.fileError != None or self.fileError != "":
    #         frm = FormLog(self.fileError,self.frame)
    #         frm.show()
    #     else:
    #         CTkMessagebox(title="خطای فایل",message="فایل لاگ برای خطا ساخته نشده است",icon="cancel")
    
    # def openFromLogSuccess(self):
    #     self.sendInvoice_tread.join()
    #     if self.fileSuccess != None or self.fileSuccess != "":
    #         frm = FormLog(self.fileSuccess,self.frame)
    #         frm.show()
    #     else:
    #         CTkMessagebox(title="خطای فایل",message="فایل لاگ برای درخواست های موفق ساخته نشده است",icon="cancel")

    # def thread_send_invoice(self):
    #     self.sendInvoice_tread = threading.Thread(target=self.send_invoice)
    #     self.sendInvoice_tread.daemon = True
    #     self.sendInvoice_tread.start()

        

    
    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
        )
        
        
        self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_path.configure(text=self.path_file)
        self.Excell = ExcellData(self.path_file)
        self.CSV = CSVFile(self.path_file)
        result = self.Excell.excelCheckBill()
        self.status = False
        if result == False:
            CTkMessagebox(title="خطا",message="فایل انتخابی مشکل دارد و یا تعداد ستوئن های آن با نمونه خواسته شده مطابقت ندارد",icon="cancel")
            self.lbl_path.configure(text="")
            self.lbl_status.configure(text="فایل خطا دار",bg_color="#a3001b")
        else:
            self.lbl_status.configure(text="دیتا آماده ارسال",bg_color="#08a300")
            self.status = True

         
  

    def reset_form(self):
        self.lbl_status.configure(text="فایل در دسترس نیست",bg_color="#ffffff")
        self.lbl_path.configure(text="" )
        for child in self.group_date.winfo_children():
            child.configure(state='normal')
        
        for child in self.group_file.winfo_children():
            child.configure(state='normal')

        self.btn_selectFile.configure(state="normal")
        self.btn_sendInvoice.configure(state="normal")
        self.InvoiceType.configure(state='disable')
        self.InvoicePatern.configure(state='disable')

    
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
        self.btn_sendInvoice.configure(state="disabled")

    def send_invoice(self):
        self.lbl_number_allFactor.configure(text="0")
        self.lbl_number_ErrorFactor.configure(text="0")
        self.lbl_number_sendFactor.configure(text="0")
        self.lbl_number_successFactor.configure(text="0")
        str_usename = self.username
        str_password = self.password
        
        self.fileError = ""
        self.fileError = ""
       
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()

        # today = date.today()
        
        if str_usename == '' or str_password == '':
            CTkMessagebox(title="ورود",message="نام کاربری ویا کلمه عبور را به درستی وارد کنید",icon="cancel")
        else:
            c = self.checkToken(str_usename)
            if c:
                self.LockElement()
                self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")

                if self.status :
                    invoices = self.Excell.getBillInvoice()
                    
                    
                    
                    self.progressbar.configure(maximum=len(invoices))
                    sucessCount = 0
                    errorCount = 0
                    
                    
                    if len(invoices) <= 0:
                        CTkMessagebox(title="دیتا",message="تعداد صورتحساب ها صفر می باشد",icon="warning")
                    else:
                        listInvoice = []
                        listIndex = []
                        counter = 0
                        type = SelectionItems.getIndex(self.InvoiceType.get(),self.TypeInvoiceItems)
                        patern = SelectionItems.getIndex(self.InvoicePatern.get(),self.paternInvoiceItems)
                        subject = SelectionItems.getIndex(self.InvoiceSubject.get(),self.SubjectInvoiceItems)

                        inD = InvoiceBill(type, subject, patern)
                        # if patern == 1:
                        #     self.Excell.preparationExcellN11()
                        # elif patern == 2:
                        #     self.Excell.preparationExcellN21()
                        self.lbl_number_allFactor.configure(text=str(len(invoices)))
                        self.frame.after(500)
                        self.frame.update()
                        
                        for index, invoice in enumerate(invoices):
                        
                            try:
                                i = inD.generatBillInvoiceApi(invoice)
                                listIndex.append([index + 1 ,invoice[0],i['uniqueId']])
                                listInvoice.append(i)
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
                                        if result[0] == 200 and result[1]['error'] == False:
                                            indexResult = lambda x,xy : [y for y in xy if y['uniqueId'] == x ] 
                                            data = result[1]['data']
                                            for invoiceItem in listIndex:
                                                try:
                                                    dataResultPerInvoice = indexResult(invoiceItem[2],data)
                                                    for i,d in enumerate(dataResultPerInvoice):
                                                        try:
                                                            if  d['status'] == 3:
                                                                try:
                                                                    self.CSV.saveData([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status'],d['taxSerialNumber']])
                                                                except:
                                                                    self.CSV.saveData([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status']])
                                                                sucessCount += 1
                                                                #فعال کردن لاگ خطا
                                                                # state_btn_success = self.btn_successLog.cget("state") 
                                                                # if state_btn_success == "disabled":
                                                                #     self.btn_successLog.configure(state = "normal")

                                                                #  ست کردن آدرس فایل لاگ
                                                                if self.fileSuccess == None or self.fileSuccess == "":
                                                                    self.fileSuccess = self.CSV.getFileSuccessSendInvoiceName()
                                                                

                                                            else:
                                                                self.CSV.saveError([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status'],d['title'],d['description']])
                                                                if i == 0:
                                                                    errorCount += 1
                                                                #فعال کردن لاگ خطا
                                                                # state_btn_error = self.btn_ErrorLog.cget("state") 
                                                                # if state_btn_error == "disabled":
                                                                #     self.btn_ErrorLog.configure(state = "normal")
                                                        except:
                                                            time.sleep(50)
                                                            self.CSV.saveError["save_error","system_error","e1"] 
                                                            continue
                                                    #end for dataResultPerInvoice
                                                except:
                                                    time.sleep(50)

                                                    continue
                                            #end For ListIndex
                                        else:
                                            for invoiceItem in listIndex: 
                                                try:
                                                    self.CSV.saveError([invoiceItem[0],invoiceItem[1],invoiceItem[2],result[0],result[1]])
                                                    errorCount += 1
                                                except:
                                                    time.sleep(50)
                                                    continue
                                            #فعال کردن لاگ خطا
                                            # state_btn_error = self.btn_ErrorLog.cget("state") 
                                            # if state_btn_error == "disabled":
                                            #     self.btn_ErrorLog.configure(state = "normal")
                                    
                                    
                                    else:                    
                                        for invoiceItem in listIndex: 
                                            try:
                                                self.CSV.saveError([invoiceItem[0],invoiceItem[1],invoiceItem[2],"login_Error","سرویس در حال حاضر در دسترس نمیباشد"])
                                                errorCount += 1
                                            except:
                                                time.sleep(50)
                                                continue

                                    counter = 0
                                    listInvoice = []
                                    listIndex = []
                                    self.lbl_number_sendFactor.configure(text=str(index+1))
                                    self.frame.update_idletasks()
                                    self.frame.after(500)
                                    self.frame.update()

                                # set address error file log
                                if self.fileError == None or self.fileError == "":
                                    self.fileError = self.CSV.getFileErrorSendInvoiceName()    
                                
                                self.lbl_number_ErrorFactor.configure(text=str(errorCount))
                                self.lbl_number_successFactor.configure(text=str(sucessCount))
                                self.progressbar['value'] = index+1
                                self.progressbar.update()
                                self.frame.update_idletasks()
                                self.frame.after(500)
                                self.frame.update()
                            except:
                                self.CSV.saveError["save_error","system_error","e2"] 
                                continue    
                       

                        CTkMessagebox(title="اتمام",message="تعداد %d فاکتور با موفقیت ارسال گردید میتوانید نتیجه را در دو فایل خطا و ثبت موفقیت در مکان فایل اصلی مشاهده نمایید"%len(invoices),icon="info")
                else:
                    CTkMessagebox(title="بارگزاری اکسل",message="لطفاً فایل را به درستی در قالب مناسب بارگزاری نمایید.",icon="cancel")
                self.reset_form()