import os
import csv
import pandas
import datetime
import random
import PySimpleGUI as gui
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
def get_day_of_week(string):
    date=datetime.datetime.strptime(string, "%Y-%m-%d")
    s=date.strftime("%A")
    match s.lower():  # Convert input to lowercase for case insensitivity
        case "monday":
            return 1
        case "tuesday":
            return 2
        case "wednesday":
            return 3
        case "thursday":
            return 4
        case "friday":
            return 5
        case "saturday":
            return 6
        case "sunday":
            return 7
dataFrames={}
files=os.listdir("./RoniData")
for i in files:
    dataFrames[i]=pandas.read_csv(f"./RoniData/{i}",encoding="latin-1")
modelDataFrames={"Mac and Cheese" :{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                 "Mac and Cheese Party Tray (Plus FREE Garlic Bread)":{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                "Grilled Cheese Sandwich":{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                'Cheesecake':{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                'Side Mac':{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                'Cheesy Garlic Bread':{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
               'Cheesy Garlic Bread' :{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
              'Garlic Bread'  :{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]}
                 }
validationData={"Mac and Cheese" :{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                 "Mac and Cheese Party Tray (Plus FREE Garlic Bread)":{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                "Grilled Cheese Sandwich":{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                'Cheesecake':{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                'Side Mac':{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
                'Cheesy Garlic Bread':{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
               'Cheesy Garlic Bread' :{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]},
              'Garlic Bread'  :{"Month":[],"Time":[],"Day":[],"OrderNumbers":[]}
                 }
itemsOrderedPerMonth={"April":0,"May":0,"June":0,"July":0,"August":0,"September":0,"October":0}
summerPredictions={"Mac and Cheese" :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
"Mac and Cheese Party Tray (Plus FREE Garlic Bread)" :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
"Grilled Cheese Sandwich" :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Cheesecake' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Side Mac' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Cheesy Garlic Bread' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Garlic Bread' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0}
}
schoolPredictions={"Mac and Cheese" :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
"Mac and Cheese Party Tray (Plus FREE Garlic Bread)" :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
"Grilled Cheese Sandwich" :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Cheesecake' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Side Mac' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Cheesy Garlic Bread' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0},
'Garlic Bread' :{"Mon 11":0,"Mon 12":0,"Mon 1":0,"Mon 2":0,"Mon 3":0,"Mon 4":0,"Mon 5":0,"Mon 6":0,"Mon 7":0,"Mon 8":0,"Mon 9":0,"Tue 11":0,"Tue 12":0,"Tue 1":0,"Tue 2":0,"Tue 3":0,"Tue 4":0,"Tue 5":0,"Tue 6":0,"Tue 7":0,"Tue 8":0,"Tue 9":0,"Wed 11":0,"Wed 12":0,"Wed 1":0,"Wed 2":0,"Wed 3":0,"Wed 4":0,"Wed 5":0,"Wed 6":0,"Wed 7":0,"Wed 8":0,"Wed 9":0,"Thur 11":0,"Thur 12":0,"Thur 1":0,"Thur 2":0,"Thur 3":0,"Thur 4":0,"Thur 5":0,"Thur 6":0,"Thur 7":0,"Thur 8":0,"Thur 9":0,"Fri 11":0,"Fri 12":0,"Fri 1":0,"Fri 2":0,"Fri 3":0,"Fri 4":0,"Fri 5":0,"Fri 6":0,"Fri 7":0,"Fri 8":0,"Fri 9":0,"Sat 11":0,"Sat 12":0,"Sat 1":0,"Sat 2":0,"Sat 3":0,"Sat 4":0,"Sat 5":0,"Sat 6":0,"Sat 7":0,"Sat 8":0,"Sat 9":0, "Sun 11":0,"Sun 12":0,"Sun 1":0,"Sun 2":0,"Sun 3":0,"Sun 4":0,"Sun 5":0,"Sun 6":0,"Sun 7":0,"Sun 8":0,"Sun 9":0}
}
for i in files:
    print(i)
    month=0
    dataInFile={"Mac and Cheese" :{"day":[],"time":[],"order":[],"month":[]},
                 "Mac and Cheese Party Tray (Plus FREE Garlic Bread)":{"day":[],"time":[],"order":[],"month":[]},
                "Grilled Cheese Sandwich":{"day":[],"time":[],"order":[],"month":[]},
                'Cheesecake':{"day":[],"time":[],"order":[],"month":[]},
                'Side Mac':{"day":[],"time":[],"order":[],"month":[]},
                'Cheesy Garlic Bread':{"day":[],"time":[],"order":[],"month":[]},
              'Garlic Bread'  :{"day":[],"time":[],"order":[],"month":[]}
        }
    match i:
        case "april_2024.csv":
            itemsOrderedPerMonth["April"]+=1
            month=4
        case "august_2024.csv":
            itemsOrderedPerMonth["August"]+=1
            month=8
        case "july_2024.csv":
            itemsOrderedPerMonth["July"]+=1
            month=7
        case "june_2024.csv":
            itemsOrderedPerMonth["June"]+=1
            month=6
        case "may_2024.csv":
            itemsOrderedPerMonth["May"]+=1
            month=5
        case "october_2024":
            itemsOrderedPerMonth["October"]+=1
            month=10
        case "september_2024.csv":
            itemsOrderedPerMonth["September"]+=1
            month=9
    for index, row in dataFrames[i].iterrows():
        #print(index)
        if row["Parent Menu Selection"]!="Sides/Desserts" and index!=0:
            name=row["Parent Menu Selection"]
            sent_date=row["Sent Date"]
            date=sent_date[0:10]
            time=sent_date[11:]
            day="Place holder"
            if index!=0:
                k=6
                day=get_day_of_week(date)
            time=time[0:2]
            if name=="Mac and Cheese" or name=="Grilled Cheese Sandwich" or name=="Mac and Cheese Party Tray (Plus FREE Garlic Bread)":
                if time in dataInFile[name]["time"] and day in dataInFile[name]["day"]:
                    index=0
                    for pos, i in enumerate(dataInFile[name]["time"]):
                        if i==time and dataInFile[name]["day"][pos]==day:
                            index=pos
                            break
                    dataInFile[name]["order"][index]+=1
                else:
                    dataInFile[name]["time"].append(time)
                    dataInFile[name]["day"].append(day)
                    dataInFile[name]["order"].append(1)
                    dataInFile[name]["month"].append(month)       
        else:
            name=row["Modifier"]
            if (name=='Cheesecake' or name=='Side Mac' or name=='Cheesy Garlic Bread' or name=='Garlic Bread') and index!=0 :
                if time in dataInFile[name]["time"] and day in dataInFile[name]["day"]:
                    index=0
                    for pos, i in enumerate(dataInFile[name]["time"]):
                        if i==time and dataInFile[name]["day"][pos]==day:
                            index=pos
                            break
                    dataInFile[name]["order"][index]+=1
                else:
                    dataInFile[name]["time"].append(time)
                    dataInFile[name]["day"].append(day)
                    dataInFile[name]["order"].append(1)
                    dataInFile[name]["month"].append(month) 
    for name in dataInFile:
        for i in range(len(dataInFile[name]["time"])):
            #Data has a 1 in 8 chance of being used for validation
            chance=random.randint(1,10)
            if chance==9:
                validationData[name]["Month"].append(dataInFile[name]["month"][i])
                validationData[name]["Time"].append(dataInFile[name]["time"][i])
                validationData[name]["Day"].append(dataInFile[name]["day"][i])
                validationData[name]["OrderNumbers"].append(dataInFile[name]["order"][i])
            else:
                modelDataFrames[name]["Month"].append(dataInFile[name]["month"][i])
                modelDataFrames[name]["Time"].append(dataInFile[name]["time"][i])
                modelDataFrames[name]["Day"].append(dataInFile[name]["day"][i])
                modelDataFrames[name]["OrderNumbers"].append(dataInFile[name]["order"][i])
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
def getError(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=2)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    error = mean_absolute_error(val_y, preds_val)
    return error
models={}
for meal in modelDataFrames:
    leaf_nodes=[]
    error=[]
    train_features=["Month","Time","Day"]
    frame=pandas.DataFrame(modelDataFrames[meal])
    x=frame[train_features]
    y=frame["OrderNumbers"]
    valid=pandas.DataFrame(validationData[meal])
    x_valid=valid[train_features]
    y_valid=valid["OrderNumbers"]
    for i in range(4,12,2):
        leaf_nodes.append(i)
        error.append(getError(i,x,x_valid,y,y_valid))
    model = DecisionTreeRegressor(max_leaf_nodes=leaf_nodes[error.index(min(error))], random_state=1)
    model.fit(x,y)
    models[meal]=model
#draw graphs onto canvas
def draw_figure(canvas, figure):
    figure_canvas = FigureCanvasTkAgg(figure, canvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas

#ALEK: CHNAGE THIS METHOD PLS
#to use month/day/time to return list of x values (amount of each meal type, in the order of the list called mealTypes)
def getInputGraph(month, day, time):
    monthNum=0
    dayNum=0
    match day.lower():  # Convert input to lowercase for case insensitivity
        case "monday":
            dayNum= 1
        case "tuesday":
            dayNum= 2
        case "wednesday":
            dayNum= 3
        case "thursday":
            dayNum= 4
        case "friday":
            dayNum= 5
        case "saturday":
            dayNum= 6
        case "sunday":
            dayNum= 7
    match month.lower():  # Convert input to lowercase to handle case insensitivity
        case "january":
            monthNum=1
        case "february":
            monthNum=2
        case "march":
            monthNum=3
        case "april":
            monthNum=4
        case "may":
            monthNum=5
        case "june":
            monthNum=6
        case "july":
            monthNum=7
        case "august":
            monthNum=8
        case "september":
            monthNum=9
        case "october":
            monthNum=10
        case "november":
            monthNum=11
        case "december":
            monthNum=12
    timeNum=int(time[0:1])
    mealTypes=["Mac and Cheese","Mac and Cheese Party Tray (Plus FREE Garlic Bread)","Grilled Cheese Sandwich",'Cheesecake',
    'Side Mac',
    'Cheesy Garlic Bread',
              'Garlic Bread']
    yValues=[]
    for meal in mealTypes:
        x={"Month":[monthNum],"Time":[timeNum],"Day":[dayNum]}
        x=pandas.DataFrame(x)
        yValues.append(models[meal].predict())
    return yValues
def updateGraph(mealTypes, amountOfMeals):
    ax4.cla()
    ax4.bar(mealTypes,amountOfMeals)
    ax4.set_xlabel("Meal Type")
    ax4.set_ylabel("Amount")
    ax4.set_title(f"Predicted Meals for {month} on {day} at {time}")
    fig1 = plt.gcf()
    return fig1

#graph data
months = ["April", "May", "June", "July", "August", "September", "October"]
mealTypes = ["Mac and Cheese","Mac and Cheese Party Tray (Plus FREE Garlic Bread)","Grilled Cheese Sandwich",'Cheesecake',
    'Side Mac',
    'Cheesy Garlic Bread',
              'Garlic Bread']
#delete line below, used for testing
amountOfMeals=[0,0,0,0,0,0,0]

#bar graph 
fig1 = plt.figure()
gs = gridspec.GridSpec(2,3, height_ratios=(1,1), width_ratios=(1,1,1))
ax1 = plt.subplot(gs[0,:])
ax1.bar(list(itemsOrderedPerMonth.keys()), list(itemsOrderedPerMonth.values()))
ax1.set_title("Total Orders per Month")
ax1.set_xlabel("Months")
ax1.set_ylabel("Total Orders")

#line graph for summer months
ax2 = plt.subplot(gs[1,0])
for key in summerPredictions:
    ax2.plot(list(summerPredictions[key].keys()), list(summerPredictions[key].values()), label=key)
ax2.set_title("Summer Months")
ax2.set_xlabel("Time")
ax2.set_ylabel("Amount of Meal Type")
ax2.legend()

#line graph for school months
ax3 = plt.subplot(gs[1,1])
for key in schoolPredictions:
    ax3.plot(list(schoolPredictions[key].keys()), list(schoolPredictions[key].values()), label=key)
ax3.set_title("School Months")
ax3.set_xlabel("Time")
ax3.set_ylabel("Amount of Meal Type")
ax3.legend()

#input and input graph
month='Month'
day='Day'
time='Time'
ax4 = plt.subplot(gs[1,2])
ax4.bar(mealTypes,amountOfMeals)
ax4.set_xlabel("Meal Type")
ax4.set_ylabel("Amount")
ax4.set_title(f"Predicted Meals for {month} on {day} at {time}")

#gui layout
fig1.tight_layout()
layout = [[gui.Text("Roni's Mac Bar Data")],
          [gui.Canvas(key="Canvas1", size=(1500,600))],
          [gui.Push(), gui.Text("Month"), gui.Input(key="Month"), gui.Push()],
          [gui.Push(), gui.Text("Day of Week", justification="center"), gui.Input(key="Day"), gui.Push()],
          [gui.Push(), gui.Text("Time 1:00-24:00", justification="center"), gui.Input(key="Time"), gui.Button("Plot"), gui.Push()]]
window = gui.Window("Window", layout, finalize=True)

#draw graphs onto canvas
figg_agg = draw_figure(window['Canvas1'].TKCanvas, fig1)
window.maximize()

#event loop
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event =="OK":
        break
    if event == "Plot":
        try:
            #update graph
            month = values["Month"]
            day = values["Day"]
            times = values["Time"]
            amountOfMeals = getInputGraph(values["Month"], values["Day"], values["Time"])
            fig1 = updateGraph(mealTypes, amountOfMeals)
            figg_agg.draw()
        except ValueError:
            gui.popup_error("Invalid input. Try again.")
window.close()