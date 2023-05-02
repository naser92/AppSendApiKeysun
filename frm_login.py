
from tkinter import*  
from tkinter import ttk
from tkinter.messagebox import showinfo , showwarning,showerror
from core.api   import ApiKeysun
from cryptography.fernet import Fernet
import hashlib


class LoginForm():
    def __init__(self ,base = Tk(),api = ApiKeysun() ) -> None:
        self.api = api
        self.base = base
        self.status = False
        self.base.geometry('300x200')
        self.base.title("EITAK")
        self.base.iconbitmap("data/logo.ico")
        self.base.eval('tk::PlaceWindow . center')
        self.base.resizable(0,0)

        Label(self.base,bg="#d1ccc0",text="(EITAK  نرم افزار ارسال صورتحساب کیسان (ایتاک" ,width="300",height="4").pack()

         
        Label(self.base,text="نام کاربری").place(x=220,y=70)
        self.txt_username = ttk.Entry(self.base,width=30)
        self.txt_username.place(x=10,y=70) 

        Label(self.base,text="کلمه عبور").place(x=220,y=100)
        self.txt_password = ttk.Entry(self.base,width=30,show='*')
        self.txt_password.place(x=10,y=100)

        self.btn_testLogin = ttk.Button(self.base,text="لاگین",command=self.loginTest)
        self.btn_testLogin.place(x=70,y=130)


    def generateForm(self) -> None:
        self.base.mainloop()  


    def loginTest(self):
            str_usename = self.txt_username.get()
            str_password = self.txt_password.get()
            if str_usename == '' or str_password == '':
                showwarning("ورود","نام کاربری ویا کلمه عبور را به درستی وارد کنید")
            else:
                c = self.checkToken(str_usename)
                if c:
                    token = self.api.getToken(str_usename,str_password)
                    if token != "":
                        self.base.destroy()
                        from frm_mainPanel import MainPanel
                        MainPanel(str_usename,str_password)
                        
                      
                    else:
                        showerror("خطا","خطا در ورود لطفاً نام کاربری و کلمه عبور را بررسی ، و دوباره سعی کنید")

    def checkToken(self,username):
        try:
      
            with open( "string.txt", "rb") as f1, open( "key.txt", "rb") as f2:
                token = f1.read()
                key = f2.read()

            f = Fernet(key)
            what_d = str(f.decrypt(token),'utf-8') 
            r = hashlib.md5(str.encode(username[:10]))
            if what_d != r.hexdigest():
                showerror("دسترسی","نام کاربری مجاز نمیباشد")
                return False
            else:
                return True
        except:
            showerror("دسترسی","نام کاربری مجاز نمیباشد")
            return False

if __name__ == "__main__":
    form = LoginForm()
    basef = form.generateForm()