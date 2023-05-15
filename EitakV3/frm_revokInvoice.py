import customtkinter as ck
import tkinter

class FormRevokInvoice():
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

        #radioButom:
        self.group_date = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_date.place(x=10,y=100)

        self.valDate = tkinter.IntVar()
        
        self.R2 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=2)
        self.R2.place(x=200,y=25)
        ck.CTkLabel(self.group_date,text="تاریخ ورودی شمسی",font=self.font).place(x=70,y=18)
        ck.CTkLabel(self.group_date,text="yyyy/mm/dd").place(x=105,y=45)

        self.R1 = ck.CTkRadioButton(self.group_date,text="",variable=self.valDate,value=1)
        self.R1.place(x=410,y=25)
        ck.CTkLabel(self.group_date,text="تاریخ ورودی میلادی",font=self.font).place(x=290,y=18)
        ck.CTkLabel(self.group_date,text="yyyy-mm-dd").place(x=315,y=45)

        lbl_selectTypeDate = ck.CTkLabel(self.group_date,text=" :انتخاب نوع تاریخ",font=self.font)
        lbl_selectTypeDate.place(x=450,y=20)

        #send element
        self.group_send = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.group_send.place(x=10,y=220)

        self.btn_sendInvoice = ck.CTkButton(self.group_send,text="ابطال صورتحساب",font=self.font)
        self.btn_sendInvoice.place(x=360,y=10)
        
        self.progressbar = ck.CTkProgressBar(self.group_send,orientation="horizontal",width=500,border_width=2)
        self.progressbar.place(x=35,y=50)
        self.progressbar.set(0)


        #Result
        ck.CTkLabel(self.frame,text="تعداد کل فاکتور ها",font=self.font12).place(x=405,y=320)
        self.lbl_number_allFactor  =  ck.CTkLabel(self.frame,text="0")  
        self.lbl_number_allFactor.place(x=350,y=320)   
        
        ck.CTkLabel(self.frame,text="تعداد فاکتور ارسالی",font=self.font12).place(x=400,y=350)  
        self.lbl_number_sendFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_sendFactor.place(x=350,y=350)   

        ck.CTkLabel(self.frame,text="فاکتور ثبت شده",font=self.font12).place(x=420,y=380)
        self.lbl_number_successFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_successFactor.place(x=350,y=380) 

        ck.CTkLabel(self.frame,text="فاکتور خطادار",font=self.font12).place(x=430,y=410)
        self.lbl_number_ErrorFactor  =  ck.CTkLabel(self.frame,text="0")
        self.lbl_number_ErrorFactor.place(x=350,y=410) 



