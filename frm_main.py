from tkinter import*  
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo , showwarning
from tkinter import ttk
from core.api import ApiKeysun
base = Tk() 
api = ApiKeysun() 

class MainForm:
    def __init__(self):
        self.base = base
        self.base.geometry('500x500')  
        self.base.title("Api keysun")
        Label(self.base,bg="#d1ccc0",text="نرم افزار ارسال صورتحساب کیسان" ,width="500",height="4").pack()
        
        Label(self.base,text="نام کاربری").place(x=400,y=100)
        self.txt_username = Text(self.base,width="15",height="1")
        self.txt_username.place(x=250,y=100) 

        Label(self.base,text="کلمه عبور").place(x=400,y=130)
        self.txt_password = Text(self.base,width="15",height="1")
        self.txt_password.place(x=250,y=130)

        Button(self.base,text="تست لاگین",command=self.login).place(x=310,y=170)
        
        
        Frame(self.base)
        Button(self.base,text="انتخاب فایل",command=self.select_file).place(x=20,y=210)

        self.lbl_path = Label(self.base,bg="#ffffff",width="50",height="1")
        self.lbl_path.place(x=100,y=213)


        

    def generateForm(self) -> None:
        self.base.mainloop()  
 
    def login(self):
        str_usename = self.txt_username.get("1.0", "end-1c")
        str_password = self.txt_password.get("1.0", "end-1c")
        token = api.getToken(str_usename,str_password)
        if token != "":
            showinfo("موفقیت","ورود با موفقیت انجام شد")
        else:
            showwarning("خطا","خطا در ورود لطفاً نام کاربری و کلمه عبور را بررسی ، و دوباره سعی کنید")


    def select_file(self):
        filetypes = (
            ('Excel files', '*.xlsx'),
            ('All files', '*.*')
        )

        self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_path.config(text=self.path_file)



if __name__ == "__main__":
    form = MainForm()
    basef = form.generateForm()

    
        