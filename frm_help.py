# import sys
# sys.path.append('..')
import customtkinter as ck
import tkinter as tk
import json
import urllib.request
import webbrowser


class FormHelp():
    def __init__(self,frame:ck.CTkFrame) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80,fg_color="#ffbe76")
        self.group_date.place(x=10,y=10)
        lbl_war2 = ck.CTkLabel(self.group_date,text="برای دریافت هر یک از قالب های مورد نیاز بر روی فایل مورد نظر کلیک کنید",font=self.font,text_color="#000")
        lbl_war2.place(x=70,y=20)
        #radioButom:
        self.group_btn = ck.CTkFrame(self.frame,border_width=2, width=570, height=180)
        self.group_btn.place(x=10,y=100)

        lbl_patern11 = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ثبت صورتحساب نوع 1 الگوی 1 فروش همراه با اطلاعات خریدار",font=self.font)
        lbl_patern11.place(x=120,y=10)

        self.btn_patern11 = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_patern11,width=50)
        self.btn_patern11.place(x=10,y=10)

        lbl_patern21 = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ثبت صورتحساب نوع 2 الگوی 1 فروش بدون اطلاعات خریدار",font=self.font)
        lbl_patern21.place(x=137,y=50)

        self.btn_patern21 = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_patern21,width=50)
        self.btn_patern21.place(x=10,y=50)

        lbl_revoke = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ابطال دسته‌ای صورتحساب‌ها",font=self.font)
        lbl_revoke.place(x=305,y=90)

        self.btn_revoke = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_revoke,width=50)
        self.btn_revoke.place(x=10,y=90)

        
        lbl_delete = ck.CTkLabel(self.group_btn,text="دانلود فایل راهنمای حذف دسته‌ای صورتحساب‌ها",font=self.font)
        lbl_delete.place(x=280,y=130)

        self.lbl_delete = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_delete,width=50)
        self.lbl_delete.place(x=10,y=130)
        
    def download_patern11(self):
        url = "https://files.mizeonline.ir/tps/assets/sample/Invoice_InvoicePatternId_1.xlsx"  
        # file_name = "Invoice_InvoicePatternId_1.xlsx"  # Replace with your desired file name
        # urllib.request.urlretrieve(url, file_name)
        webbrowser.open(url)
   
    def download_patern21(self):
        url = "https://files.mizeonline.ir/tps/assets/sample/Invoice_InvoicePatternId_21.xlsx"  # Replace with your file URL
        # file_name = "Invoice_InvoicePatternId_21.xlsx"  # Replace with your desired file name
        # urllib.request.urlretrieve(url, file_name)
        webbrowser.open(url)

    def download_revoke(self):
        url = "https://files.mizeonline.ir/tps/assets/sample/Invoice_InvoicePatternId_99.xlsx"  # Replace with your file URL
        # file_name = "Invoice_InvoicePatternId_99.xlsx"  # Replace with your desired file name
        # urllib.request.urlretrieve(url, file_name)
        webbrowser.open(url)

    def download_delete(self):
        url = "https://files.mizeonline.ir/tps/assets/sample/Invoice_Remove.xlsx"  # Replace with your file URL
        # file_name = "Invoice_InvoicePatternId_99.xlsx"  # Replace with your desired file name
        # urllib.request.urlretrieve(url, file_name)
        webbrowser.open(url)
