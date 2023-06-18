import customtkinter as ck
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time


class FormLog():
    def __init__(self,path,master) -> None:
        self.path = path
        self.lock = threading.Lock()
        self.base = ck.CTkToplevel(master)
        self.base.title("EITAK Log")
        self.base.geometry('600x400')
        self.base.iconbitmap("media/image/logo.ico")
        screen_width = self.base.winfo_screenwidth()
        screen_height = self.base.winfo_screenheight()
        x = (screen_width // 2) - (800 // 2)
        y = (screen_height // 2) - (600 // 2)
        self.base.geometry("+{}+{}".format(x, y))
        # self.base.eval('tk::PlaceWindow . center')
        # self.base.resizable(0,0)
        # self.font = font.Font(family='IRANYekan', size=12,file='data/IRANYekanBlackFaNum.ttf' ,weight="bold")
        self.font : tuple = ("Tahoma",9)
        
        # Create text widget
        self.text = tk.Text(self.base, font=self.font)
        self.text.pack(expand=True, fill="both")

        # Create scrollbar widget
        self.scrollbar = tk.Scrollbar(self.text)
        self.scrollbar.pack(side="right", fill="y")

        # Link scrollbar to text widget
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        
        # self.textboxOK = ck.CTkTextbox(self.base, width=600,height=550, corner_radius=0,font=self.font)
        # self.textboxOK.place(x=0,y=40)
        
        # ctk_textbox_scrollbar = ck.CTkScrollbar(self.base, command=self.textboxOK.yview)
        # ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

        # self.textboxOK.configure(yscrollcommand=ctk_textbox_scrollbar.set)

        # self.textboxError = ck.CTkTextbox(self.base, width=300,height=550, corner_radius=0,font=self.font)
        # self.textboxError.place(x=302,y=40)
        self.start_update_thread()


    def start_update_thread(self):
        self.update_thread = threading.Thread(target=self.updateLog)
        self.update_thread.daemon = True
        self.update_thread.start()


    def updateLog(self):

        with open(self.path,'r',encoding="utf-8") as f:
            text = f.read()
            self.text.delete("1.0","end")
            self.text.insert("end",text)
            self.text.see("end")
        # self.base.after(1000,self.updateLog)
    
    def show(self):
        self.base.mainloop()

    

if __name__ == "__main__":
    FormLog("login path")