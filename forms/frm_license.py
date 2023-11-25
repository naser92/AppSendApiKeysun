import os
import sys
sys.path.append(os.getcwd())
import customtkinter as ck
from tkinter import messagebox
from module.api   import ApiKeysun
from cryptography.fernet import Fernet
import hashlib
from model.setting import VersionApp
import os

class LicenseForm():
    def __init__(self) -> None:
        self.api = ApiKeysun()
        self.base = ck.CTk()
        self.base.title("Eitak License")
        self.base.geometry("300x200")
        self.base.eval('tk::PlaceWindow . center')
        self.base.resizable(0,0)
        self.font: tuple = ("Tahoma",12)
        self.version = VersionApp.version

        # button = ck.CTkButton(self.base, text="my button")
        # button.grid(row=0, column=0, padx=20, pady=20)
      
        # ck.CTkLabel(self.base,bg="#d1ccc0",text="(EITAK  نرم افزار ارسال صورتحساب کیسان (ایتاک" ,width="300",height="4").pack()
        label = ck.CTkLabel(self.base,text="نرم افزار ساخت لایسنس ایتاک" ,width=300,height=50,anchor="center",font=("Tahoma",14))
        label.grid(row=0, column=0, padx=0, pady=0)

         
       
        self.txt_username = ck.CTkEntry(self.base,width=280,placeholder_text="username")
        self.txt_username.place(x=10,y=70)


        self.btn_testLogin = ck.CTkButton(self.base,text="ساخت لایسنس",font=("Tahoma",12),command=self.license_generate)
        self.btn_testLogin.place(x=80,y=130)

        self.base.mainloop()

    def encry(self,code):

        key = Fernet.generate_key()
        f = Fernet(key)

        what_b = str.encode(code)
        token = f.encrypt(what_b)
        string = os.path.join(self.folder_path, "string.txt")
        key_add = os.path.join(self.folder_path, "key.txt")
        try:
            with open(string, "wb") as f1, open(key_add, "wb") as f2:
                f1.write(token)
                f2.write(key)
            messagebox.showinfo("موفقیت","با موفقیت ساخته شد")
        except:
            messagebox.showerror("خطا","متاسفانه در ساخت لایسنس با خطا مواجه شدید")



    def license_generate(self):
        str_usename = self.txt_username.get()
        if len(str_usename) < 10 :
            messagebox.showerror("خطا ورودی", "نام کاربری نباید از 10 رقم کمتر باشد")
        else:
            current_directory = os.path.abspath(os.curdir)
            self.folder_path = os.path.join(current_directory ,"license_" + str_usename)
            try:
                os.makedirs(self.folder_path)
            except:
                pass
            r = hashlib.md5(str.encode(str_usename[:10]))
            self.encry(r.hexdigest())





if __name__ == "__main__":
    LicenseForm()