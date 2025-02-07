import tkinter as tk
from tkinter.constants import CENTER, RIGHT
from typing import Text
from gtts import gTTS
import os
import playsound
import time
from tkinter import StringVar, filedialog

"""Fonts"""
font14= ("Verdana", 14)
font17= ("Verdana", 17)
font20 = ("Verdana", 20)
font40 = ("Verdana", 40)

"""VAR GLOBAL"""
global s1
global s2

"""TOL"""
def indexer (index):
    stage = index
    s1 = pinFile[stage]
    s2 = pinFile[stage + 1]
    stageHuman = stage +1
    pin1Var.set(s1)
    pin2Var.set(s2)
    stageVar.set("STAGE\n"+str(stageHuman))
    winScode.update()
    mytext = f'stage {stageHuman}  .   Pin {s1} Connect to pin {s2}   '
    myobj = gTTS(text=mytext, lang='en', slow=True)
    myobj.save("pin.mp3")
    playsound.playsound('pin.mp3')
    print(f'stage {stageHuman} . Pin {s1} Connect to pin {s2}')
    os.remove('pin.mp3')

"""ROL"""
def word():
    timeDelay = int(timerEnt.get())
    startstages  = int(stageEnt.get())
    index = 0
    index +=(startstages-1)
    rower = len(pinFile)
    for i in range(rower):
      time.sleep(timeDelay)
      indexer(index)
      index+=1

"""Open File"""
def browseFiles():  
    global pinFile
    filename = filedialog.askopenfilename(initialdir = "/",
    title = "Select a Scode *.txt File",
    filetypes =(("Text files","*.txt*"),"all files",))
    scodeFile = open(f"{filename}","r")
    listFile = scodeFile.read()
    pinFile = listFile.split(",")

"""GUI TKinter"""
winScode = tk.Tk()
winScode.title("String Art S-Code Machine")
winScode.geometry("760x700")
winScode.config(background="#1a1a1a")
#winScode.iconbitmap("icon.ico")

"""winscode config colume and row"""
winScode.columnconfigure(0,weight=0)
winScode.columnconfigure(1,weight=3)
winScode.columnconfigure(2,weight=0)

"""title text"""
titleText = tk.Label(winScode,text="Choose your Scode by FileManager")
titleText.config(background="#1a1a1a",fg="#F1F1F1",font=font14)
titleText.grid(row=0,column=0,columnspan=3,padx=6, pady=6)

"""upload code Button"""
btnUpload = tk.Button(winScode,text="Upload S-code File")
btnUpload.config(background="#0000FF",fg="#F1F1F1",
        activebackground="#f3f3f3",font=font14,
        bd = 0,command=browseFiles)
btnUpload.grid(row=1,column=0,columnspan=3,pady=6,ipadx=10
        ,ipady=6)

"""timer Label"""
timerLabel = tk.Label(winScode,text = "Delay (second)")
timerLabel.config(background="#1a1a1a",fg="#F1F1F1",justify=CENTER,font=font14)
timerLabel.grid(row=2,column=0,ipadx=20,ipady=4)

"""Entry Get Seconds time Delay"""
timerEnt = tk.Entry(winScode)
timerEnt.config(bg = "#5a5a5a",fg="#f1f1f1",font=font14,justify=CENTER,width=4)
timerEnt.grid(row=3,column=0,ipady=2)
timerEnt.insert(0,"5")
"""Stage Label"""
stageLabel = tk.Label(winScode,text = "Start (Stage)")
stageLabel.config(background="#1a1a1a",fg="#F1F1F1",justify=CENTER,font=font14)
stageLabel.grid(row=2,column=2,ipadx=20,ipady=4)
projectedSales = tk.IntVar()
"""Entry Get Stage Pin"""

stageEnt = tk.Entry(winScode)
stageEnt.config(bg = "#5a5a5a",fg="#f1f1f1",font=font14,justify=CENTER,width=4)
stageEnt.grid(row=3,column=2,ipady=2)
stageEnt.insert(0,"1")
"""Start Button"""
btnStart = tk.Button(winScode,text="START")
btnStart.config(background="#000099",fg="#F1F1F1",justify=CENTER,font=font17,
        activebackground="#f3f3f3",bd = 0,command=word)
btnStart.grid(row=4,column=0,columnspan=3,ipady=10,ipadx=8)

"""pin 1 Label"""
pin1Var = StringVar()
txtPin1 = tk.Label(winScode,textvariable=pin1Var)
txtPin1.config(background="#1a1a1a",fg="#F1F1F1",justify=CENTER,font=font40)
txtPin1.grid(row=5,column=0,columnspan = 3,rowspan=1,pady=15,padx=10,sticky=tk.N)

"""Just Say ( to )"""
scodesym = tk.Label(winScode,text="To")
scodesym.config(background="#1a1a1a",fg="#F1F1F1",justify=CENTER,font=font17)
scodesym.grid(row=6,column=0,columnspan = 3,rowspan=1,pady=10,padx=10)

"""pin 2 Label"""
pin2Var = StringVar()
txtPin2 = tk.Label(winScode,textvariable=pin2Var) 
txtPin2.config(background="#1a1a1a",fg="#F1F1F1",justify=CENTER,font=font40)
txtPin2.grid(row=7,column=0,columnspan = 3,rowspan=1,pady=15,padx=10,sticky=tk.S)

"""Stage Number"""
stageVar = StringVar()
txtStage = tk.Label(winScode,textvariable=stageVar)
txtStage.config(background="#4a4a1a",fg="#F1F1F1",justify=CENTER,font=font20)
txtStage.grid(row=8,column=0,columnspan = 3,rowspan=1,pady=10,padx=10,ipadx=4,ipady=4)

"""stop Button"""
btnStop = tk.Button(winScode,text="STOP",command=winScode.destroy)
btnStop.config(background="#990000",fg="#F1F1F1",justify=CENTER,font=font17,
        activebackground="#f3f3f3",bd = 0)
btnStop.grid(row=9,column=0,columnspan=3,pady=10,ipady=20,ipadx=8,sticky=tk.S)
btnStop.update_idletasks()

"""Make A LOOP"""
winScode.mainloop()

