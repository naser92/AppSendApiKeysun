# import requests as r
# import json
# response   = r.get("https://files.mizeonline.ir/tps/assets/Eitak/eitak.json")
# if response.status_code == 200:
#     data = response.json()
# a = data['version']
# print (a)



# test = [0, 1, 2, 3, 4, 5, 6]
# print(test.pop(0))
# test.append(18)
# print(test)
# print(test.pop(0))


# import jdatetime
# date = str("1402/03/12").split('/')
# date = jdatetime.date(int(date[0]),int(date[1]),int(date[2])).togregorian()
# print(date)

# import tkinter as tk
# from tkinter import messagebox
import configparser

# # Create the frm_login window
# class LoginWindow:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Login")

#         # Create the username label and entry
#         tk.Label(self.master, text="Username").grid(row=0, column=0)
#         self.username_entry = tk.Entry(self.master)
#         self.username_entry.grid(row=0, column=1)

#         # Create the password label and entry
#         tk.Label(self.master, text="Password").grid(row=1, column=0)
#         self.password_entry = tk.Entry(self.master, show="*")
#         self.password_entry.grid(row=1, column=1)

#         # Create the login button
#         tk.Button(self.master, text="Login", command=self.login).grid(row=2, column=1)

#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()

#         # Verify the login credentials
#         if username == "admin" and password == "password":
#             # Store the login status in a configuration file
#             config = configparser.ConfigParser()
#             config['DEFAULT'] = {'LoggedIn': 'True'}
#             with open('config.ini', 'w') as f:
#                 config.write(f)

#             # Close the frm_login window
#             self.master.destroy()
#         else:
#             messagebox.showerror("Error", "Invalid login credentials")

# # Create the frm_version window
# class VersionWindow:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Version")
#         tk.Label(self.master, text="Version 1.0").pack()

# # Create the frm_main window
# class MainWindow:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Main")

#         # Check the login status in the configuration file
#         config = configparser.ConfigParser()
#         config.read('config.ini')
#         if config['DEFAULT'].getboolean('LoggedIn', fallback=False):
#             # Show the frm_version window
#             VersionWindow(tk.Toplevel(self.master))
#         else:
#             # Show the frm_login window
#             LoginWindow(tk.Toplevel(self.master))

# # Create the main Tkinter window
# root = tk.Tk()
# MainWindow(root)
# root.mainloop()
import tkinter as tk
from tkinter import Scrollbar

def create_scrollable_text(root, x, y, text):
    text_widget = tk.Text(root, wrap="none", state="normal")
    text_widget.insert("end", text)
    text_widget.place(x=x, y=y)
    text_widget.tag_configure("rtl", justify="right")
    scrollbar = Scrollbar(root, command=text_widget.yview)
    scrollbar.place(x=x + text_widget.winfo_reqwidth(), y=y, height=text_widget.winfo_reqheight())

    text_widget['yscrollcommand'] = scrollbar.set

# ساخت پنجره اصلی
root = tk.Tk()
root.geometry("400x200")
root.title("نمونه اسکرولی فارسی در Tkinter")

# متن‌های فارسی
text1 = "این یک متن فارسی است که در نقطه مشخصی قرار می‌گیرد."
text2 = "این هم یک متن دیگر فارسی است که در کنار متن اول قرار می‌گیرد."

# ایجاد ویجت متنی با اسکرول
create_scrollable_text(root, x=10, y=100, text=f"{text1}\n\n{text2}")

root.mainloop()