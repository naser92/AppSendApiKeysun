import pandas as pd
import numpy as np

class CheckResult:
    def __init__(self,responseData,listInvoice:pd.DataFrame):
        dfData = pd.DataFrame(responseData)
        
        # listInvoice.insert(loc=0, column='ExcelRowNumber', value=listInvoice.index.to_list())
        self.result =   listInvoice.join(dfData.set_index('uniqueId'), on='uniqueId',validate='1:m',how='left', lsuffix='_left', rsuffix='_right')
        self.result = self.result.replace(np.nan,None)


    def getSuccessResult(self):
        df = self.result[self.result['status'] == 3]
        listDropName = ['ExcelRowNumber','invoiceNumber','uniqueId','status','taxSerialNumber']
        for i in df.columns.values:
            if not i in listDropName :
                df = df.drop(columns=i) 
        return df


    def getErrorResult(self):
        df =  self.result[self.result['status'] != 3]
        df =  df.dropna(subset =['status'])
        listColName = ['ExcelRowNumber','invoiceNumber','uniqueId','status','title','description_right','commodityCode']
        for i in df.columns.values:
            if not i in listColName :
                df = df.drop(columns=i) 
        if "commodityCode" in df.columns.values :
            df = df[['ExcelRowNumber','invoiceNumber','uniqueId','status','title','description_right','commodityCode']] 
        else:
            df = df[['ExcelRowNumber','invoiceNumber','uniqueId','status','title','description_right']] 
        return df

    
    def countSuceeded(self):
        return len(self.result[self.result['status'] == 3])
    

    def countFailed(self):
        errordf = self.result[self.result['status'] != 3]
        errordf = errordf.dropna(subset =['status'])
        return len(errordf['uniqueId'].drop_duplicates())
    

class FackeRecord:
    def __init__(self,Data:pd.DataFrame,status:str,title:str):
        # self.invoices = invoices
        self.data = Data
        self.status = status
        self.title = title

    def get_data(self)-> pd.DataFrame:
        # self.invoices.insert(loc=0, column='ExcelRowNumber', value=self.invoices.index.to_list())
        # listUniqueId = self.data.applymap(lambda x: x['uniqueId'])
        # self.invoices = self.invoices[self.invoices['uniqueId'].isin(listUniqueId)]
        listColName = ['ExcelRowNumber','invoiceNumber','uniqueId','status','title','description']
        self.data = self.data.assign(status = self.status)
        self.data = self.data.assign(title = self.title) 
        for i in self.data.columns.values:
            if not i in listColName :
                self.data = self.data.drop(columns=i) 
        return self.data



if __name__ == "__main__":
    # a = api.getToken("0780637356031","sUmM11kN")
    responce = {
        "data": [
            {
            "status": 1,
            "uniqueId": "ac26c798-6d13-4d34-82ee-5ee96aee7671",
            "trakingId": "0a65423e-8565-4286-bb3d-fe215ccae5bf",
            "taxSerialNumber": "A1112D04C7B000000D87C7",
            "description": "",
            "title": ""
            },
            {
            "status": 1,
            "uniqueId": "ac26c798-6d13-4d34-82ee-fe215ccaeaaa",
            "trakingId": "0a65423e-8565-4286-bb3d-2",
            "taxSerialNumber": "A1112D04C7B000000D87C6",
            "commodityCode" : "12",
            "description": "",
            "title": "فاکتور دو خطا"
            },
            {
            "status": 1,
            "uniqueId": "ac26c798-6d13-4d34-82ee-fe215ccaeaaa",
            "trakingId": "0a65423e-8565-4286-bb3d-2",
            "taxSerialNumber": "A1112D04C7B000000D87C6",
            "description": "",
            "title": "فاکتور دو خطا 2"
            },
            {
            "status": 1,
            "uniqueId": "ac26c798-6d13-4d34-82ee-fe215ccaebbb",
            "trakingId": "0a65423e-8565-4286-bb3d-1",
            "taxSerialNumber": "A1112D04C7B000000D87C5",
            "description": "",
            "title": "فاکتور تک خطا"
            },
            # {
            #           "status": 1,
            #             "uniqueId": "8c98085d-10d7-4c84-b4b6-e55acf246721",
            #             "description": "نوع خریدار نا معتبر است",
            #             "title": "BuyerType"
            # }
        ],
        "error": False,
        "succeeded": True
    }
    data  = pd.DataFrame(responce["data"])
    print (data)
    # indexlist = [
    #     ["1","11","ac26c798-6d13-4d34-82ee-5ee96aee7671"],
    #     ["2","22","0a65423e-8565-4286-bb3d-fe215ccaeaaa"],
    #     ["3","33","0a65423e-8565-4286-bb3d-fe215ccaebbb"]
    # ]
    indexlist = [
        {"indexRow":"1","invocieNumber":"11","uniqueId":"ac26c798-6d13-4d34-82ee-5ee96aee7671","chert":"456464"},
        {"indexRow":"2","invocieNumber":"22","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaeaaa","chert":"456464"},
        {"indexRow":"3","invocieNumber":"33","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaebbb","chert":"456464"},
        {"indexRow":"4","invocieNumber":"44","uniqueId":"ac26c798-6d13-4d34-82ee-e55acf246721","chert":"456464"},
        
    ]

    datatest = [
            {"indexRow":"1","invocieNumber":"11","uniqueId":"ac26c798-6d13-4d34-82ee-5ee96aee7671","chert":"456464"},
        {"indexRow":"4","invocieNumber":"44","uniqueId":"ac26c798-6d13-4d34-82ee-e55acf246721","chert":"456464"},

    ]
    # check = CheckResult(responce["data"],pd.DataFrame(indexlist))
    data = pd.DataFrame(indexlist)
    fake = FackeRecord(data,pd.DataFrame(datatest),"505","ارتباط قطع می باشد")
    data = fake.get_data()
    print (data)
    # print (check.countFailed())
