import pandas as pd
class CheckResult:
    def __init__(self,responseData,listInvoice):
        dfData = pd.DataFrame(responseData)
        dfListInvoice = pd.DataFrame(listInvoice)
        self.result =   dfListInvoice.join(dfData.set_index('uniqueId'), on='uniqueId',validate='1:m')

    def getSuccessResult(self):
        df = self.result[self.result['status'] == 3]
        listDropName = ['description','title']
        for i in df.columns.values:
            if i in listDropName :
                df = df.drop(columns=i) 
        return df


    def getErrorResult(self):
        df =  self.result[self.result['status'] != 3]
        listDropName = ['trakingId','taxSerialNumber']
        for i in df.columns.values:
            if i in listDropName :
                df = df.drop(columns=i) 
        return df

    
    def countSuceeded(self):
        return len(self.result[self.result['status'] == 3])
    
    def countFailed(self):
        errordf = self.result[self.result['status'] != 3]
        return len(errordf['uniqueId'].drop_duplicates())
    



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
            {
                      "status": 1,
                        "uniqueId": "8c98085d-10d7-4c84-b4b6-e55acf246721",
                        "description": "نوع خریدار نا معتبر است",
                        "title": "BuyerType"
            }
        ],
        "error": False,
        "succeeded": True
    }
    # indexlist = [
    #     ["1","11","ac26c798-6d13-4d34-82ee-5ee96aee7671"],
    #     ["2","22","0a65423e-8565-4286-bb3d-fe215ccaeaaa"],
    #     ["3","33","0a65423e-8565-4286-bb3d-fe215ccaebbb"]
    # ]
    indexlist = [
        {"indexRow":"1","invocieNumber":"11","uniqueId":"ac26c798-6d13-4d34-82ee-5ee96aee7671"},
        {"indexRow":"2","invocieNumber":"22","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaeaaa"},
        {"indexRow":"3","invocieNumber":"33","uniqueId":"ac26c798-6d13-4d34-82ee-fe215ccaebbb"},
        {"indexRow":"4","invocieNumber":"44","uniqueId":"8c98085d-10d7-4c84-b4b6-e55acf246721"},
    ]
    check = CheckResult(responce["data"],indexlist)
    print (check.countSuceeded())
