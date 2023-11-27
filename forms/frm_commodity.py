import os
import sys
sys.path.append(os.getcwd())
import customtkinter as ck
from tkinter import ttk
from tkinter import filedialog as fd
from module.ExcellData import ExcellData
from module.csvFile import CSVFile
from module.connection import CheckInternet
from package.CTkMessagebox import CTkMessagebox
import pandas as pd
import threading
import time
from module.api import ApiKeysun
import math
from module.resultProcess import CheckResultCommodityRequest

api = ApiKeysun() 
class FormCommodity():
    def __init__(self,frame:ck.CTkFrame,username, password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.status = False
        self.username = username
        self.password = password

        
        #warning:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80,fg_color="#ffbe76")
        self.group_date.place(x=10,y=10)

        lbl_war = ck.CTkLabel(self.group_date,text="لطفاً برای اضافه نمودن کالاهای خود از قالب مناسب استفاده کنید",font=self.font12,text_color="#000")
        lbl_war.place(x=220,y=10)
        lbl_war2 = ck.CTkLabel(self.group_date,text="فایل اکسل در قالب مناسب را می توانید در این جا دانلود کنید",font=self.font12,text_color="#000")
        lbl_war2.place(x=240,y=45)

        
        self.btn_selectFile = ck.CTkButton(self.group_date,text="دانلود فایل",font=self.font)#,command=self.select_file
        self.btn_selectFile.place(x=20,y=45)


        #input data
        self.frame_data = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_data.place(x=10,y=100)

        lbl_input = ck.CTkLabel(self.frame_data,text=" :ورود فایل",font=self.font)
        lbl_input.place(x=480,y=25)

        self.lbl_path = ck.CTkLabel(self.frame_data,bg_color="#ffffff",width=275,height=20,text="",text_color="#000000")
        self.lbl_path.place(x=180,y=30)

        self.btn_selectFile = ck.CTkButton(self.frame_data,text="انتخاب فایل",font=self.font,command=self.select_file)
        self.btn_selectFile.place(x=20,y=25)

        #send element
        self.group_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_send.place(x=10,y=220)

        self.btn_sendInvoice = ck.CTkButton(self.group_send,text="ارسال محصولات",font=self.font,command=self.thread_send_commodity)#,command=self.deleteInvoice
        self.btn_sendInvoice.place(x=400,y=10)
        
        self.progressbar = ttk.Progressbar(self.group_send)
        self.progressbar.place(x=20,y=50,width=520)

        #Result
        ck.CTkLabel(self.frame,text="تعداد کل کالا/خدمت",font=self.font12).place(x=455,y=320)
        self.lbl_number_allCommodity  =  ck.CTkLabel(self.frame,text="0")  
        self.lbl_number_allCommodity.place(x=350,y=320)   
        
        ck.CTkLabel(self.frame,text="تعداد کالا/خدمت ارسالی",font=self.font12).place(x=450,y=350)  
        self.lbl_number_sendCommodity  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_sendCommodity.place(x=350,y=350)   

        ck.CTkLabel(self.frame,text="کالا/خدمت ثبت شده",font=self.font12).place(x=470,y=380)
        self.lbl_number_successCommodity  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_successCommodity.place(x=350,y=380) 

        ck.CTkLabel(self.frame,text="کالا/خدمت خطادار",font=self.font12).place(x=480,y=410)
        self.lbl_number_ErrorCommodity  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_ErrorCommodity.place(x=350,y=410) 


        self.lbl_status = ck.CTkLabel(self.frame,text="فایل در دسترس نیست" ,bg_color="#ffffff",width=600, height=30,font=self.font,text_color="#000000")
        self.lbl_status.place(x=0,y=580)


    # select file and uploadFile
    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
        )
        self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_path.configure(text=self.path_file)
        self.lbl_status.configure(text="داده در حال بارگزاری لطفاً منتظر بمانید ...",bg_color="#34495e")
        self.Excell = ExcellData(self.path_file)
        self.CSV = CSVFile(self.path_file)
        result = self.Excell.checkExcelCommodity()

        if not result:
            CTkMessagebox(title="خطا", message="تعداد ستون های اکسل انتخابی با نمونه مورد نظر مطابقت دارد",icon="cancel")
            self.status = False
            self.lbl_status.configure(text="فایل خطا دار",bg_color="#a3001b")
            self.lbl_path.configure(text="")
        else:
            self.status = True
            self.lbl_status.configure(text="دیتا آماده ارسال",bg_color="#08a300")

    def startAction(self):
        self.lbl_number_allCommodity.configure(text="0")
        self.lbl_number_ErrorCommodity.configure(text="0")
        self.lbl_number_sendCommodity.configure(text="0")
        self.lbl_number_successCommodity.configure(text="0")
        self.btn_sendInvoice.configure(state="disabled")
        self.btn_selectFile.configure(state="disabled")
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()

    def thread_send_commodity(self):
        self.sendInvoice_tread = threading.Thread(target=self.send_request)
        self.sendInvoice_tread.daemon = True
        self.sendInvoice_tread.start()

    def lockElement(self):
        pass
    
    def ResetElements(self):
        pass

    def updateFrame(self):
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()

    def check_connection(self):
        internet = CheckInternet()
        if internet.checkServerConnection():
            self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")
            return True
        else:
            self.lbl_status.configure(text="ارتباط با سرور قطع میباشد",bg_color="#a3001b")
            return False

    def send_request(self):
        self.startAction()
        str_username = self.username
        str_password = self.password

        if str_username == '' or str_password == '':
            CTkMessagebox(title="ورود",message="نام کاربری ویا کلمه عبور را به درستی وارد کنید",icon="cancel")
            self.btn_sendInvoice.configure(state="normal")
        else:
            self.lbl_status.configure(text="لطفاً منتظر بمانید ...",bg_color="#9b59b6")
            token = api.getToken(str_username,str_password)

            if token != "":
                self.lockElement()
                if self.status:
                    self.lbl_status.configure(text="اطلاعات در حال پردازش است لطفاً منتظر بمانید ...",bg_color="#e67e22")
                    commodity = self.Excell.readExcelSheetCommodity()
                    
                    if commodity.empty:
                        CTkMessagebox(title="دیتا",message="تعداد صورتحساب ها صفر می باشد",icon="warning")
                    else: 
                        listCommodity = commodity[commodity['error'] == False]
                        if listCommodity.empty:
                            #print all row commodity only coloumn content : index,commodityCode,errormessage
                            columns = ['ExcelRowNumber','commodityCode','status','errorMessage']
                            self.CSV.SaveErrorSendInvoice(commodity.loc[:,columns])
                            CTkMessagebox(title="دیتا",message="لطفا خطاهای فایل را بررسی نمایید فایل csv خطا ها در کنار فایل اصلی میباشد",icon="warning")
                        else:
                            listCommodityError = commodity[commodity['error'] == True]
                            errorCount =  len(listCommodityError)
                            columns = ['ExcelRowNumber','commodityCode','status','errorMessage']
                            self.CSV.SaveErrorSendInvoice(listCommodityError.loc[:,columns])

                            sucessCount = 0
                            self.progressbar.configure(maximum=len(commodity))
                            self.progressbar['value'] = errorCount
                            self.progressbar.update()
                            self.lbl_number_allCommodity.configure(text=str(len(commodity)))
                            self.lbl_status.configure(text="در حال ارسال لطفا منتظر بمانید ...",bg_color="#009FBD")
                            self.updateFrame()

                            batch_size = 10
                            total_batches = math.ceil(len(listCommodity) / batch_size)
                            data_baches = [listCommodity[i * batch_size:(i + 1) * batch_size] for i in range(total_batches)]
                            for  data in data_baches:
                                try:
                                    repeat = True
                                    while repeat:
                                        repeat = not self.check_connection()    
                                        token = ""

                                        if repeat == False :
                                            token = api.getToken(str_username,str_password)
                                        
                                        if token != "" and repeat == False:
                                            datap = self.Excell.PreparationDataCommodity(data) 
                                            result = api.AddCommodity(datap,token)
                                            if result[0] == 200 and result[1]['error'] == False:
                                                check = CheckResultCommodityRequest(result[1]['data'],data)
                                                if check.countSuceeded() > 0 : 
                                                    r = check.getSuccessResult()
                                                    self.CSV.SaveSuccessSendCommodity(r)
                                                if check.countFailed() > 0 : 
                                                    r = check.getErrorResult()
                                                    self.CSV.SaveErrorSendCommodity(r)
                                                errorCount += check.countFailed()
                                                sucessCount += check.countSuceeded()
                                                repeat = False

                                            elif   result[0] == 200:
                                                
                                                recordData = check.FakeData(data,result[1]['traceId'],result[1]['message'])
                                                self.CSV.SaveErrorSendInvoice(recordData)
                                                errorCount += len(data) 
                                                repeat = False
                                               
                                            elif result[0] == 500:
                                                repeat = True
                                             
                                            else:
                                                try:
                                                    recordData = check.FakeData(data,result[0],result[1])
                                                    self.CSV.SaveErrorSendInvoice(recordData)
                                                    errorCount += len(data) 
                                                    repeat = False
                                                except:
                                                    time.sleep(50)
                                                    errorCount += len(data) 
                                                    repeat = False
                                                    continue
                                                pass

                                        else:
                                            repeat = True

                                    self.lbl_number_sendCommodity.configure(text=str(errorCount+sucessCount))
                                    self.updateFrame()

                                    # if self.fileError == None or self.fileError == "":
                                    #     self.fileError = self.CSV.getFileErrorSendInvoiceName()    
                                    
                                    self.lbl_number_ErrorCommodity.configure(text=str(errorCount))
                                    self.lbl_number_successCommodity.configure(text=str(sucessCount))
                                    value = errorCount + sucessCount
                                    self.progressbar['value'] = value
                                    self.updateFrame()

                                except  Exception as e:
    
                                    recordData = check.FakeData(data,"system_error",str(e))
                                    self.CSV.SaveErrorSendInvoice(recordData)
                                    continue
                    
                    CTkMessagebox(title="اتمام",message="تعداد %d کالا/خدمت با موفقیت ارسال گردید میتوانید نتیجه را در دو فایل خطا و ثبت موفقیت در مکان فایل اصلی مشاهده نمایید"%len(commodity),icon="info")
                    

                self.ResetElements()
            else:
                CTkMessagebox(title="ارتباط با سرور",message="ممکن است ارتباط اینترنت و یا مشکلی در سرور رخ داده باشد لطفاً دوباره امتحان نمایید",icon="cancel")
                self.lbl_status.configure(text="ممکن است ارتباط اینترنت و یا مشکلی در سرور رخ داده باشد",bg_color="#c0392b")
                self.btn_sendInvoice.configure(state="normal")


