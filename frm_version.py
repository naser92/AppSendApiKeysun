import customtkinter as ck
import webbrowser

class VersionForm():
    def __init__(self,Currentversion,LastVersion,url) -> None:
        self.url = url
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

        lbl_current = ck.CTkLabel(self.group_download,text="   ورژن کنونی برنامه شما  " + self.Currentversion + "  می باشد" ,font=self.font,text_color="#DF0737")
        lbl_current.place(x=50,y=10)

        lbl_current = ck.CTkLabel(self.group_download,text="   ورژن نسخه برنامه  " + self.LastVersion + "  می باشد" ,font=self.font,text_color="#399F2E")
        lbl_current.place(x=60,y=40)

        lbl_current = ck.CTkLabel(self.group_download,text="برای دانلود آخرین ورژن بر روی دکمه زیر کلیک کنید" ,font=self.font)
        lbl_current.place(x=40,y=70)

        
        self.btn_revoke = ck.CTkButton(self.group_download,text="دانلود ورژن جدید",font=self.font,width=50,command=self.download_app)
        self.btn_revoke.place(x=120,y=110)

    def download_app(self):
        url = self.url  
        webbrowser.open(url)
        

       
    

    def generateForm(self) -> None:
        self.base.mainloop()  


if __name__ == "__main__":
    form = VersionForm("3.6.0","3.6.1")
    basef = form.generateForm()