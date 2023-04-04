from tkinter import*  
base = Tk()  

class MainForm ():
    def __init__(self):
        self.base = base
        self.base.geometry('500x500')  
        self.base.title("Send Invoice By API To Keysun")
        
    def generateForm(self) -> None:
        self.base.mainloop()  
 

if __name__ == "__main__":
    form = MainForm()
    basef = form.generateForm()

    
        