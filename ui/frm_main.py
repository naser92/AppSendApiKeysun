from tkinter import*  
base = Tk()  

class MainForm ():
    def __init__(self):
        self.base = base
        self.base.geometry('500x500')  
        self.base.title("Api keysun")
        Label(self.base,bg="#d1ccc0",text="نرم افزار ارسال صورتحساب کیسان" ,width="500",height="4").pack()
        
        Label(self.base,text="نام کاربری").place(x=400,y=100)
        self.txt_username = Text(self.base,width="15",height="1").place(x=250,y=100)

        Label(self.base,text="کلمه عبور").place(x=400,y=130)
        self.txt_password = Text(self.base,width="15",height="1").place(x=250,y=130)

    def generateForm(self) -> None:
        self.base.mainloop()  
 

if __name__ == "__main__":
    form = MainForm()
    basef = form.generateForm()

    
        