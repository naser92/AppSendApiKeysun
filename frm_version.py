import customtkinter as ck
import webbrowser
from module.api import ApiKeysun
from package.CTkMessagebox import CTkMessagebox
import subprocess
import os
class VersionForm():
    def __init__(self,Currentversion,LastVersion,url) -> None:
        self.url = url
        self.api = ApiKeysun()
        self.Currentversion = Currentversion
        self.LastVersion = LastVersion
        self.base = ck.CTk()
        self.base.title("Eitak")
        self.base.geometry("350x220")
        self.base.iconbitmap("media/image/logo.ico")
        self.base.eval('tk::PlaceWindow . center')
        self.base.resizable(0,0)
        self.font: tuple = ("Tahoma",12)

        self.group_date = ck.CTkFrame(self.base,border_width=2, width=330, height=50,fg_color="#FFCD02")
        self.group_date.place(x=10,y=10)
      
        
        lbl_war = ck.CTkLabel(self.group_date,text="نرم افزار جدید ایتاک ",font=self.font,text_color="#0066FF")
        lbl_war.place(x=120,y=10)

        self.group_download = ck.CTkFrame(self.base,border_width=2, width=330, height=150)
        self.group_download.place(x=10,y=63)

        lbl_current = ck.CTkLabel(self.group_download,text="   نسخه کنونی برنامه شما  " + self.Currentversion + "  می باشد" ,font=self.font,text_color="#DF0737")
        lbl_current.place(x=50,y=10)

        lbl_current = ck.CTkLabel(self.group_download,text="   نسخه فعال برنامه  " + self.LastVersion + "  می باشد" ,font=self.font,text_color="#399F2E")
        lbl_current.place(x=60,y=40)

        lbl_current = ck.CTkLabel(self.group_download,text="برای دانلود آخرین نسخه بر روی دکمه زیر کلیک کنید" ,font=self.font)
        lbl_current.place(x=40,y=70)

        
        self.btn_revoke = ck.CTkButton(self.group_download,text="دانلود نسخه جدید",font=self.font,width=50,command=self.download_app)
        self.btn_revoke.place(x=220,y=110)

        self.auto_update = ck.CTkButton(self.group_download,text="بروز رسانی خودکار",font=self.font,width=50,command=self.update)
        self.auto_update.place(x=112,y=110)

        self.btn_help = ck.CTkButton(self.group_download,text="دانلود راهنما ایتاک",font=self.font,width=50,command=self.download_help)
        self.btn_help.place(x=5,y=110)

    def download_app(self):
        url = self.url  
        webbrowser.open(url)

    def download_help(self):
        url = self.api.GetURL_Help()
        if url == "0":
            CTkMessagebox(title="خطای شبکه", message="لطفاً ارتباط خود با اینترنت را بررسی کنید",icon="cancel")
        elif url == "O":
            CTkMessagebox(title="خطای سرور", message="ممکن است در سرور خطایی رخ داده شده باشد لطفاً دوباره امتحان کنید",icon="cancel")
        else:
            webbrowser.open(url)

    def generateForm(self) -> None:
        self.base.mainloop()  

    def update(self):
        try: 
            curent_path = os.getcwd()
            app_name = "update.exe"
            path_file = os.path.join(curent_path,app_name)
            subprocess.run(path_file, check=True)
            self.base.destroy()
        except subprocess.CalledProcessError as e:
            CTkMessagebox(title="خطا", message=f"Error running update : {e}",icon="cancel")
        except FileNotFoundError:
            CTkMessagebox(title="خطا", message="برنامه بروز رسانی پیدا نشد",icon="cancel")






if __name__ == "__main__":
    form = VersionForm("3.6.2","3.6.3","ldsa")
    basef = form.generateForm()