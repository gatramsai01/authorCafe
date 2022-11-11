import pandas as pd
import numpy as np
import json
annual=pd.read_csv("./csv/annual.csv")
annual=annual.set_index('year')





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
    row=set()

    for col in cols:
        x=df.query(f'{col}<10').index 
        row.update(x)

    df=df.drop(row)


    for col in cols:
        
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

