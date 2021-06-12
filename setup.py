import plotly.express as px
import csv     
import numpy as np
import pandas as pd



def getdatasource(data_path):
    marks =[]
    days =[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))

    return {"x":marks,"y":days}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print('correlation between size of tv and the aveage time speent watching it:- \n---',correlation[0,1])
    

df =pd.read_csv("marks.csv")

fig = px.scatter(df,x = "Marks In Percentage" , y = "Days Present")
fig.show()

def setup():
    data_path ='marks.csv'

    datasource = getdatasource(data_path)
    findcorrelation(datasource)

setup()