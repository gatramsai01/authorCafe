import pandas as pd

files=["./csv/annual.csv","./csv/cummulative.csv","./csv/university.csv"]




def extract(file):
    df=pd.read_csv(file)
    outputFile=file.split('/')[2].split('.')[0]
    df.to_json(f"./json/{outputFile}.json")

for file in files:
    extract(file)
