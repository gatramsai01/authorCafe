import pandas as pd
import os

files=["./annual.csv","./cummulative.csv","./university.csv"]


def extract(file):
    df=pd.read_csv(file)
    outputFile=file.split('.')[1][1:]
    df.to_json(f"{outputFile}.json",orient='records')

for file in files:
    extract(file)