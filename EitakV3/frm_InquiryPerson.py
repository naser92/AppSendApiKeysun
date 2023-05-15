# import sys
# sys.path.append('..')
import customtkinter as ck
import tkinter
from module.api import ApiKeysun
class FormInquiryPerson():
    def __init__(self,frame:ck.CTkFrame) -> None:
        self.frame = frame
        self.font : tuple = ("Tahoma",14)
        self.font12 : tuple = ("Tahoma",12)

        #input data
        self.frame_data = ck.CTkFrame(self.frame,border_width=2, width=570, height=80)
        self.frame_data.place(x=10,y=10)

        lbl_input = ck.CTkLabel(self.frame_data,text=" :شماره اقتصادی",font=self.font)
        lbl_input.place(x=410,y=25)

        self.txt_economicCode = ck.CTkEntry(self.frame_data,width=200,placeholder_text="Economic Code")
        self.txt_economicCode.place(x=200,y=25)

        self.btn_selectFile = ck.CTkButton(self.frame_data,text="استعلام",font=self.font)
        self.btn_selectFile.place(x=40,y=25)