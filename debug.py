import os
import csv
import pandas
file="./RoniData/june_2024.csv"
dataFrames={}
df={"Order #":[],"Sent Date":[],"Modifier":[],"Option Group Name":[],"Parent Menu Selection":[],"Order ID":[]}
with open(file) as f:
    read=csv.reader(f)
    count=0
    for i in read:
        print(count)
        count+=1