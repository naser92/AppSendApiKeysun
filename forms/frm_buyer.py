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


class FormBuyer():
    def __init__(self,frame:ck.CTkFrame,username, password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.status = False
        self.username = username
        self.passwoerd = password

        #warning:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80,fg_color="#ffbe76")
        self.group_date.place(x=10,y=10)

        lbl_war = ck.CTkLabel(self.group_date,text="لطفاً برای اضافه نمودن خریداران خود از قالب مناسب استفاده کنید",font=self.font12,text_color="#000")
        lbl_war.place(x=220,y=10)
        lbl_war2 = ck.CTkLabel(self.group_date,text="فایل اکسل در قالب مناسب را می توانید در این جا دانلود کنید",font=self.font12,text_color="#000")
        lbl_war2.place(x=240,y=45)

        self.btn_selectFile = ck.CTkButton(self.group_date,text="دانلود فایل",font=self.font)#,command=self.select_file
        self.btn_selectFile.place(x=20,y=45)

         #warning:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=40,fg_color="#e74c3c")
        self.group_date.place(x=10,y=100)

        lbl_war = ck.CTkLabel(self.group_date,text="لطفاً برای اضافه نمودن خریداران از نوع مشارکت مدنی حتماً شناسه اقتصادی در اکسل پر شود",font=self.font12,text_color="#000")
        lbl_war.place(x=45,y=5)
        # lbl_war2 = ck.CTkLabel(self.group_date,text="فایل اکسل در قالب مناسب را می توانید در این جا دانلود کنید",font=self.font12,text_color="#000")
        # lbl_war2.place(x=240,y=45)

        
        

        #input data
        self.frame_data = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_data.place(x=10,y=150)

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
        ck.CTkLabel(self.frame,text="تعداد کل خریداران",font=self.font12).place(x=455,y=320)
        self.lbl_number_allCommodity  =  ck.CTkLabel(self.frame,text="0")  
        self.lbl_number_allCommodity.place(x=350,y=320)   
        
        ck.CTkLabel(self.frame,text="تعداد خریداران ارسالی",font=self.font12).place(x=450,y=350)  
        self.lbl_number_sendCommodity  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_sendCommodity.place(x=350,y=350)   

        ck.CTkLabel(self.frame,text="خریداران ثبت شده",font=self.font12).place(x=470,y=380)
        self.lbl_number_successCommodity  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_successCommodity.place(x=350,y=380) 

        ck.CTkLabel(self.frame,text="خریداران خطادار",font=self.font12).place(x=480,y=410)
        self.lbl_number_ErrorCommodity  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_ErrorCommodity.place(x=350,y=410) 


        self.lbl_status = ck.CTkLabel(self.frame,text="فایل در دسترس نیست" ,bg_color="#ffffff",width=600, height=30,font=self.font,text_color="#000000")
        self.lbl_status.place(x=0,y=580)

        
    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
        )
        self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_path.configure(text=self.path_file)
        self.lbl_status.configure(text="داده در حال بارگزاری لطفاً منتظر بمانید ...",bg_color="#34495e")
        self.Excell = ExcellData(self.path_file)
        self.CSV = CSVFile(self.path_file)
        result = self.Excell.checkExcelBuyer()

        if not result:
            CTkMessagebox(title="خطا", message="تعداد ستون های اکسل انتخابی با نمونه مورد نظر مطابقت دارد",icon="cancel")
            self.status = False
            self.lbl_status.configure(text="فایل خطا دار",bg_color="#a3001b")
            self.lbl_path.configure(text="")
        else:
            self.status = True
            self.lbl_status.configure(text="دیتا آماده ارسال",bg_color="#08a300")

    def thread_send_commodity(self):
        self.sendInvoice_tread = threading.Thread(target=self.send_request)
        self.sendInvoice_tread.daemon = True
        self.sendInvoice_tread.start()

    def send_request(self):
        pass