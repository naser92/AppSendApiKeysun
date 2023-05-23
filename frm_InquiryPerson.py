# import sys
# sys.path.append('..')
import customtkinter as ck
import tkinter as tk
from module.api import APIEconomicCode
import json

api = APIEconomicCode()
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

        self.btn_selectFile = ck.CTkButton(self.frame_data,text="استعلام",font=self.font,command=self.InquiryPerson)
        self.btn_selectFile.place(x=40,y=25)

        self.textbox = ck.CTkTextbox(self.frame, width=570,height=300, corner_radius=0,font=self.font)
        self.textbox.place(x=10,y=100)
        


    def InquiryPerson(self):
        self.textbox.delete("1.0","end")
        e = self.txt_economicCode.get()
        # if len(r) > 0 :
        #      self.textbox.delete(tk.SEL_FIRST) result['data']
        result = api.InquiryPerson(e)
        if "data" in result:
            # result = result['data']
            self.textbox.insert(index="1.0",text=json.dumps(result['data'], indent=4,ensure_ascii=False))
            return
        self.textbox.insert(index="1.0",text=result)

    