from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

mongoUrl='mongodb://root:example@localhost:27017/'

client=MongoClient(mongoUrl)

db=client['authorCafe']



def dataParser(dataList):
    labels=list(dataList[0]['data'].keys())
    data=[]
    for i in dataList:
     unviName=i['name']
     univData=list(i['data'].values())
     temp={
        "label":unviName,
        "data":univData
     }
     data.append(temp)
    return {
        "labels":labels,
        "datasets":data
     }


@app.get('/annual',status_code=200)
def root():

    dataList=list(db.annual.find())

    res=dataParser(dataList)
    
    return res


@app.get('/cummulative',status_code=200)
def root():

    dataList=list(db.cummulative.find())

    res=dataParser(dataList)
    
    return res