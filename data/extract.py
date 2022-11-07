import pandas as pd
import numpy as np
import json
annual=pd.read_csv("./csv/annual.csv")
annual=annual.set_index('year')

cummulative=pd.read_csv('./csv/cummulative.csv')
cummulative=cummulative.set_index('year')



class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)





def extract(df):
    data=[]
    cols=df.columns
    for col in cols:
        
        df.loc[df[col]<10,col]=0
        myDict=dict(df[col])
        temp={
            "name":col,
            "data":myDict,
        }
        data.append(temp)

    return data


annualData=extract(annual)

with open('./json/annual.json','w') as outFile:
        outFile.write(json.dumps(annualData,cls=NpEncoder))

cummulativeData=extract(cummulative)

with open('./json/cummulative.json','w') as outFile:
        outFile.write(json.dumps(cummulativeData,cls=NpEncoder))