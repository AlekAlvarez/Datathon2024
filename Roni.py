import os
import csv
import pandas
import PySimpleGUI as gui
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

dataFrames={}
files=os.listdir("./RoniData")
for i in files:
    dataFrames[i]=pandas.read_csv(f"./RoniData/{i}",encoding="latin-1")
print(dataFrames)

#draw graphs onto canvas
def draw_figure(canvas, figure):
    figure_canvas = FigureCanvasTkAgg(figure, canvas)
    figure_canvas.draw()
    figure_canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas

#ALEK: CHNAGE THIS METHOD PLS
#to use month/day/time to return list of x values (amount of each meal type, in the order of the list called mealTypes)
def getInputGraph(month, day, time):
    if month == "April" and day=="Tuesday" and time=="1:00":
        return [1,2,3,4,5,6,7]
    if month == "May" and day=="Tuesday" and time=="1:00":
        return [7,6,5,4,3,2,1]

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
#delete line below, used for testing
itemsOrderedPerMonth={"April":50, "May":35, "June":98}
mealTypes = ["Mac and Cheese", "Grilled Cheese Sandwich", "Cheesecake", "Side Mac", "Cheesy Garlic Bread", "Garlic Bread", "Mac and Cheese Party Tray"]
#delete line below, used for testing
summerPredictions = {"Meal1":{"Mon 11":10, "Mon 12":2, "Mon 1":16}, "Meal2":{"Mon 11":20, "Mon 12":5, "Mon 1":6}}
#delete line below, used for testing
schoolPredictions = {"Meal1":{"Mon 11":10, "Mon 12":2, "Mon 1":16}, "Meal2":{"Mon 11":20, "Mon 12":5, "Mon 1":6}}
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