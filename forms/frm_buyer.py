import os
import sys
sys.path.append(os.getcwd())
import customtkinter as ck
import tkinter


class FormBuyer():
    def __init__(self,frame:ck.CTkFrame,username, password) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)
        self.status = False
        self.username = username
        self.passwoerd = password

        #input data
        self.frame_data = ck.CTkFrame(self.frame,border_width=2, width=670, height=80)
        self.frame_data.place(x=10,y=10)

        lbl_input = ck.CTkLabel(self.frame_data,text=" :ورود فایل",font=self.font)
        lbl_input.place(x=480,y=25)

        self.lbl_path = ck.CTkLabel(self.frame_data,bg_color="#ffffff",width=275,height=20,text="",text_color="#000000")
        self.lbl_path.place(x=180,y=30)

        self.btn_selectFile = ck.CTkButton(self.frame_data,text="انتخاب فایل",font=self.font)#,command=self.select_file
        self.btn_selectFile.place(x=20,y=25)