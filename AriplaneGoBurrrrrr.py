import tkinter
from tkinter.constants import CENTER, END, N, TOP
from typing import AsyncGenerator
    
    

planes = {"Cessna": [5, 5] , "747": [] , "B2 Bomber": [] , "B1 Bomber": []}

pWindow=None
variable = None
def process():
    
    airDensity = 1.225
    velocity = float(e1.get())
    area = float(e2.get())
    length = float(e3.get())
    lengthU = float(e4.get())
    lengthL = float(e5.get())
    v1 = velocity*(lengthU/length)
    v2 = velocity*(lengthL/length)

    upwardPressure = -.5*airDensity*(v2*v2-v1*v1)
    print(upwardPressure)
    setPressure(upwardPressure)

    coefficientLift = (pow(lengthU, 2)-pow(lengthL, 2))/pow(length,2)
    print(coefficientLift)
    setCL(coefficientLift)

    forceLift = upwardPressure * area
    print(forceLift)
    setLift(forceLift)

def presetsWindow():
    global pWindow
    global variable
    pWindow = tkinter.Tk()
    pWindow.title("Presets")
    pWindow.geometry("400x200")
    variable = tkinter.StringVar(pWindow)
    variable.set("None")
    CustomMenu = tkinter.OptionMenu(pWindow, variable, *list(planes.keys()))
    CustomMenu.place(relx=0.35, rely=0.3, width=135)
    tkinter.Label(pWindow, text="Presets", font = ("Arial", 25)).place(relx = 0.4, rely = 0.1)
    LoadButton = tkinter.Button(pWindow, text='Load', width=10, command=Load)
    SaveButton = tkinter.Button(pWindow, text='Save', width=10, command=pWindow.destroy)
    RemoveButton = tkinter.Button(pWindow, text='Remove', width=10, command=pWindow.destroy)

    SaveButton.place(relx = 0.7, rely = 0.5)
    LoadButton.place(relx = 0.375, rely = 0.5)
    RemoveButton.place(relx = 0.05, rely = 0.5)
   
    pWindow.mainloop()

def Load():
    global pWindow
    calculatePresets()
    pWindow.destroy()


def calculatePresets(): 
    input = planes[variable.get()]
    cl = list(input)[0]
    area = list(input)[1]
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e3.insert(0,str(pow(1/(cl/75), 0.5)))
    e4.insert(0, 10.0)
    e5.insert(0, 5.0) 
    e2.insert(0, area)


def setPressure(upwardPressure):
    UPmsg = tkinter.Message(master, text = str(round(upwardPressure, 2)) + " atm", width = 100)
    UPmsg.grid(row = 1, column = 5)

def setCL(coefficientLift):
    CLmsg = tkinter.Message(master, text = str(round(coefficientLift, 2)) , width = 100)
    CLmsg.grid(row = 3, column = 5)

def setLift(forceLift):
    FLmsg = tkinter.Message(master, text = str(round(forceLift, 2))+ " N", width = 100)
    FLmsg.grid(row = 2, column = 5)

master = tkinter.Tk()
master.title('Lift Simulator')






e1 = tkinter.Entry(master)
e2 = tkinter.Entry(master)
e3 = tkinter.Entry(master)
e4 = tkinter.Entry(master)
e5 = tkinter.Entry(master)

button2 = tkinter.Button(master, text='Preset Menu', width=25, command=presetsWindow)
button = tkinter.Button(master, text='Calculate', width=25, command=process)


e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)


button.grid(row=6,column=1)
button2.grid(row=11,column=1)
tkinter.Label(master, text='Custom Measurements').grid(row = 0, column = 1)
tkinter.Label(master, text='         ').grid(row = 0, column = 2)

tkinter.Label(master, text='         ').grid(row = 7, column = 1)
tkinter.Label(master, text='         ').grid(row = 8, column = 1)

tkinter.Label(master, text='Velocity').grid(row=1)
tkinter.Label(master, text='Area').grid(row=2)
tkinter.Label(master, text='Chord Length').grid(row=3)
tkinter.Label(master, text='Upper Length').grid(row=4)
tkinter.Label(master, text='Lower Length').grid(row=5)
tkinter.Label(master, text='Pressure Difference: ').grid(row=1, column = 4)
tkinter.Label(master, text='Force of Lift: ').grid(row=2, column=4)
tkinter.Label(master, text='Coefficient of Lift: ').grid(row=3, column=4)

master.mainloop()

