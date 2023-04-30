import numpy as np
import pandas as pd
from csv import writer
from datetime import date


class CSVFile():
    def __init__(self,path:str) -> None:
        split_str = path.split("/")
        name_file = split_str[-1]
        path_file = split_str[:-1]
        name_file = name_file.split(".")
        name_file = name_file[:-1]
        self.fileName = ".".join(name_file)
        self.path = "/".join(path_file) + "/"



    def saveData(self,data):
        d = date.today()
        file = self.path + self.fileName + "_success" + str(d) + ".csv" 
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
    
    def saveError(self,data):
        d = date.today()
        file = self.path + self.fileName + "_error" + d + ".csv" 
        with open(file, 'a',encoding="utf-8",newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()


if __name__ == "__main__":
    p = "Z:\@User\ناصر داورزنی\پخش هجرت\out of memory"
