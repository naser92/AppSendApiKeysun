# import hashlib
# from cryptography.fernet import Fernet
# import json


# r = hashlib.md5(b'0015194094')

# print (r.hexdigest())
# key = Fernet.generate_key()
# f = Fernet(key)
# b = str(r.hexdigest())
# print (b)
# token = f.encrypt(b'c9f1b63516f1bd2999c911ca3ec78bd7')
# data = {
#     "token" : token
# }

# with open('personal.txt', 'w') as json_file:
#     json_file.write(str(token))

# programming_languages = ["JavaScript","Python","Java","C++"]
# try:
#     programming_languages.index("Python")
#     print("ok")
# except ValueError:
#     print("That item does not exist")

# import math
# x = 1234.223154145
# try:
#     a = math.modf(x)
#     qq = str(a[0])[1:4]
#     ww = str(a[1])[:-2]
#     a = ww + qq
#     a = float(a)
#     print (a)
# except:
#     a = None


import tkinter as tk



class AlignTest(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.grid()
        self.parent.title('Align test')
        self.createMenus()
        self.createWidgets()


    def createMenus(self):
        # Menu
        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        # Menu->File
        self.fileMenu = tk.Menu(self.menubar)

        # Menu->Quit
        self.fileMenu.add_command(label='Quit',
                                  command=self.onExit)

        # Create File Menu
        self.menubar.add_cascade(label='File',
                                 menu=self.fileMenu)


    def createWidgets(self):

        # Main frame
        self.mainFrame = tk.Frame(self.parent)
        self.mainFrame.grid(row=0, column=0)

        # Outer LabelFrame1
        self.outerLabelFrame1 = tk.LabelFrame(self.mainFrame,
                                             text='Outer1')
        self.outerLabelFrame1.grid(row=0, column=0,sticky='ew')

        # Inner Label
        self.innerLabel = tk.Label(self.outerLabelFrame1,
                                   text='This is a longer string, for example!')
        self.innerLabel.grid(row=0, column=0)


        # Outer LabelFrame2
        self.outerLabelFrame2 = tk.LabelFrame(self.mainFrame,
                                             text='Outer2')
        self.outerLabelFrame2.grid(row=1, column=0, sticky='ew')
        self.outerLabelFrame2.grid_columnconfigure(0, weight=1)

        # Inner labelFrames each with a single labels
        self.innerLabel1 = tk.LabelFrame(self.outerLabelFrame2,
                                         bg='yellow',
                                         text='Inner1')
        self.innerLabel1.grid(row=0, column=0, sticky='ew')
        self.innerLabel1.grid_columnconfigure(0, weight=1)
        self.value1 = tk.Label(self.innerLabel1,
                               bg='green',
                               anchor='e',
                               text='12.8543')
        self.value1.grid(row=0, column=0, sticky='ew')


        self.innerLabel2 = tk.LabelFrame(self.outerLabelFrame2,
                                         bg='yellow',
                                         text='Inner2')
        self.innerLabel2.grid(row=1, column=0, sticky='ew')
        self.innerLabel2.grid_columnconfigure(0, weight=1)
        self.value2 = tk.Label(self.innerLabel2,
                               bg='green',
                               anchor='e',
                               text='0.3452')
        self.value2.grid(row=0, column=0, sticky='ew')


        self.innerLabel3 = tk.LabelFrame(self.outerLabelFrame2,
                                         bg='yellow',
                                         text='Inner3')
        self.innerLabel3.grid(row=2, column=0, sticky='ew')
        self.innerLabel3.grid_columnconfigure(0, weight=1)
        self.value3 = tk.Label(self.innerLabel3,
                               bg='green',
                               anchor='e',
                               text='123.4302')
        self.value3.grid(row=0, column=0, sticky='ew')

    def onExit(self):
        self.parent.quit()



def main():
    root = tk.Tk()
    app = AlignTest(root)
    app.mainloop()



if __name__ == '__main__':
   main()