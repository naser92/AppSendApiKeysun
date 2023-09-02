# import pandas as pd
# import os

# path = os.path.join(os.getcwd(),"dataTest\\testpython.xlsx") 

# def newName_col():
#     # if row == 1:
#     #     return "invoice"
#     # elif row == 2:
#     #     return "invvoiceDate"
#     # elif row == 3:
#     #     return "InvicePattern"
#     return["invoice", "invoiceDate", "invicePattern"]
    

# df = pd.read_excel(path,sheet_name='Sheet1')
# df = df.set_axis(newName_col(),axis='columns')

# print (df)

# # load data Csv file

# isinstance
# import math
# Alldata = [12,112,47,445,95,48949,494,464,84,4,48,454,64,84,4,4,54,4,54,584,54,87,24,42,42,29,464,4,3,46,4,4,5,4,54,3,8548,987,84]
# batch_size = 10
# total_batches = math.ceil(len(Alldata) / batch_size)
# data_baches = [Alldata[i * batch_size:(i + 1) * batch_size] for i in range(total_batches)]
# for data in data_baches:
#     print (data)

# import json
# import pandas as pd

# with open('dataTest/json.json', 'r', encoding="utf8") as jsonFile:
#     data_dict = json.load(jsonFile)

# fields_export = ['NameVahed','NameModir','TelKarkhane','TelMarkazi','TelModir','CodePosti','AddressMarkazi','Kargah','ShenasMeli']

# dataList = [{field: data_dict.get(field) for field in fields_export} for data_dict in data_dict]
# df = pd.DataFrame(dataList)

# # df.to_excel('output.xlsx',index=False)
# import pandas as pd

# # create a sample DataFrame
# data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'age': [25, 30, None, 35],
#         'city': ['New York', 'Paris', '', 'London'],
#         'country': ['USA', '', 'France', 'UK']}
# df = pd.DataFrame(data)

# # filter out records with empty strings in the 'city' and 'country' columns
# df_filtered = df.dropna(subset=['age', 'country'])
# print (df_filtered)

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

def main2():
        for p in PRIMES:
          i = is_prime(p)
          print('%d is prime: %s' % (p, i))

if __name__ == '__main__':
    main()
    main2()