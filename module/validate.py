
import re
from datetime import datetime
class Validation:
    def __init__(self):
        pass

    def check_data_type(self, value):
        if isinstance(value, int):
            return "integer"
        elif isinstance(value, float):
            return "float"
        elif isinstance(value, str):
            return "string"
        else:
            return "unknown"
        
    def valueDate(self, value):
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if re.match(pattern, str(value)):
            return True
        else: 
            return False
        
    def valueShamsiDate(self, value):
        pattern = r'^\d{4}/\d{2}/\d{2}$'
        if re.match(pattern, str(value)):
            return True
        else: 
            return False
        
    def valueNodecimal(self, value):
        pattern = r'^-?\d+(\.0+)?$'
        if re.match(pattern, str(value)):
            return True
        else: 
            return False
    
    def ValidDate(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return True
        except:
            return False
        

if __name__ == "__main__":
    Valid = Validation()
    print (Valid.valueShamsiDate("20238/12/14"))