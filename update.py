import requests as r
import os
import zipfile
from tqdm import tqdm

class Updater:
    def __init__(self) -> None:
        pass

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
            name  =  "Eitak_" + v + ".zip" 
            # name  =  "Test_" + v + ".zip" 
            responce  = r.get(self.url,stream=True)
            file_path = os.path.join(os.getcwd(),name)
            total_size = int(responce.headers.get('content-length', 0))
            block_size = 1024

            with open(file_path, 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=f'Downloading Eitak_{v}') as pbar:
                    for data in responce.iter_content(block_size):
                        pbar.update(len(data))
                        f.write(data)
            return file_path
        return None
    
    def delete_file(self):
        curen_dir = os.getcwd()
        items = os.listdir(curen_dir)
        try:
            for item in items :
                item_path = os.path.join(curen_dir,item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    os.rmdir(item_path)
            return True
        except Exception as e:
            print(f"An error removeFile: {e}")
            return False

    
    def update_file (self):
        file = self.download_update()
        if file != None:
            try:
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    for file_info in zip_ref.infolist():
                        file_name = file_info.filename
                        target_path = os.path.join(os.getcwd(),file_name)
                        print(target_path)

                        if file_name.endswith('/'):
                            os.makedirs(target_path, exist_ok=True)
                            continue


                        if os.path.exists(target_path):
                            os.remove(target_path)
                        
                        target_dir = os.path.dirname(target_path)

                        if not os.path.exists(target_dir):
                            os.makedirs(target_dir)

                        with open(target_path, 'wb') as f:
                            f.write(zip_ref.read(file_info))

                os.remove(file)
                print ("The update was completed successfully")
            except:
                print("The update encountered an error")
        else:
            print("The update encountered an error")

        input ("")


if __name__ == "__main__":
   update =  Updater()
   update.update_file()