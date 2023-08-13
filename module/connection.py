import socket
import urllib.request
import subprocess as s

class CheckInternet():
    def __init__(self):
        self.IpDNS = "8.8.8.8"
        self.url = "https://mizeonline.ir/"
    
    def checkInternetConnection(self) -> bool:
        try :
            socket.create_connection(("8.8.8.8",53),timeout=2)
            return True
        except:
            return False
        
    def checkServerConnection(self) -> bool:
        try :
            if s.call(["ping", "185.143.234.120"])==0 :
                return True
            else:
                return False
        except:
            return False
        

if __name__ == "__main__":
    inter = CheckInternet()
    while True:
        a = inter.checkServerConnection()
        print ("internet connet" if a else "connect Faild")