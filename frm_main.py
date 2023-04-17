from tkinter import*  
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo , showwarning,showerror
from tkinter import ttk
from core.api import ApiKeysun
from core.ExcellData import ExcellData
from core.InvoiceData import InvoiceData
from model.setting import SettingData
from threading import Thread
import time
from cryptography.fernet import Fernet
import hashlib

base = Tk() 
api = ApiKeysun() 
setting = SettingData()
class MainForm:
    def __init__(self):
        self.base = base
        self.status = False
        self.base.geometry('500x500')  
        self.base.title("Api keysun")
        self.base.iconbitmap("data/logo.ico")
        self.base.eval('tk::PlaceWindow . center')
        self.base.resizable(0,0)
        Label(self.base,bg="#d1ccc0",text="نرم افزار ارسال صورتحساب کیسان" ,width="500",height="4").pack()
        
        #start-------------fromLogin
        # self.frm_login = Frame(self.base)
        # self.frm_login.pack()
        Label(self.base,text="نام کاربری").place(x=350,y=70)
        # self.txt_username = Text(self.base,width="30",height="1")
        self.txt_username = ttk.Entry(self.base,width=40)
        self.txt_username.place(x=100,y=70) 

        Label(self.base,text="کلمه عبور").place(x=350,y=100)
        # self.txt_password = ttk.Entry(self.base,width="30",height="1",show='*')
        self.txt_password = ttk.Entry(self.base,width=40,show='*')
        self.txt_password.place(x=100,y=100)

        self.btn_testLogin = ttk.Button(self.base,text="لاگین",command=self.loginTest)
        self.btn_testLogin.place(x=250,y=130)

        self.btn_reset = ttk.Button(self.base,text="کنسل",command=self.reset_form)
        self.btn_reset.place(x=110,y=130)
        #End-------------fromLogin
        
        self.numberPatern = ttk.Combobox(self.base, width=45,state="readonly" ,value=["انتخاب الگو صورتحساب","الگو 1 صورتحساب همراه با اطلاعات خریدار","الگو 2 صورتحساب بدون اطلاعات خریدار"])
        self.numberPatern.current(0)
        self.numberPatern.place(x=100,y=230)
        
        self.btn_selectFile = ttk.Button(self.base,text="انتخاب فایل",command=self.select_file)
        self.btn_selectFile.place(x=20,y=260)

        self.lbl_path = Label(self.base,bg="#ffffff",width="50",height="1")
        self.lbl_path.place(x=100,y=263)

        #start------------radioButom
        self.valDate = IntVar()
        self.R1 = ttk.Radiobutton(self.base,text="تاریخ ورودی میلادی",variable=self.valDate,value=1)
        self.R1.place(x=300,y=170)
        Label(self.base,text="yyyy-mm-dd").place(x=320,y=190)

        self.R2 = ttk.Radiobutton(self.base,text="تاریخ ورودی شمسی",variable=self.valDate,value=2)
        self.R2.place(x=120,y=170)
        Label(self.base,text="yyyy/mm/dd").place(x=140,y=190)
        #end------------radioButom

        self.btn_sendInvoice = ttk.Button(self.base,text="ارسال اطلاعات",command=self.send_invoice)
        self.btn_sendInvoice.place(x=360,y=300)

        self.progressbar = ttk.Progressbar()
        self.progressbar.place(x=50,y=330,width=400)

        
        #start--------------Result_Lable
        Label(self.base,text="تعداد کل فاکتور ها").place(x=350,y=360)
        self.lbl_number_allFactor  = Label(self.base,text="0")  
        self.lbl_number_allFactor.place(x=300,y=360)   

        
        Label(self.base,text="تعداد فاکتور ارسالی").place(x=350,y=380)  
        self.lbl_number_sendFactor  = Label(self.base,text="0")
        self.lbl_number_sendFactor.place(x=300,y=380)   

        Label(self.base,text="فاکتور ثبت شده").place(x=350,y=400)
        self.lbl_number_successFactor  = Label(self.base,text="0")
        self.lbl_number_successFactor.place(x=300,y=400) 

        Label(self.base,text="فاکتور خطادار").place(x=350,y=420)
        self.lbl_number_ErrorFactor  = Label(self.base,text="0")
        self.lbl_number_ErrorFactor.place(x=300,y=420) 
        
        #end--------------Result_Lable

        
        self.lbl_status = Label(self.base,text="فایل در دسترس نیست" ,bg="#ffffff",width='100', height="2")
        self.lbl_status.place(x=0,y=464)


       

    def btn_SendInvoice_click(self):
        self.Tread = Thread(target=self.send_invoice)
        self.Tread.start()

    def generateForm(self) -> None:
        self.base.mainloop()  
 
    def checkToken(self,username):
        try:
            with open("string.txt", "rb") as f1, open("key.txt", "rb") as f2:
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
    
    def loginTest(self):
        # str_usename = self.txt_username.get("1.0", "end-1c")
        # str_password = self.txt_password.get("1.0", "end-1c")
        str_usename = self.txt_username.get()
        str_password = self.txt_password.get()
        if str_usename == '' or str_password == '':
            showwarning("ورود","نام کاربری ویا کلمه عبور را به درستی وارد کنید")
        else:
            c = self.checkToken(str_usename)
            if c:
                token = api.getToken(str_usename,str_password)
                if token != "":
                    showinfo("موفقیت","ورود با موفقیت انجام شد")
                    self.txt_username.config(state="disabled")
                    self.txt_password.config(state="disabled")
                    self.btn_testLogin.state(["disabled"]) 
                else:
                    showerror("خطا","خطا در ورود لطفاً نام کاربری و کلمه عبور را بررسی ، و دوباره سعی کنید")

    def lockElement(self):
        self.txt_username.config(state="disabled")
        self.txt_password.config(state="disabled")
        self.numberPatern.config(state="disabled")
        self.btn_testLogin.state(["disabled"])
        self.btn_selectFile.state(["disabled"])
        self.btn_reset.state(["disabled"])
        self.btn_sendInvoice.state(["disabled"])
        self.lbl_status.config(text="در حال ارسال لطفا منتظر بمانید ...",bg="#009FBD")
        self.R1.config(state="disabled")
        self.R2.config(state="disabled")
        

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

    def reset_form(self):
        self.txt_username.config(state="normal")
        self.txt_password.config(state="normal")
        self.numberPatern.config(state="readonly")
        self.numberPatern.current(0)
        self.lbl_status.config(text="فایل در دسترس نیست",bg="#ffffff")
        self.status = False
        self.btn_testLogin.state(["!disabled"])
        self.btn_selectFile.state(["!disabled"])
        self.btn_reset.state(["!disabled"])
        self.btn_sendInvoice.state(["!disabled"])
        self.lbl_path.config(text="")
        self.R1.config(state="normal")
        self.R2.config(state="normal")


    def send_invoice(self):
        self.lbl_number_allFactor.config(text="0")
        self.lbl_number_ErrorFactor.config(text="0")
        self.lbl_number_sendFactor.config(text="0")
        self.lbl_number_successFactor.config(text="0")
        str_usename = self.txt_username.get()
        str_password = self.txt_password.get()
        vdate = self.valDate.get()
        if str_usename == '' or str_password == '':
            showwarning("ورود","نام کاربری ویا کلمه عبور را به درستی وارد کنید")
        elif vdate == 0 :
            showwarning("نوع تاریخ","نوع ورودی تاریخ را مشخص نمایید")
        else:
            c = self.checkToken(str_usename)
            if c:
                self.lockElement()
                if self.status :
                    invoices = self.Excell.getInvoice()
                    items = self.Excell.getInvoiceItem()
                    payments = self.Excell.getPayment()
                    

                    
                    self.progressbar.configure(maximum=len(invoices))
                    sucessCount = 0
                    errorCount = 0
                    
                    
                    if len(invoices) <= 0:
                        showwarning("دیتا","تعداد صورتحساب ها صفر می باشد")
                    elif len(items) <= 0:
                        showwarning("دیتا","تعداد آیتم صورتحساب ها صفر می باشد")
                    else:
                        inD = InvoiceData(items,payments)
                        listInvoice = []
                        listIndex = []
                        counter = 0
                        patern = self.numberPatern.current()

                        if patern == 1:
                            self.Excell.preparationExcellN11()
                        elif patern == 2:
                            self.Excell.preparationExcellN21()

                        self.lbl_number_allFactor.config(text=str(len(invoices)))
                        
                        for index, invoice in enumerate(invoices):
                        
                        
                            if patern == 1:
                                i = inD.generateInvoiceNo1(invoice,vdate)
                                listInvoice.append(i)
                            elif patern == 2:
                                i = inD.generateInvoiceNo2(invoice,vdate)
                                listInvoice.append(i)

                            listIndex.append([index + 1 ,invoice[0],i['uniqueId']])
                            counter += 1
                            
                            if counter == setting.BatchSizeOfInvoices or  index ==  (len(invoices) - 1) :
                                # print (listIndex)
                                token = api.getToken(str_usename,str_password)
                                if token != "":
                                    result = api.sendInvoice(listInvoice,token)
                                    if result[0] == 200:
                                        data = result[1]
                                        listUniqeId = []
                                        for invoiceItem in listIndex:
                                            
                                            for d in data['data']:
                                                if invoiceItem[2] == d['uniqueId']:
                                                    if  d['status'] == 3:
                                                        if patern == 1:
                                                            self.Excell.SaveResultN11([d['uniqueId'],d['status'],d['taxSerialNumber'],"",""],invoiceItem[0])
                                                        elif patern ==2:
                                                            self.Excell.SaveResultN21([d['uniqueId'],d['status'],d['taxSerialNumber'],"",""],invoiceItem[0])
                                                        sucessCount += 1
                                                    else:
                                                        if patern == 1:
                                                            self.Excell.SaveResultN11([d['uniqueId'],d['status'],"",d['description'],d['title']],invoiceItem[0])
                                                        elif patern ==2:
                                                            self.Excell.SaveResultN21([d['uniqueId'],d['status'],"",d['description'],d['title']],invoiceItem[0])
                                                        try:
                                                            listUniqeId.index(d['uniqueId'])
                                                        except ValueError:
                                                            errorCount += 1
                                                        listUniqeId.append(invoiceItem[2])
                                                elif d == "Erorrserver":
                                                    if patern == 1:
                                                        self.Excell.SaveResultN11([d['uniqueId'],d['status'],"",d['description'],d['title']],invoiceItem[0])
                                                    elif patern ==2:
                                                        self.Excell.SaveResultN21([d['uniqueId'],d['status'],"",d['description'],d['title']],invoiceItem[0])
                                                    errorCount += 1
                                    
                                    else:
                                        if patern == 1:
                                            self.Excell.SaveResultN11([listInvoice[1],d['status'],"systemError","server"],invoiceItem[0])
                                        elif patern ==2:
                                            self.Excell.SaveResultN11([listInvoice[1],d['status'],"systemError","server"],invoiceItem[0])
                                        errorCount += 1
                                
                                
                                else:                    
                                    print("login Faild")
                                counter = 0
                                listInvoice = []
                                listIndex = []
                                self.lbl_number_sendFactor.config(text=str(index+1))
                                self.base.update_idletasks()
                                self.base.after(500)
                                self.base.update()
                                
                            
                            self.lbl_number_ErrorFactor.config(text=str(errorCount))
                            self.lbl_number_successFactor.config(text=str(sucessCount))
                            self.progressbar['value'] = index+1
                            self.progressbar.update()
                            self.base.update_idletasks()
                            self.base.after(500)
                            self.base.update()
                            


                        showinfo("اتمام","تعداد %d فاکتور با موفقیت ارسال گردید میتوانید نتیجه را در اکسل انتخابی مشاهده نمایید"%len(invoices))
                else:
                    showerror("بارگزاری اکسل","لطفاً فایل را به درستی در قالب مناسب بارگزاری نمایید.")

                self.reset_form()
if __name__ == "__main__":
    form = MainForm()
    basef = form.generateForm()

    
        