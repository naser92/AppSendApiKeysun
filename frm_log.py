import customtkinter as ck

class FormLog():
    def __init__(self) -> None:
        print ("run form")
        self.base = ck.CTk()
        self.base.title("EITAK Log")
        self.base.geometry('600x400')
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
        

        self.textboxOK = ck.CTkTextbox(self.base, width=300,height=550, corner_radius=0,font=self.font)
        self.textboxOK.place(x=0,y=40)
        
        # ctk_textbox_scrollbar = ck.CTkScrollbar(self.base, command=self.textboxOK.yview)
        # ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

        # self.textboxOK.configure(yscrollcommand=ctk_textbox_scrollbar.set)

        self.textboxError = ck.CTkTextbox(self.base, width=300,height=550, corner_radius=0,font=self.font)
        self.textboxError.place(x=302,y=40)
        self.base.mainloop()

if __name__ == "__main__":
    FormLog()