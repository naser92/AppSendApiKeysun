from tkinter import*  
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo , showwarning,showerror
from tkinter import ttk
from core.api import ApiKeysun
from core.ExcellData import ExcellData
from core.InvoiceData import InvoiceData
from core.csvFile import CSVFile
from model.setting import SettingData
from threading import Thread
import time
from cryptography.fernet import Fernet
import hashlib
from PIL import Image, ImageTk
from datetime import date

api = ApiKeysun() 
setting = SettingData()

class MainPanel():
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password
        self.base = Tk()
        self.status = False
        self.base.geometry('500x500')
        self.base.title("EITAK")
        self.base.iconbitmap("data/logo.ico")
        self.base.eval('tk::PlaceWindow . center')
        self.base.resizable(0,0)

        Label(self.base,bg="#d1ccc0",text="(EITAK  نرم افزار ارسال صورتحساب کیسان (ایتاک" ,width="300",height="4").pack()

        

        self.notebook = ttk.Notebook(self.base,width=500,height=380)
       

        self.frm_sendinvoice = ttk.Frame(self.notebook)
        self.frm_cancellation = ttk.Frame(self.notebook)
        self.frm_inquiry = ttk.Frame(self.notebook)
        

        self.frm_sendinvoice.pack(fill= BOTH, expand=True)
        self.frm_cancellation.pack(fill= BOTH, expand=True)
        self.frm_inquiry.pack(fill= BOTH, expand=True)

        self.notebook.add(self.frm_sendinvoice, text = "        ارسال صورتحساب        ")
        self.notebook.add(self.frm_inquiry, text = "        استعلام صورتحساب        ")
        self.notebook.insert("end",self.frm_cancellation, text = "         ابطال صورتحساب        ")

        self.notebook.tab(2, state="disabled")

        # start ------------frm_sendinvoice------------
      
        #radioButom:
        self.sendinvoice_group_date = ttk.Labelframe(self.frm_sendinvoice, text='انتخاب نوع تاریخ ورودی', width=480, height=80)
        self.sendinvoice_group_date.place(x=10,y=10)
        self.valDate = IntVar()
        self.R1 = ttk.Radiobutton(self.sendinvoice_group_date,variable=self.valDate,value=1)
        self.R1.place(x=200,y=15)
        Label(self.sendinvoice_group_date,text="تاریخ ورودی میلادی").place(x=90,y=5)
        Label(self.sendinvoice_group_date,text="yyyy-mm-dd").place(x=100,y=25)

        self.R2 = ttk.Radiobutton(self.sendinvoice_group_date,variable=self.valDate,value=2)
        self.R2.place(x=380,y=15)
        Label(self.sendinvoice_group_date,text="تاریخ ورودی شمسی").place(x=270,y=5)
        Label(self.sendinvoice_group_date,text="yyyy/mm/dd").place(x=280,y=25)
        #inputfile
        self.sendinvoice_group_file = ttk.Labelframe(self.frm_sendinvoice, text='ورود فایل', width=480, height=90)
        self.sendinvoice_group_file.place(x=10,y=90)
        self.numberPatern = ttk.Combobox(self.sendinvoice_group_file, width=45,state="readonly" ,
                                            value=["انتخاب الگو صورتحساب","الگو 1 صورتحساب همراه با اطلاعات خریدار","الگو 2 صورتحساب بدون اطلاعات خریدار"])
        self.numberPatern.current(0)
        self.numberPatern.place(x=100,y=5)
        
        self.btn_selectFile = ttk.Button(self.sendinvoice_group_file,text="انتخاب فایل",command=self.select_file)
        self.btn_selectFile.place(x=20,y=35)

        self.lbl_path = Label(self.sendinvoice_group_file,bg="#ffffff",width="50",height="1")
        self.lbl_path.place(x=100,y=38)

        #send element
        self.sendinvoice_group_send = ttk.Labelframe(self.frm_sendinvoice, text='ارسال فایل', width=480, height=80)
        self.sendinvoice_group_send.place(x=10,y=180)

        self.btn_sendInvoice = ttk.Button(self.sendinvoice_group_send,text="ارسال صورتحساب",command=self.send_invoice)
        self.btn_sendInvoice.place(x=360,y=5)

        
        self.btn_reset = ttk.Button(self.sendinvoice_group_send,text="کنسل",command=self.reset_form)
        self.btn_reset.place(x=285,y=5)

        self.progressbar = ttk.Progressbar(self.sendinvoice_group_send)
        self.progressbar.place(x=10,y=35,width=450)

        #Result_Lable
        # self.sendinvoice_group_reportLable = ttk.Labelframe(self.frm_sendinvoice, text='آمار ارسال', width=240, height=115)
        # self.sendinvoice_group_reportLable.place(x=250,y=240)

        Label(self.frm_sendinvoice,text="تعداد کل فاکتور ها").place(x=355,y=270)
        self.lbl_number_allFactor  = Label(self.frm_sendinvoice,text="0")  
        self.lbl_number_allFactor.place(x=300,y=270)   

        
        Label(self.frm_sendinvoice,text="تعداد فاکتور ارسالی").place(x=350,y=290)  
        self.lbl_number_sendFactor  = Label(self.frm_sendinvoice,text="0")
        self.lbl_number_sendFactor.place(x=300,y=290)   

        Label(self.frm_sendinvoice,text="فاکتور ثبت شده").place(x=370,y=310)
        self.lbl_number_successFactor  = Label(self.frm_sendinvoice,text="0")
        self.lbl_number_successFactor.place(x=300,y=310) 

        Label(self.frm_sendinvoice,text="فاکتور خطادار").place(x=380,y=330)
        self.lbl_number_ErrorFactor  = Label(self.frm_sendinvoice,text="0")
        self.lbl_number_ErrorFactor.place(x=300,y=330) 


        self.lbl_status = Label(self.frm_sendinvoice,text="فایل در دسترس نیست" ,bg="#ffffff",width='100', height="1")
        self.lbl_status.place(x=0,y=360)

        # end   ------------frm_sendinvoice------------

        # start ------------frm_inquiry------------
        self.inquiry_group_inputType = ttk.Labelframe(self.frm_inquiry, text='ورود فایل', width=480, height=80)
        self.inquiry_group_inputType.place(x=10,y=30)
        self.path_inquiry_file = None
        self.btn_inquiry_selectFile = ttk.Button(self.inquiry_group_inputType,text="انتخاب فایل",command=self.select_file_inquiry)
        self.btn_inquiry_selectFile.place(x=10,y=10)

        self.lbl_inquiry_path = Label(self.inquiry_group_inputType,bg="#ffffff",width="50",height="1")
        self.lbl_inquiry_path.place(x=100,y=13)

        self.lbl_inquiry_mesasge = Label(self.inquiry_group_inputType)
        self.lbl_inquiry_mesasge.place(x=100,y=35)

        # inquiry_lbl1 = Label(self.frm_inquiry,text="وجود دارد را مشخس کنید TaxSerialNumber شماره سونی راکه در آن")
        # inquiry_lbl1.place(x=140,y=120)
        # inquiry_lbl2 = Label(self.frm_inquiry,text="شماره ستون ها از 1 شروع می شود",fg="red")
        # inquiry_lbl2.place(x=300,y=140)

        # self.inquiry_txt_numberColum = ttk.Entry(self.frm_inquiry,width=1,text='5')
        # self.inquiry_txt_numberColum.place(x=140,y=143) 
        
        self.inquiry_group_fielType = ttk.Labelframe(self.frm_inquiry, text='نحوه استعلام صورتحساب', width=480, height=80)
        self.inquiry_group_fielType.place(x=10,y=120)
        self.valTypeinquiry = IntVar()
        self.R11 = ttk.Radiobutton(self.inquiry_group_fielType,text="UniqeId",variable=self.valTypeinquiry,value=2)
        self.R11.place(x=10,y=15)
        

        self.R22 = ttk.Radiobutton(self.inquiry_group_fielType,text="TaxSerialNumber",variable=self.valTypeinquiry,value=4)
        self.R22.place(x=250,y=15)
       
         #send element
        self.inquiry_group_send = ttk.Labelframe(self.frm_inquiry, text='ارسال فایل', width=480, height=80)
        self.inquiry_group_send.place(x=10,y=200)

        self.btn_sendInvoice = ttk.Button(self.inquiry_group_send,text="استعلام",command=self.inquiry_incvoice)
        self.btn_sendInvoice.place(x=375,y=5)

        self.inquiry_progressbar = ttk.Progressbar(self.inquiry_group_send)
        self.inquiry_progressbar.place(x=10,y=35,width=450)
        #Result_Lable
        
        
        Label(self.frm_inquiry,text="تعداد کل فاکتور ها").place(x=350,y=300)
        self.inquiry_lbl_number_allFactor  = Label(self.frm_inquiry,text="0")  
        self.inquiry_lbl_number_allFactor.place(x=300,y=300)   

        
        Label(self.frm_inquiry,text="تعداد فاکتور استعلام شده").place(x=350,y=320)  
        self.inquiry_lbl_number_sendFactor  = Label(self.frm_inquiry,text="0")
        self.inquiry_lbl_number_sendFactor.place(x=300,y=320)   
        # end   ------------frm_inquiry------------
        Label(self.base,text="Version:2.0.0").place(x=10,y=478)
        self.notebook.place(x=0,y=70)

        load = Image.open('data/logo.png')
        render = ImageTk.PhotoImage(load)
        img = Label(self.base, image=render,width=70,height=50)
        img.image = render
        img.place(x=10, y=380)

         
        load2 = Image.open('data/keysunlogo.png')
        render2 = ImageTk.PhotoImage(load2)
        img2 = Label(self.base, image=render2,width=60,height=55,bg="#d1ccc0")
        img2.image = render2
        img2.place(x=400, y=5)

        self.base.mainloop()

    def generateForm(self) -> None:
        self.base.mainloop()  

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
                self.CSV = CSVFile(self.path_file)
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

    def lockElement(self):
        # self.numberPatern.config(state="disabled")
        # self.btn_selectFile.state(["disabled"])
        # self.btn_reset.state(["disabled"])
        # self.btn_sendInvoice.state(["disabled"])
        self.lbl_status.config(text="در حال ارسال لطفا منتظر بمانید ...",bg="#009FBD")
        # self.R1.config(state="disabled")
        # self.R2.config(state="disabled")
        self.notebook.tab(1, state="disabled")
        for child in self.sendinvoice_group_date.winfo_children():
            child.configure(state='disable')
        
        for child in self.sendinvoice_group_file.winfo_children():
            child.configure(state='disable')

    def send_invoice(self):
            self.lbl_number_allFactor.config(text="0")
            self.lbl_number_ErrorFactor.config(text="0")
            self.lbl_number_sendFactor.config(text="0")
            self.lbl_number_successFactor.config(text="0")
            str_usename = self.username
            str_password = self.password
            vdate = self.valDate.get()
            # today = date.today()
            
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

                            # if patern == 1:
                            #     self.Excell.preparationExcellN11()
                            # elif patern == 2:
                            #     self.Excell.preparationExcellN21()

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
                                        import json
                                        json_object = json.dumps(listInvoice)
                                        with open("sample1.json", "w") as outfile:
                                             outfile.write(json_object)
                                        result = api.sendInvoice(listInvoice,token)
                                        # curentTime = time.strftime("%H:%M:%S")
                                        if result[0] == 200:
                                            indexResult = lambda x,xy : [y for y in xy if y['uniqueId'] == x ] 
                                            data = result[1]['data']
                                            for invoiceItem in listIndex:
                                                dataResultPerInvoice = indexResult(invoiceItem[2],data)
                                                for i,d in enumerate(dataResultPerInvoice):
                                                    if  d['status'] == 3:
                                                        self.CSV.saveData([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status'],d['taxSerialNumber']])
                                                        sucessCount += 1
                                                    else:
                                                        self.CSV.saveError([invoiceItem[0],invoiceItem[1],d['uniqueId'],d['status'],d['title'],d['description']])
                                                        if i == 0:
                                                            errorCount += 1
                                        
                                        else:
                                            for invoiceItem in listIndex: 
                                                self.CSV.saveError([invoiceItem[0],invoiceItem[1],invoiceItem[2],result[0],result[1]])
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


    def reset_form(self):
        # self.numberPatern.config(state="readonly")
        # self.numberPatern.current(0)
        self.lbl_status.config(text="فایل در دسترس نیست",bg="#ffffff")
        # self.status = False
        # self.btn_selectFile.state(["!disabled"])
        # self.btn_reset.state(["!disabled"])
        # self.btn_sendInvoice.state(["!disabled"])
        # self.lbl_path.config(text="")
        # self.R1.config(state="normal")
        # self.R2.config(state="normal")
        self.notebook.tab(1, state="normal")
        for child in self.sendinvoice_group_date.winfo_children():
            child.configure(state='normal')
        
        for child in self.sendinvoice_group_file.winfo_children():
            child.configure(state='normal')

    #inquiry_function
    def select_file_inquiry(self):
        self.lbl_inquiry_mesasge.config(text="")
        filetypes = (
            ('csv files', '*.csv'),
            # ('Excel files', '*.xlsx'),
            ('All files', '*.*')
        )
        self.path_inquiry_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_inquiry_path.config(text=self.path_inquiry_file)
        self.CSV = CSVFile(self.path_inquiry_file)
        self.Excell =ExcellData(self.path_inquiry_file)
        filename  = self.path_inquiry_file.split("/")
        filename = filename[-1]
        filename = filename.split(".")
        filename = filename[-1]
        if filename == "csv": # or filename == "xlsx":
            typeFile = "CSV" if filename == "csv" else "excel"
            # showinfo("file","file is select %s"%typeFile)
            self.lbl_inquiry_mesasge.config(text="%s نوع فایل انتخابی"%typeFile)
            

        else:
            showerror("نوع فایل انتخابی","فایل انتخابی باید یکی از فرمت های %s و یا %s باشد"%("csv","xlsx"))
        
    def lock_inquiry_element(self):
        for child in self.inquiry_group_inputType.winfo_children():
            child.configure(state='disable')
        
        for child in self.inquiry_group_fielType.winfo_children():
            child.configure(state='disable')
        
        self.notebook.tab(0, state="disabled")
        self.base.update_idletasks()
        self.base.after(500)
        self.base.update()


    def inquiry_incvoice(self):
        self.inquiry_lbl_number_allFactor.config(text="0")
        self.inquiry_lbl_number_sendFactor.config(text="0")
        valTypeinquiry = self.valTypeinquiry.get()
        # self.inquiry_group_fielType.state["disabled"]
        # self.inquiry_group_inputType.state["disabled"]
       

        if valTypeinquiry == 0 :
            showwarning("نوع روش استفاده","مشخص کنید از چه طریقی اقدانم به استعلام می نمایید ")
        elif self.path_inquiry_file == None:
            showwarning("انتخاب فایل","فایل را انتخاب کنید")
        else:
            self.lock_inquiry_element()
            
            v = valTypeinquiry
            listinquiry = self.CSV.read_file_inquiry(v)
            if listinquiry != None:
                listitem = []
                counter = 0
                self.inquiry_progressbar['value'] = 0
                self.inquiry_progressbar.configure(maximum=len(listinquiry))
                self.inquiry_lbl_number_allFactor.config(text=str(len(listinquiry)))
                for index,item in enumerate(listinquiry):
                    listitem.append(item)
                    counter += 1

                    if counter == setting.BatchSizeOfInvoices or index ==  (len(listinquiry) - 1):
                        token = api.getToken(self.username,self.password)
                        if token != "":
                            if valTypeinquiry == 2 :
                                result = api.inquiryInvoiceByUniqeId(listitem,token)
                            elif valTypeinquiry == 4 :
                                result = api.inquiryInvoiceByTaxserialnumber(listitem,token)
                            
                            if result[0] == 200 and len(result[1]['data']) > 0:
                                data = result[1]['data']
                                for d in data:
                                    if valTypeinquiry == 2 :
                                        self.CSV.saveDatainquiry2([d['uniqueId'],d['trackingId'],d['taxSerialNumber'],d['statusCode'],d['statusTitle']])
                                    elif valTypeinquiry == 4 :
                                        self.CSV.saveDatainquiry4([d['trackingId'],d['taxSerialNumber'],d['statusCode'],d['statusTitle']])

                        else:                    
                            self.CSV.saveError(['loginError'])
                        
                        listitem = []
                        counter = 0
                        self.inquiry_lbl_number_sendFactor.config(text=str(index+1))
                        self.inquiry_progressbar['value'] = index+1
                        self.inquiry_progressbar.update()
                        self.base.update_idletasks()
                        self.base.after(500)
                        self.base.update()
            else:
                showerror("خطا در خواندن فایل")
        
        for child in self.inquiry_group_inputType.winfo_children():
            child.configure(state='normal')
        
        for child in self.inquiry_group_fielType.winfo_children():
            child.configure(state='normal')
        
        self.notebook.tab(0, state="normal")
        self.base.update_idletasks()
        self.base.after(500)
        self.base.update()
        showinfo("اتمام","عملیات با موفقیت انجام شد نتیجه را می توانید در پوشه ای که خود فایل وجود دارد مشاهده نمایید")

if __name__ == "__main__":
    MainPanel("","")