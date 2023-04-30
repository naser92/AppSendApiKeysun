import numpy as np
import pandas as pd
from csv import writer
from datetime import date
import time

class CSVFile():
    def __init__(self,path:str) -> None:
        split_str = path.split("/")
        name_file = split_str[-1]
        path_file = split_str[:-1]
        name_file = name_file.split(".")
        name_file = name_file[:-1]
        self.fileName = ".".join(name_file)
        self.path = "/".join(path_file) + "/"
        self.curentTime = str(time.strftime("%H-%M"))
        self.today = date.today()


    def saveData(self,data):
       
        file = self.path + self.fileName + "_success_" + str(self.today) + "_" + self.curentTime + ".csv" 
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
    
    def saveError(self,data):
      
        file = self.path + self.fileName + "_error_" + str(self.today) +"_" + self.curentTime + ".csv" 
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()


if __name__ == "__main__":
    import time
    print (time.strftime("%H:%M"))