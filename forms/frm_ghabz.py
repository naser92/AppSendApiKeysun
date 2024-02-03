import os
import sys
sys.path.append(os.getcwd())
import customtkinter as ck
import tkinter
from tkinter import filedialog as fd
from module.ExcellData import ExcellData
from module.csvFile import CSVFile
from package.CTkMessagebox import CTkMessagebox
from tkinter import ttk
from model.setting import SettingData
from module.api import ApiKeysun
from model.formData import BillType_combo
from PIL import Image
import threading
from module.connection import CheckInternet
import math
from module.resultProcess import CheckResult,FackeRecord
import time

api = ApiKeysun() 
setting = SettingData()
class FormGhabz():
    def __init__(self,frame:ck.CTkFrame,username,password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.username = username
        self.password = password
        self.status = False
        self.path_file = None
        self.fileSuccess = None # مخصوص لاگ
        self.fileError = None
        self.BillType = [
            BillType_combo(0,0,"bill","سایر قبوض"),
            BillType_combo(1,5,"Water","قبض آب"),
            BillType_combo(1,5,"electric","قبض برق"),
            BillType_combo(1,5,"gaz","قبض گاز"),
            BillType_combo(1,5,"tell","قبض تلفن"),
        ]

        self.image_path = os.path.join(os.getcwd(), "media","image")

         #group_date:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_date.place(x=10,y=10)
        
        self.valDate = tkinter.IntVar()
        self.valDate.set(2)
        
        self.R2 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=2)
        self.R2.place(x=200,y=25)
        ck.CTkLabel(self.group_date,text="تاریخ ورودی شمسی",font=self.font).place(x=70,y=18)
        ck.CTkLabel(self.group_date,text="yyyy/mm/dd").place(x=105,y=45)

        self.R1 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=1)
        self.R1.place(x=410,y=25)
        ck.CTkLabel(self.group_date,text="تاریخ ورودی میلادی",font=self.font).place(x=290,y=18)
        ck.CTkLabel(self.group_date,text="yyyy-mm-dd").place(x=315,y=45)

        # for child in self.group_date.winfo_children():
        #     child.configure(state='disable')

        
        #inputfile
        self.group_file = ck.CTkFrame(self.frame,border_width=2, width=570, height=90)
        self.group_file.place(x=10,y=110)

        self.cmb_BillType = ck.CTkComboBox(self.group_file, width=450,font=self.font,dropdown_font=self.font12,state="readonly",command=self.changeImage,
                                            values=[self.BillType[0].stringViwe,self.BillType[1].stringViwe,self.BillType[2].stringViwe,self.BillType[3].stringViwe,self.BillType[4].stringViwe])
        
        self.cmb_BillType.place(x=20,y=10)
        self.cmb_BillType.set(self.BillType[0].stringViwe)

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

        self.logo_bill = ck.CTkImage(Image.open(os.path.join(self.image_path,"bill.png")),size=(70,60))
        self.img_logo = ck.CTkLabel(self.frame, image=self.logo_bill,text="")
        self.img_logo.place(x=230, y=340)

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



    def changeImage(self,choice):
        r = BillType_combo.getIndex(choice,self.BillType)
  
        r = r[2] + ".png"
        self.logo_bill = ck.CTkImage(Image.open(os.path.join(self.image_path,r)),size=(70,60))
        self.img_logo = ck.CTkLabel(self.frame, image=self.logo_bill,text="")
        self.img_logo.place(x=230, y=340)

    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
        )
        # ids =  BillType_combo.getIndex(self.cmb_BillType.get(),self.BillType)
        # if ids[0] != 0:
        self.lbl_status.configure(text="داده در حال بارگزاری لطفاً منتظر بمانید ...",bg_color="#34495e")
        self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_path.configure(text=self.path_file)
        self.dataProcessing  =  ExcellData(self.path_file)
        self.CSV = CSVFile(self.path_file)
        result = self.dataProcessing.check_count_col_excell(1,5,None)
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
                self.cmb_BillType.configure(state='disabled')
        # else:

        #     CTkMessagebox(title='انتخاب نوع قبض',message="نوع قبض را انتخاب کنید",icon="warning")


    def thread_send_invoice(self):
        self.sendInvoice_tread = threading.Thread(target=self.sendData)
        self.sendInvoice_tread.daemon = True
        self.sendInvoice_tread.start()


    def reset_form(self):
        self.lbl_status.configure(text="فایل در دسترس نیست",bg_color="#ffffff")
        self.lbl_path.configure(text="" )
        for child in self.group_date.winfo_children():
            child.configure(state='normal')
        
        for child in self.group_file.winfo_children():
            child.configure(state='normal')

        self.btn_selectFile.configure(state="normal")
        self.btn_reset.configure(state="normal")

        self.path_file = None

    def openFormLogError(self):
        pass

    def openFromLogSuccess(self):
        pass

    def startSendAction(self):
        self.lbl_number_allFactor.configure(text="0")
        self.lbl_number_ErrorFactor.configure(text="0")
        self.lbl_number_sendFactor.configure(text="0")
        self.lbl_number_successFactor.configure(text="0")
        self.fileError = ""
        self.fileError = ""
        self.btn_successLog.configure(state="disabled")
        self.btn_ErrorLog.configure(state="disabled")
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()
    
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
        

    def sendData(self):
        self.startSendAction()
        str_usename = self.username
        str_password = self.password
        vdate = self.valDate.get()

        if str_usename == '' or str_password == '':
            CTkMessagebox(title="ورود",message="نام کاربری ویا کلمه عبور را به درستی وارد کنید",icon="cancel")
        elif vdate == 0 :
            CTkMessagebox(title="نوع تاریخ",message="نوع ورودی تاریخ را مشخص نمایید",icon="cancel")
        elif self.path_file == None or self.path_file == "":
            CTkMessagebox(title="فایل",message="فایلی انتخاب نشده",icon="cancel")
        else:
            token = api.getToken(str_usename,str_password)
            if token != "":
                self.LockElement()
                if self.status:
                    self.lbl_status.configure(text="اطلاعات در حال پردازش است لطفاً منتظر بمانید ...",bg_color="#e67e22")
                    patern = BillType_combo.getIndex(self.cmb_BillType.get(),self.BillType)
                    typeId = 1
                    patternId = 5
                    bilTypeSTR = None
                    invoices = self.dataProcessing.readExcelSheet(typeId,patternId,0,bilTypeSTR,vdate)
                    invoiceItems = self.dataProcessing.readExcelSheet(typeId,patternId,1,bilTypeSTR,vdate)
                    invoicePayments = None
                                        

                    if len(invoices) <= 0:
                        CTkMessagebox(title="دیتا",message="تعداد صورتحساب ها صفر می باشد",icon="warning")
                        self.lbl_status.configure(text="فایل خطا دار",bg_color="#a3001b")
                        
                    elif len(invoiceItems) <= 0:
                        CTkMessagebox(title="دیتا",message="تعداد آیتم صورتحساب ها صفر می باشد",icon="warning")
                        self.lbl_status.configure(text="فایل خطا دار",bg_color="#a3001b")


                    else:
                        self.progressbar.configure(maximum=len(invoices))
                        sucessCount = 0
                        errorCount = 0
                        self.lbl_number_allFactor.configure(text=str(len(invoices)))
                        self.frame.after(500)
                        self.frame.update()

                        self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")

                        batch_size = 10
                        total_batches = math.ceil(len(invoices) / batch_size)
                        data_baches = [invoices[i * batch_size:(i + 1) * batch_size] for i in range(total_batches)]

                        for  data_b in data_baches:
                            try:
                                df_item = invoiceItems[(invoiceItems['invoiceNumber'].isin(data_b['invoiceNumber'])) & (invoiceItems['invoiceDate'].isin(data_b['invoiceDate']))]  

                                data = self.dataProcessing.PreparationData(data_b,df_item,None)
                                repeat = True
                                while repeat:

                                    repeat = not self.check_connection()
                                    
                                    if repeat == False :
                                        token = api.getToken(str_usename,str_password)
                                        self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")
                                    
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

                                        elif result[0] == 403:
                                            self.lbl_status.configure(text="شمادسترسی لازم برای ارسال صورتحساب را ندارید",bg_color="#e74c3c")
                                            break

                                        elif result[0] == 500:
                                            self.lbl_status.configure(text="خطا در سرور ارسال مجدد پاکت",bg_color="#e74c3c")
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

                            except Exception as e:
                                fakeRecord = FackeRecord(data_b,"system_error",str(e))
                                recordData = fakeRecord.get_data()
                                self.CSV.SaveErrorSendInvoice(recordData)
                                continue
                    #end For invocie
                        CTkMessagebox(title="اتمام",message="تعداد %d فاکتور با موفقیت ارسال گردید میتوانید نتیجه را در دو فایل خطا و ثبت موفقیت در مکان فایل اصلی مشاهده نمایید"%len(invoices),icon="info")
                                
                    if self.fileSuccess != None and self.fileSuccess != "":
                        self.btn_successLog.configure(state = "normal")   
                        
                    if self.fileError != None and self.fileError != "":
                        self.btn_ErrorLog.configure(state = "normal")

                    self.reset_form()
                
                else:
                    CTkMessagebox(title="ارتباط با سرور",message="ممکن است ارتباط اینترنت و یا مشکلی در سرور رخ داده باشد لطفاً دوباره امتحان نمایید",icon="cancel")