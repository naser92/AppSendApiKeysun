import winreg
import os


class WindowsRegistry:
    def __init__(self) -> None:
        try:
            self.key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Eitak',0,winreg.KEY_WRITE)
        except FileNotFoundError:
            self.key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r'Software\Eitak')

    def writeUsername(self, username):
        self.key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Eitak',0,winreg.KEY_WRITE)
        winreg.SetValueEx(self.key, 'username',0, winreg.REG_SZ, username)
        winreg.CloseKey(self.key)

    def writeFirstLogin(self, value):
        self.key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Eitak',0,winreg.KEY_WRITE)
        winreg.SetValueEx(self.key, 'first_login', 0, winreg.REG_DWORD, value)
        winreg.CloseKey(self.key)

    def getUsername(self):
        try:
            self.key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Eitak',0,winreg.KEY_READ)
            return winreg.QueryValueEx(self.key, 'Username')[0]
        except:
            return None
    
    def getFirstLogin(self):
        try:
            self.key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Eitak',0,winreg.KEY_READ)
            return winreg.QueryValueEx(self.key, 'first_login')[0]
        except:
            return 0




if __name__ == "__main__":
    reg = WindowsRegistry()
    # reg.writeUsername("naser")
    username  = reg.getUsername()
    print(username)
    

