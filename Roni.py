import os
import csv
import pandas
files=os.listdir("./RoniData")
dataFrames={}
for i in files:
    df={"Order #":[],"Sent Date":[],"Modifier":[],"Option Group Name":[],"Parent Menu Selection":[],"Order ID":[]}
    dataFrames[i]=pandas.DataFrame(df)
    with open(f"./RoniData/{i}") as file:
        read=csv.reader(file)
        for j in read:
            if j[0]!="Order #":
                dictionary={"Order #":[j[0]],"Sent Date":[j[1]],"Modifier":[j[2]],"Option Group Name":[j[3]],"Parent Menu Selection":[j[4]],"Order ID":[j[5]]}
                new_row=pandas.DataFrame(dictionary)
                dataFrames[i]=pandas.concat([dataFrames[i],new_row],ignore_index=False)
print(dataFrames)