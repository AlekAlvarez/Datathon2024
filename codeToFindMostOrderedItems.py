import os
import csv
import pandas

dataFrames={}
files=os.listdir("./RoniData")
for i in files:
    dataFrames[i]=pandas.read_csv(f"./RoniData/{i}",encoding="latin-1")
print(dataFrames)
summerDataFrames={"Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[],"Saturday":[],"Sunday":[]}
orderItems={}
for i in files:
    for index, row in dataFrames[i].iterrows():
        if row["Parent Menu Selection"]!="Sides/Desserts":
            if row["Parent Menu Selection"] in orderItems:
                orderItems[row["Parent Menu Selection"]]+=1
            else:
                orderItems[row["Parent Menu Selection"]]=1
        else:
            if row["Modifier"] in orderItems:
                orderItems[row["Modifier"]]+=1
            else:
                orderItems[row["Modifier"]]=1
print(orderItems)