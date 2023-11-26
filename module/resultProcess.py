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
        listDropName = ['ExcelRowNumber','invoiceNumber','uniqueId','status','taxSerialNumber','trakingId']
        for i in df.columns.values:
            if not i in listDropName :
                df = df.drop(columns=i) 
        try:
            df = df[['ExcelRowNumber','invoiceNumber','uniqueId','status','trakingId','taxSerialNumber']]
        except:
            try:
                df = df[['ExcelRowNumber','invoiceNumber','uniqueId','status','trakingId']]
            except:
                pass
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
        listColName = ['ExcelRowNumber','invoiceNumber','uniqueId','status','title']
        self.data = self.data.assign(status = self.status)
        self.data = self.data.assign(title = self.title) 
        for i in self.data.columns.values:
            if not i in listColName :
                self.data = self.data.drop(columns=i) 
        return self.data


class CheckResultCommodityRequest:
    def __init__(self,responseData,listCommodity:pd.DataFrame):
        dfData = pd.DataFrame(responseData)
        self.result =  listCommodity.join(dfData.set_index('commodityCode'), on='commodityCode',validate='1:m',how='left', lsuffix='_left', rsuffix='_right')
        self.result = self.result.replace(np.nan,None)

    def countSuceeded(self):
        return len(self.result[self.result['status'] == 3])
    
    def countFailed(self):
        errordf = self.result[self.result['status'] != 3]
        errordf = errordf.dropna(subset =['status'])
        return len(errordf['commodityCode'].drop_duplicates())
    
    def getSuccessResult(self):
        df = self.result[self.result['status'] == 3]
        listDropName = ['ExcelRowNumber','commodityCode','status','description','title']
        for i in df.columns.values:
            if not i in listDropName :
                df = df.drop(columns=i) 
        try:
            df = df[['ExcelRowNumber','commodityCode','status','description','title']]
        except:
           pass

        return df

    def getErrorResult(self):
        df =  self.result[self.result['status'] != 3]
        df =  df.dropna(subset =['status'])
        listColName = ['ExcelRowNumber','commodityCode','status','description','title']
        for i in df.columns.values:
            if not i in listColName :
                df = df.drop(columns=i) 
        df = df[['ExcelRowNumber','commodityCode','status','description','title']]
        return df    

    def FakeData(self,Data:pd.DataFrame,status:str,description:str):
        listColName = ['ExcelRowNumber','commodityCode','status','description']
        Data = Data.assign(status = status)
        Data = Data.assign(description = description) 
        for i in Data.columns.values:
            if not i in listColName :
                Data = Data.drop(columns=i) 
        return Data

if __name__ == "__main__":
    # a = api.getToken("0780637356031","sUmM11kN")
    responce = {
        "data": [
            {
            "rowIndex":0,
            "status": 3,
            "commodityCode": "2001111442116",
            "description": "کد کالا خدمت ثبت شد",
            "title": "CommodityCode"
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
            "status": 3,
            "uniqueId": "ac26c798-6d13-4d34-82ee-fe215ccaebbb",
            "trakingId": "0a65423e-8565-4286-bb3d-1",
            "description": "",
            "taxSerialNumber": "A1112D04C7B000000D87C5",
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
        {"ExcelRowNumber":"1","":"11","uniqueId":"ac26c798-6d13-4d34-82ee-5ee96aee7671","chert":"456464"},
        {"ExcelRowNumber":"2","commodityCode":"22","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaeaaa","chert":"456464"},
        {"ExcelRowNumber":"3","invoiceNumber":"33","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaebbb","chert":"456464"},
        {"ExcelRowNumber":"4","invoiceNumber":"44","uniqueId":"ac26c798-6d13-4d34-82ee-e55acf246721","chert":"456464"},
        
    ]

    datatest = [
            {"ExcelRowNumber":"1","invoiceNumber":"11","uniqueId":"ac26c798-6d13-4d34-82ee-5ee96aee7671","chert":"456464"},
        {"ExcelRowNumber":"4","invoiceNumber":"44","uniqueId":"ac26c798-6d13-4d34-82ee-e55acf246721","chert":"456464"},

    ]
    check = CheckResult(responce["data"],pd.DataFrame(indexlist))
    data = pd.DataFrame(indexlist)
    # fake = FackeRecord(data,pd.DataFrame(datatest),"505","ارتباط قطع می باشد")
    # data = fake.get_data()
    # print (data)
    print (check.getSuccessResult())
