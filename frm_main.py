from tkinter import*  
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo , showwarning
from tkinter import ttk
from core.api import ApiKeysun
from core.ExcellData import ExcellData
from core.InvoiceData import InvoiceData
from model.setting import SettingData
base = Tk() 
api = ApiKeysun() 
setting = SettingData()
class MainForm:
    def __init__(self):
        self.base = base
        self.status = False
        self.base.geometry('500x500')  
        self.base.title("Api keysun")
        Label(self.base,bg="#d1ccc0",text="نرم افزار ارسال صورتحساب کیسان" ,width="500",height="4").pack()
        
        Label(self.base,text="نام کاربری").place(x=400,y=100)
        self.txt_username = Text(self.base,width="30",height="1")
        self.txt_username.place(x=100,y=100) 

        Label(self.base,text="کلمه عبور").place(x=400,y=130)
        self.txt_password = Text(self.base,width="30",height="1")
        self.txt_password.place(x=100,y=130)

        Button(self.base,text="تست لاگین",command=self.loginTest).place(x=200,y=165)

        self.numberPatern = ttk.Combobox(self.base, width=40, value=["انتخاب الگو صورتحساب","الگو 1 صورتحساب همراه با اطلاعات خریدار","الگو 2 صورتحساب بدون اطلاعات خریدار"])
        self.numberPatern.current(0)
        self.numberPatern.place(x=100,y=210)
        
        
        
        Button(self.base,text="انتخاب فایل",command=self.select_file).place(x=20,y=240)

        self.lbl_path = Label(self.base,bg="#ffffff",width="50",height="1")
        self.lbl_path.place(x=100,y=243)

        self.lbl_status = Label(self.base,text="فایل در دسترس نیست" ,bg="#ffffff",width='500', height="2")
        self.lbl_status.place(x=0,y=450)
       

        Button(self.base,text="ارسال اطلاعات",command=self.send_invoice).place(x=210,y=300)

    def generateForm(self) -> None:
        self.base.mainloop()  
 
    def loginTest(self):
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
        patern = self.numberPatern.current()
        if patern != 0:
            self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
            self.lbl_path.config(text=self.path_file)
            self.Excell = ExcellData(self.path_file)
            result = self.Excell.checkExcel(patern)
         
            if result == None:
                showwarning("خطا","فایل انتخابی مشکل دارد لطفا دوباره انتخاب کنید")
            else:
                messageItem = ["صورتحساب","اقلام صورتحساب","پرداخت‌های صورتحساب"]
                self.status = True
                for i,r in enumerate(result):
                    if r == 0:  
                        showwarning("خطا", " تعداد ستون های" + messageItem[i] + " " + "در الگوی انتخابی مقایرت دارد")
                        self.status = False
                        self.lbl_status.config(text="فایل خطا دار",bg="#a3001b")


                if self.status : 
                    self.lbl_status.config(text="دیتا آماده ارسال",bg="#08a300")
                    self.numberPatern.config(state='disabled')
                
        else:
            showwarning('انتخاب الگو',"نوع الگوی فاکتور را انتخاب کنید")


    def send_invoice(self):
        if self.status :
            invoices = self.Excell.getInvoice()
            items = self.Excell.getInvoiceItem()
            payments = self.Excell.getPayment()
            if len(invoices) <= 0:
                showwarning("دیتا","تعداد صورتحساب ها صفر می باشد")
            elif len(items) <= 0:
                showwarning("دیتا","تعداد آیتم صورتحساب ها صفر می باشد")
            else:
                inD = InvoiceData(items,payments)
                listInvoice = []
                counter = 0
                patern = self.numberPatern.current()
                for index, invoice in enumerate(invoices):
                    if patern == 1:
                        i = inD.generateInvoiceNo1(invoice)
                        listInvoice.append(i)
                        counter += 1
                
                
                if counter == setting.BatchSizeOfInvoices or  index ==  len(invoices) :
                    counter = 0
                 

        else:
            showwarning("بارگزاری اکسل","لطفاً فایل را به درستی در قالب مناسب بارگزاری نمایید.")

if __name__ == "__main__":
    form = MainForm()
    basef = form.generateForm()

    
        