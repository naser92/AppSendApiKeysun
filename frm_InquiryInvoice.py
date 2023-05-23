import customtkinter as ck
import tkinter
from tkinter import filedialog as fd
from module.ExcellData import ExcellData
from module.InvoiceData import InvoiceData
from module.csvFile import CSVFile
from package.CTkMessagebox import CTkMessagebox
from tkinter import ttk
from model.setting import SettingData
from module.api import ApiKeysun

api = ApiKeysun() 
setting = SettingData()
class FormInquiryInvoice():
    def __init__(self,frame:ck.CTkFrame,username,password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.username = username
        self.password = password
        #input data
        self.frame_data = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_data.place(x=10,y=10)

        lbl_input = ck.CTkLabel(self.frame_data,text=" :ورود فایل",font=self.font)
        lbl_input.place(x=480,y=25)

        self.lbl_path = ck.CTkLabel(self.frame_data,bg_color="#ffffff",width=275,height=20,text="",text_color="#000000")
        self.lbl_path.place(x=180,y=30)

        self.btn_selectFile = ck.CTkButton(self.frame_data,text="انتخاب فایل",font=self.font,command=self.select_file)
        self.btn_selectFile.place(x=20,y=25)

        #select Inquiry Type
        self.frame_TypeInquire = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_TypeInquire.place(x=10,y=100)

        lbl_selectTypeDate = ck.CTkLabel(self.frame_TypeInquire,text=" :انتخاب روش استعلام",font=self.font)
        lbl_selectTypeDate.place(x=420,y=25)

        self.valTypeinquiry = tkinter.IntVar()
        self.R1 = ck.CTkRadioButton(self.frame_TypeInquire,text="UniqeId",variable=self.valTypeinquiry,value=2)
        self.R1.place(x=100,y=25)

        self.R2 = ck.CTkRadioButton(self.frame_TypeInquire,text="TaxSerialNumber",variable=self.valTypeinquiry,value=4)
        self.R2.place(x=250,y=25)

        #send Element
        self.frame_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_send.place(x=10,y=190)

        self.btn_sendInvoice = ck.CTkButton(self.frame_send,text="استعلام",font=self.font,command=self.inquiry_incvoice)
        self.btn_sendInvoice.place(x=400,y=10)
        

        self.progressbar = ttk.Progressbar(self.frame_send)
        self.progressbar.place(x=20,y=50,width=520)
      


        #result lable
        ck.CTkLabel(self.frame,text="تعداد کل فاکتور ها",font=self.font12).place(x=450,y=320)
        self.lbl_number_allFactor  =  ck.CTkLabel(self.frame,text="0")  
        self.lbl_number_allFactor.place(x=350,y=320)   
        
        ck.CTkLabel(self.frame,text="فاکتور های استعلام شده",font=self.font12).place(x=410,y=350)  
        self.lbl_number_sendFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_sendFactor.place(x=350,y=350)  

    def select_file(self):
        # self.lbl_inquiry_mesasge.config(text="")
        filetypes = (
            ('csv files', '*.csv'),
            # ('Excel files', '*.xlsx'),
            # ('All files', '*.*')
        )
        self.path_file = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
        self.lbl_path.configure(text=self.path_file)
        self.CSV = CSVFile(self.path_file)
        self.Excell =ExcellData(self.path_file)
    
    def lock_element(self):
        for child in self.frame_TypeInquire.winfo_children():
            child.configure(state='disable')
        
        for child in self.frame_data.winfo_children():
            child.configure(state='disable')

        self.btn_selectFile.configure(state="disabled")
        
        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()

    def inquiry_incvoice(self):
        valTypeinquiry = self.valTypeinquiry.get()
        if valTypeinquiry == 0 :
            CTkMessagebox(title="نوع روش استفاده",message="مشخص کنید از چه طریقی اقدانم به استعلام می نمایید ")
        elif self.path_file == None:
            CTkMessagebox(title="انتخاب فایل",message="فایل را انتخاب کنید",icon="cancel")
        else:
            self.lock_element()
            listinquiry = self.CSV.read_file_inquiry(valTypeinquiry)
            if listinquiry != None:
                listitem = []
                counter = 0
                self.progressbar['value'] = 0
                self.progressbar.configure(maximum=len(listinquiry))
                self.lbl_number_allFactor.configure(text=str(len(listinquiry)))
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
                                    self.CSV.saveDatainquiry2([d['uniqueId'],d['trackingId'],d['taxSerialNumber'],d['statusCode'],d['statusTitle']])
                                    # if valTypeinquiry == 2 :
                                    #     self.CSV.saveDatainquiry2([d['uniqueId'],d['trackingId'],d['taxSerialNumber'],d['statusCode'],d['statusTitle']])
                                    # elif valTypeinquiry == 4 :
                                    #     self.CSV.saveDatainquiry4([d['trackingId'],d['taxSerialNumber'],d['statusCode'],d['statusTitle']])
                        else:                    
                            self.CSV.saveError(['loginError'])
                        
                        listitem = []
                        counter = 0
                        self.lbl_number_sendFactor.configure(text=str(index+1))
                        self.progressbar['value'] = index+1
                        self.progressbar.update()
                        self.frame.update_idletasks()
                        self.frame.after(500)
                        self.frame.update()
            else:
                CTkMessagebox(title="فایل",message="خطا در خواندن فایل",icon="cancel")
        
        for child in self.frame_TypeInquire.winfo_children():
            child.configure(state='normal')
        
        for child in self.frame_data.winfo_children():
            child.configure(state='normal')

        self.btn_selectFile.configure(state="normal")
        

        self.frame.update_idletasks()
        self.frame.after(500)
        self.frame.update()
        CTkMessagebox(title="اتمام",message="عملیات با موفقیت انجام شد نتیجه را می توانید در پوشه ای که خود فایل وجود دارد مشاهده نمایید",icon="check")