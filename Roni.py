import os
import csv
import pandas
import PySimpleGUI as gui
import matplotlib.pyplot as plt
dataFrames={}
for i in files:
    dataFrames[i]=pandas.read_csv(f"./RoniData/{i}",encoding="latin-1")
print(dataFrames)

#draw graphs onto canvas

#line graph for summer months (june/july/august)
fig1, ax = plt.subplots()
ax.plot([1,2],[3,4])
ax.set_title("Summer Months")

#line graph for school months
fig2, ax = plt.subplots()
ax.plot([2,3],[4,5])
ax.set_title("School Months")

#gui layout
layout = [[gui.Text("Roni's Mac Bar Data")],
          [gui.Canvas(key="Canvas1"), gui.Canvas(key="Canvas2")]]
window = gui.window("Window", layout, finalize=True)
#draw graphs onto window
fig_canvas_agg1 = gui.draw_figure(window["Canvas1"].TKCanvas, fig1)
fig_canvas_agg2 = gui.draw_figure(window["Canvas2"].TKCanvas, fig2)

#event loop
while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event =="OK":
        break
window.close()