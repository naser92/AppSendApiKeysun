import requests as r
import os
import zipfile

class Updater:
    def __init__(self) -> None:
        self.url = ""

        self.update_file()

    def GetVersion (self):
        response = r.get("https://files.mizeonline.ir/tps/assets/Eitak/eitak.json")
        if response.status_code == 200:
            data = response.json()
            try:
                self.url = data['url']
            except:
                self.urlVersion = None

            return data['version']
        else:
            return "0"

    def download_update(self):
        v = self.GetVersion()
        if v == "0" :
            print ("server Error Please try again ...")
        else:
            # name  =  "Eitak_" + v + ".zip" 
            name  =  "Test_" + v + ".zip" 
            responce  = r.get(self.url)
            file_path = os.path.join(os.getcwd(),name)

            with open(file_path, 'wb') as f:
                f.write(responce.content)

            return file_path
        return None
    
    def update_file (self):
        file = self.download_update()
        if file != None:
            try:
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    for file_info in zip_ref.infolist():
                        file_name = file_info.filename
                        target_path = os.path.join(os.getcwd(),file_name)

                        if file_name.endswith('/'):
                            os.makedirs(target_path, exist_ok=True)
                            continue

                        if os.path.exists(target_path):
                            os.remove(target_path)

                        with open(target_path, 'wb') as f:
                            f.write(zip_ref.read(file_info))

                os.remove(file)
                print ("The update was completed successfully")
            except:
                print("The update encountered an error")
        else:
            print("The update encountered an error")


if __name__ == "__main__":
    Updater()