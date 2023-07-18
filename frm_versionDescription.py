import customtkinter as ck
from package.CTkMessagebox import CTkMessagebox
from model.setting import VersionApp
import tkinter as tk
from tkinter import Scrollbar

class DescriptinVersion :
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.base = ck.CTk()
        self.base.title("Eitak Version")
        self.base.geometry("500x500")
        self.base.iconbitmap("media/image/logo.ico")
        screen_width = self.base.winfo_screenwidth()
        screen_height = self.base.winfo_screenheight()
        x = (screen_width // 2) - (500 // 2)
        y = (screen_height // 2) - (500 // 2)
        self.base.geometry("+{}+{}".format(x, y))
        self.base.resizable(0,0)

        self.font : tuple = ("Tahoma",12)

        self.frame_data = ck.CTkFrame(self.base,border_width=2, width=480, height=50)
        self.frame_data.place(x=10,y=10)



        lbl_header = ck.CTkLabel(self.frame_data,text="تغییرات نسخه" + "  " + VersionApp.version ,font= ("Tahoma",18))
        lbl_header.place(x=150 ,y=10)  

        self.text = tk.Text(self.base, font=self.font,wrap="word", state="normal",width=50,height=20)
        self.text.place(x=10,y=70)
       


        self.text.tag_configure("rtl", justify="right")
        self.text.configure(state="normal")

        self.scrollbar = tk.Scrollbar(self.base,command=self.text.yview)
        self.scrollbar.place(x=10+self.text.winfo_reqwidth(), y=70,height=self.text.winfo_reqheight())
        self.text['yscrollcommand'] = self.scrollbar.set

        self.text.insert("end", "در فایل اکسل ارسال صورتحساب در شیت اقلام صورتحساب ستون 'شرح اضافی کالا/خدمت' افزوده گردید لطفاً نسبت به دانلود نسخه جدید اکسل در قسمت راهنما اقدان نمایید \n\n", "rtl")
       
        self.text.insert("end", "تمامی مقادیر ریالی بجز 'مبلغ واحد' بدون اعشار می باشد\n\n", "rtl")
     
        self.text.insert("end","  نرخ ارزش افزوده باید مطابق با شناسه کالا عمومی /خصوصی کالا که از طرف مالیات اعلام گردیده باشد ", "rtl")

        self.text.configure(state="disabled")


        self.btn_sendInvoice = ck.CTkButton(self.base,text="متوجه شدم",font=self.font,command=self.closeForm)
        self.btn_sendInvoice.place(x=170,y=463)



        self.base.mainloop()
    
    def closeForm (self):
        self.base.destroy()
        from frm_main import MainPanel
        MainPanel(self.username,self.password)


if __name__ == "__main__":
    DescriptinVersion("","")