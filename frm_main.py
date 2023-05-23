import customtkinter as ck
from package.CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
from tkinter import font
from frm_sendInvoice import FormSendInvoice
from frm_InquiryInvoice import FormInquiryInvoice
from frm_revokInvoice import FormRevokInvoice
from frm_InquiryPerson import FormInquiryPerson
from frm_deleteInvoice import FormDeleteInvoice
from frm_help import FormHelp
import os

class MainPanel():
    def __init__(self,username,password) -> None:
        self.username = username 
        self.password = password
        self.base = ck.CTk()
        self.status = False
        self.base.geometry('800x600')
        self.base.title("EITAK")
        self.base.iconbitmap("media/image/logo.ico")
        screen_width = self.base.winfo_screenwidth()
        screen_height = self.base.winfo_screenheight()
        x = (screen_width // 2) - (800 // 2)
        y = (screen_height // 2) - (600 // 2)
        self.base.geometry("+{}+{}".format(x, y))
        # self.base.eval('tk::PlaceWindow . center')
        self.base.resizable(0,0)
        # self.font = font.Font(family='IRANYekan', size=12,file='data/IRANYekanBlackFaNum.ttf' ,weight="bold")
        self.font : tuple = ("Tahoma",12)
        # self.base.config(bg="#0003a1")
        # load Image 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "media/image")
        self.sendInvoice_image = ck.CTkImage(light_image=Image.open(os.path.join(image_path, "sendInvice.jpg")),size=(20,20))
        self.inquiryInvoice_image = ck.CTkImage(light_image=Image.open(os.path.join(image_path, "inquiryInvoice.png")),size=(15,20))
        self.revokInvoice_image = ck.CTkImage(light_image=Image.open(os.path.join(image_path, "revokInvoice.png")),size=(20,20))
        self.inquiryPerson_image = ck.CTkImage(light_image=Image.open(os.path.join(image_path, "person.png")),size=(20,20))
        self.help_image = ck.CTkImage(light_image=Image.open(os.path.join(image_path, "help.png")),size=(20,20))

        #create menu frame
        self.menu_frame = ck.CTkFrame(self.base,corner_radius=0,height=600,width=200)
        self.menu_frame.place(x=600,y=0)

        self.btn_send_invoice = ck.CTkButton(self.menu_frame, text="      ارسال صورتحساب", compound="right", font=self.font,
                                             corner_radius=0, height=40, border_spacing=10,fg_color="transparent",width=150,
                                            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w",image=self.sendInvoice_image,command=self.send_button_event)
        self.btn_send_invoice.place(x=20,y=100)

        self.btn_inqiure_invoice = ck.CTkButton(self.menu_frame, text="    استعلام صورتحساب", compound="right", font=self.font,
                                             corner_radius=0, height=40, border_spacing=10,fg_color="transparent",width=150,
                                            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w",image=self.inquiryInvoice_image,command=self.inquiry_button_event)
        self.btn_inqiure_invoice.place(x=20,y=150)

        self.btn_revok_invoice = ck.CTkButton(self.menu_frame, text="       ابطال صورتحساب", compound="right", font=self.font,width=150,
                                              corner_radius=0, height=40, border_spacing=10,fg_color="transparent",
                                            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w",image=self.revokInvoice_image,command=self.revok_button_event)
        self.btn_revok_invoice.place(x=20,y=200)

        
        self.btn_delete_invoice = ck.CTkButton(self.menu_frame, text="  پاک کردن صورتحساب", compound="right", font=self.font,width=150,
                                              corner_radius=0, height=40, border_spacing=10,fg_color="transparent",
                                            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w",image=self.revokInvoice_image,command=self.delete_button_event)
        self.btn_delete_invoice.place(x=20,y=250)

        self.btn_inqiurePerson_invoice = ck.CTkButton(self.menu_frame, text="استعلام مودیان مالیاتی", compound="right", font=self.font,width=150,
                                              corner_radius=0, height=40, border_spacing=10,fg_color="transparent",
                                            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w",image=self.inquiryPerson_image,command=self.inquiryPerson_button_event)
        self.btn_inqiurePerson_invoice.place(x=20,y=300)

        
        self.btn_help = ck.CTkButton(self.menu_frame, text="                     راهنما", compound="right", font=self.font,width=150,
                                              corner_radius=0, height=40, border_spacing=10,fg_color="transparent",
                                            text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w",image=self.help_image,command=self.help_button_event)
        self.btn_help.place(x=20,y=450)



        # label_theme = ck.CTkLabel(self.menu_frame,text="تم",font=self.font)
        # label_theme.place(x=150,y=410)

        self.appearance_mode_menu = ck.CTkOptionMenu(self.menu_frame, values=["System","Light", "Dark"],width=160,
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.place(x=20,y=30)

        load = ck.CTkImage(Image.open('media/image/logo.png'),size=(60,50))
        img = ck.CTkLabel(self.menu_frame, image=load,text="")
        img.place(x=80, y=510)

        label_version = ck.CTkLabel(self.menu_frame,text="Version 6.3.0")
        label_version.place(x=73,y=565)


        #create header
        self.header_frame = ck.CTkFrame(self.base,corner_radius=0,height=80,width=590)
        self.header_frame.place(x=5,y=5)
        label = ck.CTkLabel(self.header_frame,text="(نرم افزار ارسال صورتحساب کیسان (ایتاک" ,width=300,height=50,font=("Tahoma",14))
        label.place(x=240,y=15)

        

        load2 = ck.CTkImage(Image.open('media/image/keysunlogo.png'),size=(60,60))
        img2 = ck.CTkLabel(self.header_frame, image=load2,text="")
        img2.place(x=520, y=10)

        #invoice Frame
        self.invoice_frame = ck.CTkFrame(self.base, corner_radius=0,width=590,height=505)#fg_color="transparent"
        self.invoice_frame.place(x=5,y=90)
        FormSendInvoice(self.invoice_frame,self.username,self.password)

        #invoice Frame 
        self.inquiry_frame = ck.CTkFrame(self.base, corner_radius=0,width=590,height=505)#fg_color="transparent"
        self.inquiry_frame.place(x=5,y=90)
        FormInquiryInvoice(self.inquiry_frame,self.username,self.password)

        #Revok Frame 
        self.revok_frame = ck.CTkFrame(self.base, corner_radius=0,width=590,height=505)#fg_color="transparent"
        self.revok_frame.place(x=5,y=90)
        FormRevokInvoice(self.revok_frame,self.username,self.password)
       
        #inqiuryPerson Frame 
        self.inqiuryPerson_frame = ck.CTkFrame(self.base, corner_radius=0,width=590,height=505)#fg_color="transparent"
        self.inqiuryPerson_frame.place(x=5,y=90)
        FormInquiryPerson(self.inqiuryPerson_frame)

        #delete Frame 
        self.delete_frame = ck.CTkFrame(self.base, corner_radius=0,width=590,height=505)#fg_color="transparent"
        self.delete_frame.place(x=5,y=90)
        FormDeleteInvoice(self.delete_frame,self.username,self.password)

        #help Frame 
        self.help_frame = ck.CTkFrame(self.base, corner_radius=0,width=590,height=505)#fg_color="transparent"
        self.help_frame.place(x=5,y=90)
        FormHelp(self.help_frame)

        self.select_frame_by_name("send")
        self.base.mainloop()

    def change_appearance_mode_event(self, new_appearance_mode):
        ck.set_appearance_mode(new_appearance_mode)

    def select_frame_by_name(self, name):
        self.btn_send_invoice.configure(fg_color=("gray75", "gray25") if name == "send" else "transparent")
        self.btn_inqiure_invoice.configure(fg_color=("gray75", "gray25") if name == "inquiry" else "transparent")
        self.btn_revok_invoice.configure(fg_color=("gray75", "gray25") if name == "revok" else "transparent")
        self.btn_inqiurePerson_invoice.configure(fg_color=("gray75", "gray25") if name == "inquiryPerson" else "transparent")
        self.btn_delete_invoice.configure(fg_color=("gray75", "gray25") if name == "delete" else "transparent")
        self.btn_help.configure(fg_color=("gray75", "gray25") if name == "help" else "transparent")

        # show selected frame
        if name == "send":
            self.invoice_frame.place(x=5,y=90)
        else:  
            self.invoice_frame.place_forget()
       
        if name == "inquiry":
            self.inquiry_frame.place(x=5,y=90)
        else:
            self.inquiry_frame.place_forget()
        
        if name == "revok":
            self.revok_frame.place(x=5,y=90)
        else:
            self.revok_frame.place_forget()
        
        if name == "inquiryPerson":
            self.inqiuryPerson_frame.place(x=5,y=90)
        else:
            self.inqiuryPerson_frame.place_forget()

        if name == "delete":
            self.delete_frame.place(x=5,y=90)
        else:
            self.delete_frame.place_forget()

        if name == "help":
            self.help_frame.place(x=5,y=90)
        else:
            self.help_frame.place_forget()


    def send_button_event(self):
        self.select_frame_by_name("send")

    def inquiry_button_event(self):
        self.select_frame_by_name("inquiry")

    def revok_button_event(self):
        self.select_frame_by_name("revok")

    def inquiryPerson_button_event(self):
         self.select_frame_by_name("inquiryPerson")

    def delete_button_event(self):
        self.select_frame_by_name("delete")
    
    def help_button_event(self):
        self.select_frame_by_name("help")
        

if __name__ == "__main__":
    MainPanel("","")