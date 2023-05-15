import customtkinter as ck
import tkinter

class FormInquiryInvoice():
    def __init__(self,frame:ck.CTkFrame) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        #input data
        self.frame_data = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_data.place(x=10,y=10)

        lbl_input = ck.CTkLabel(self.frame_data,text=" :ورود فایل",font=self.font)
        lbl_input.place(x=480,y=25)

        self.lbl_path = ck.CTkLabel(self.frame_data,bg_color="#ffffff",width=275,height=20,text="")
        self.lbl_path.place(x=180,y=30)

        self.btn_selectFile = ck.CTkButton(self.frame_data,text="انتخاب فایل",font=self.font)
        self.btn_selectFile.place(x=20,y=25)

        #select Inquiry Type
        self.frame_TypeInquire = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_TypeInquire.place(x=10,y=100)

        lbl_selectTypeDate = ck.CTkLabel(self.frame_TypeInquire,text=" :انتخاب روش استعلام",font=self.font)
        lbl_selectTypeDate.place(x=420,y=25)

        self.valTypeinquiry = tkinter.IntVar()
        self.R1 = ck.CTkRadioButton(self.frame_TypeInquire,text="UniqeId",variable=self.valTypeinquiry,value=1)
        self.R1.place(x=100,y=25)

        self.R2 = ck.CTkRadioButton(self.frame_TypeInquire,text="TaxSerialNumber",variable=self.valTypeinquiry,value=2)
        self.R2.place(x=250,y=25)

        #send Element
        self.frame_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_send.place(x=10,y=190)

        self.btn_sendInvoice = ck.CTkButton(self.frame_send,text="استعلام",font=self.font)
        self.btn_sendInvoice.place(x=360,y=10)
        

        self.progressbar = ck.CTkProgressBar(self.frame_send,orientation="horizontal",width=500,border_width=2)
        self.progressbar.place(x=35,y=50)
        self.progressbar.set(0)


        #result lable
        ck.CTkLabel(self.frame,text="تعداد کل فاکتور ها",font=self.font12).place(x=440,y=320)
        self.lbl_number_allFactor  =  ck.CTkLabel(self.frame,text="0")  
        self.lbl_number_allFactor.place(x=350,y=320)   
        
        ck.CTkLabel(self.frame,text="فاکتور های استعلام شده",font=self.font12).place(x=400,y=350)  
        self.lbl_number_sendFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_sendFactor.place(x=350,y=350)   