import os
import sys
sys.path.append(os.getcwd())
import customtkinter as ck
import webbrowser
from package.CTkMessagebox import CTkMessagebox
from module.api import ApiKeysun
from model.setting import VersionApp, Location
from forms.frm_versionDescription import DescriptinVersion


class FormHelp():
    def __init__(self,frame:ck.CTkFrame) -> None:
        self.frame = frame
        self.api = ApiKeysun()
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80,fg_color="#ffbe76")
        self.group_date.place(x=10,y=10)
        lbl_war2 = ck.CTkLabel(self.group_date,text="برای دریافت هر یک از قالب های مورد نیاز بر روی فایل مورد نظر کلیک کنید",font=self.font,text_color="#000")
        lbl_war2.place(x=70,y=20)
        #radioButom:
        self.group_btn = ck.CTkFrame(self.frame,border_width=2, width=570, height=420)
        self.group_btn.place(x=10,y=100)
        
        ylocation = Location(0,10,0,40)
       
        ####################################
        lbl_patern11 = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ثبت صورتحساب نوع 1 الگوی 1 فروش همراه با اطلاعات خریدار",font=self.font)
        lbl_patern11.place(x=120,y=ylocation.setRowLocation(0) )

        self.btn_patern11 = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_patern11,width=50)
        self.btn_patern11.place(x=10,y=ylocation.setRowLocation(0))
        ####################################

        lbl_patern21 = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ثبت صورتحساب نوع 2 الگوی 1 فروش بدون اطلاعات خریدار",font=self.font)
        lbl_patern21.place(x=137,y=ylocation.setRowLocation(1) )

        self.btn_patern21 = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_patern21,width=50)
        self.btn_patern21.place(x=10,y=ylocation.setRowLocation(1))
        ####################################

        lbl_patern13 = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ثبت صورتحساب نوع 1 الگوی3 طلا و جواهر با اطلاعات خریدار",font=self.font)
        lbl_patern13.place(x=130,y=ylocation.setRowLocation(2) )

        self.btn_patern13 = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_patern13,width=50)
        self.btn_patern13.place(x=10,y=ylocation.setRowLocation(2))

         ####################################

        lbl_patern23 = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ثبت صورتحساب نوع 2 الگوی 3 طلا و جواهر بدون اطلاعات خریدار",font=self.font)
        lbl_patern23.place(x=103,y=ylocation.setRowLocation(3) )

        self.btn_patern23 = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_patern23,width=50)
        self.btn_patern23.place(x=10,y=ylocation.setRowLocation(3))

        ######################################

        
        lbl_patern23 = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ثبت صورتحساب نوع 1 الگوی 5 قبض",font=self.font)
        lbl_patern23.place(x=260,y=ylocation.setRowLocation(4) )

        self.btn_patern23 = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_patern15,width=50)
        self.btn_patern23.place(x=10,y=ylocation.setRowLocation(4))

        ######################################

        lbl_revoke = ck.CTkLabel(self.group_btn,text="دانلود راهنمای ابطال دسته‌ای صورتحساب‌ها",font=self.font)
        lbl_revoke.place(x=303,y=ylocation.setRowLocation(5))

        self.btn_revoke = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_revoke,width=50)
        self.btn_revoke.place(x=10,y=ylocation.setRowLocation(5))

        #########################################

        lbl_delete = ck.CTkLabel(self.group_btn,text="دانلود فایل راهنمای حذف دسته‌ای صورتحساب‌ها",font=self.font)
        lbl_delete.place(x=275,y=ylocation.setRowLocation(6))

        self.lbl_delete = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_delete,width=50)
        self.lbl_delete.place(x=10,y=ylocation.setRowLocation(6))

        ##########################################
         
        lbl_bill = ck.CTkLabel(self.group_btn,text=" دانلود فایل ارسال صورتحساب های بارنامه" + VersionApp.version,font=self.font)
        lbl_bill.place(x=280,y=ylocation.setRowLocation(7))

        self.btn_bill = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.OpenDescriptinVersion,width=50)
        self.btn_bill.place(x=10,y=ylocation.setRowLocation(7))

        ###########################################
           
        lbl_help = ck.CTkLabel(self.group_btn,text="دانلود فایل راهنمای ایتاک نسخه  " + VersionApp.version,font=self.font)
        lbl_help.place(x=328,y=ylocation.setRowLocation(8))

        self.btn_help = ck.CTkButton(self.group_btn,text="دانلود",font=self.font,command=self.download_help,width=50)
        self.btn_help.place(x=10,y=ylocation.setRowLocation(8))

        ############################################
          
        lbl_view = ck.CTkLabel(self.group_btn,text="   مشاهده آخرین تغییرات نسخه " + VersionApp.version,font=self.font)
        lbl_view.place(x=328,y=ylocation.setRowLocation(9))

        self.btn_view = ck.CTkButton(self.group_btn,text="نمایش",font=self.font,command=self.OpenDescriptinVersion,width=50)
        self.btn_view.place(x=10,y=ylocation.setRowLocation(9))

        #############################################
        
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

    def download_patern13(self):
        url = "https://files.mizeonline.ir/tps/assets/sample/Invoice_InvoicePatternId_3.xlsx"  # Replace with your file URL
        # file_name = "Invoice_InvoicePatternId_21.xlsx"  # Replace with your desired file name
        # urllib.request.urlretrieve(url, file_name)
        webbrowser.open(url)

    def download_patern23(self):
        url = "https://files.mizeonline.ir/tps/assets/sample/Invoice_InvoicePatternId_23.xlsx"  # Replace with your file URL
        # file_name = "Invoice_InvoicePatternId_21.xlsx"  # Replace with your desired file name
        # urllib.request.urlretrieve(url, file_name)
        webbrowser.open(url)

    def download_patern15(self):
        url = "https://files.mizeonline.ir/tps/assets/sample/Invoice_InvoicePatternId_5.xlsx"  # Replace with your file UR
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

    def download_help(self):
        url = self.api.GetURL_Help()
        if url == "0":
            CTkMessagebox(title="خطای شبکه", message="ممکن است در سرور خطایی رخ داده شده باشد لطفاً دوباره امتحان کنید",icon="warning")
        elif url == "O":
            CTkMessagebox(title="خطای سرور", message="ممکن است در سرور خطایی رخ داده شده باشد لطفاً دوباره امتحان کنید",icon="warning")

        else:
            webbrowser.open(url)

    def OpenDescriptinVersion(self):
        DescriptinVersion("","",2)