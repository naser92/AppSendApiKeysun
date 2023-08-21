import customtkinter as ck
from package.CTkMessagebox import CTkMessagebox
from module.api   import ApiKeysun
from cryptography.fernet import Fernet
import hashlib
from model.setting import VersionApp
import configparser
from module.winRegister import WindowsRegistry
from module.connection import CheckInternet


config = configparser.ConfigParser()
class LoginForm():
    def __init__(self) -> None:
        self.api = ApiKeysun()
        self.base = ck.CTk()
        self.base.title("Eitak")
        self.base.geometry("300x200")
        self.base.iconbitmap("media/image/logo.ico")
        self.base.eval('tk::PlaceWindow . center')
        self.base.resizable(0,0)
        self.font: tuple = ("Tahoma",12)
        self.version = VersionApp.version
        self.reg = WindowsRegistry()

        # button = ck.CTkButton(self.base, text="my button")
        # button.grid(row=0, column=0, padx=20, pady=20)
      
        # ck.CTkLabel(self.base,bg="#d1ccc0",text="(EITAK  نرم افزار ارسال صورتحساب کیسان (ایتاک" ,width="300",height="4").pack()
        label = ck.CTkLabel(self.base,text="(نرم افزار ارسال صورتحساب کیسان (ایتاک" ,width=300,height=50,anchor="center",font=("Tahoma",14))
        label.grid(row=0, column=0, padx=0, pady=0)



        ck.CTkLabel(self.base,text="نام کاربری",font=self.font).place(x=220,y=70)
        self.txt_username = ck.CTkEntry(self.base,width=200,placeholder_text="username", corner_radius=10)
        self.txt_username.place(x=10,y=70)

    
        user = self.reg.getUsername()
        if user is not None:
            self.txt_username.insert(0,user)

        ck.CTkLabel(self.base,text="کلمه عبور",font=self.font).place(x=220,y=100)
        self.txt_password = ck.CTkEntry(self.base,width=200,show='*',placeholder_text="Password",corner_radius=10)
        self.txt_password.place(x=10,y=100)

        self.btn_testLogin = ck.CTkButton(self.base,text="ورود",command=self.loginTest,font=("Tahoma",12),corner_radius=100)
        self.btn_testLogin.place(x=70,y=130)
        

    def generateForm(self) -> None:
        self.base.mainloop()  


    def checkFirst_login(self):
        regVersion = self.reg.getVersion()
        if regVersion != self.version:
            self.reg.writeVersion(self.version)
            self.reg.writeFirstLogin(0)


    def loginTest(self):
            str_usename = self.txt_username.get()
            str_password = self.txt_password.get()
            if str_usename == '' or str_password == '':
                CTkMessagebox(title="ورود",message="نام کاربری ویا کلمه عبور را به درستی وارد کنید",icon="cancel")
            else:
                # c = self.checkToken(str_usename)
                token = self.api.getToken(str_usename,str_password)
                if token != "":
                    if self.checkPermissions(token):
                        v = self.api.GetVersion()
                        if v == self.version:
                            self.checkFirst_login()
                            self.base.destroy()
                            isLogin = self.reg.getFirstLogin()
                            if not isLogin or isLogin == 0:
                                self.reg.writeUsername(str_usename)
                                self.reg.writeFirstLogin(1)
                                from frm_versionDescription import DescriptinVersion
                                DescriptinVersion(str_usename,str_password,1)
                            else:
                                self.reg.writeUsername(str_usename)
                                self.reg.writeFirstLogin(1)
                                from frm_main import MainPanel
                                MainPanel(str_usename,str_password)
                        else:
                            self.reg.writeFirstLogin(0)
                            url = self.api.getUrl()
                            self.base.destroy()
                            from frm_version import VersionForm
                            frm = VersionForm(self.version,v,url)
                            frm.generateForm()
                else:
                    inter = CheckInternet()
                    connection = inter.checkServerConnection()
                    if connection:
                        CTkMessagebox(title="خطا",message="خطا در ورود لطفاً نام کاربری و کلمه عبور را بررسی ، و دوباره سعی کنید",icon="warning")
                    else:
                        CTkMessagebox(title="ارتباط",message="ارتباط با سرور قطع میباشد لطفاً ارتباط به اینترنت را بررسی نمایید",icon="warning")


    def checkPermissions(self,token) -> bool:
        info = self.api.checkPakage(token)
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





    def checkToken(self,username):
        try:
      
            with open( "string.txt", "rb") as f1, open( "key.txt", "rb") as f2:
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


if __name__ == "__main__":
    form = LoginForm()
    basef = form.generateForm()