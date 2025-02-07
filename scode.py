import tkinter as tk
from tkinter import StringVar, filedialog

"""Fonts"""
font14= ("Verdana", 14)
font17= ("Verdana", 17)
font35 = ("Verdana", 35)
font40 = ("Verdana", 40)

###################################################
global indez 
global s1
global s2
indez = -1

def browseFiles():  
    global pinFile
    global rower
    filename = filedialog.askopenfilename(initialdir = "/",
    title = "Select a Scode *.txt File",
    filetypes =(("Text files","*.txt*"),"all files",))
    scodeFile = open(f"{filename}","r")
    listFile = scodeFile.read()
    pinFile = listFile.split(",")
    rower = len(pinFile)
    print('len : >> ',rower)


def indexer(index):
    s1 = pinFile[index]#stage
    s2 = pinFile[index + 1]#stage
    stepHuman = index +1 #stage
    pin1.set(str(s1))
    pin2.set(str(s2))
    step.set("Step\n"+str(stepHuman))
    winScode.update()
    print(f'LOG -- >> Step {stepHuman} . Pin {s1} Connect to pin {s2}')

def plusOne():
    global indez 
    rr = rower -3
    if indez <= rr:
        indez +=  1
        if indez in range(0,rower):
            indexer(indez)
            Scode1.update()
        else:
           print("OUT Of Index")
           pass


def plusOneH():
    global indez 
    rr = rower -103
    if indez <= rr:
        indez +=  100
        if indez in range(0,rower):
            indexer(indez)
            Scode1.update()
        else:
           print("OUT Of Index")
           pass


def minesOne():
    global indez 
    if indez >=1:
        indez -=  1
        if indez in range(0,rower):
            indexer(indez)
        else:
            print("OUT Of Index")
            pass


def minesOneH():
    global indez 
    if indez >=100:
        indez -=  100
        if indez in range(0,rower):
            indexer(indez)
        else:
            print("OUT Of Index")
            pass



###################################################
"""GUI TKinter"""
winScode = tk.Tk()
winScode.title("String Art S-Code Machine")
winScode.geometry("660x660")
winScode.config(background="#1a1a1a")

"""winscode config colume and row"""
winScode.columnconfigure(0,weight=0)
winScode.columnconfigure(1,weight=1)
winScode.columnconfigure(2,weight=0)
winScode.rowconfigure(0, weight=0)
winScode.rowconfigure(1, weight=0)
winScode.rowconfigure(2, weight=3)
winScode.rowconfigure(3, weight=3)
winScode.rowconfigure(4, weight=3)
winScode.rowconfigure(5, weight=3)

"""title text"""
scodeTxt = tk.Label(winScode,text="Choose your S-code by FileManager")
scodeTxt.config(background="#1a1a1a",fg="#F1F1F1",font=font14)
scodeTxt.grid(row=0,column=0,columnspan=3,padx=10, pady=12)

"""upload code Button"""
btnScodeUp = tk.Button(winScode,text="Upload S-code File",command=browseFiles)
btnScodeUp.config(background="#1a1a1a",fg="#F1F1F1",font=font17,
    activebackground="#f3f3f3",bd = 0)
btnScodeUp.grid(row=1,column=0,columnspan=3,padx= 10,pady=10,ipadx=10
    ,ipady=10)

"""Next Step Button"""
btnScodeNxt = tk.Button(winScode,text="next",command=plusOne)
btnScodeNxt.config(background="#1a1a1a",fg="#F1F1F1",
                font=font17,activebackground="#f3f3f3",bd = 0,height=50)
btnScodeNxt.grid(row=2,column=2,columnspan=1,rowspan=3,padx=5,pady=10,
    ipadx=15,ipady=20,sticky = tk.E)

"""Last Step Button"""
btnScodeLst = tk.Button(winScode,text="Last",command=minesOne)
btnScodeLst.config(background="#1a1a1a",fg="#F1F1F1",
                font=font17,activebackground="#f3f3f3",bd = 0,height=50)
btnScodeLst.grid(row=2,column=0,columnspan=1,rowspan=3,padx=5,pady=10,
    ipadx=15,ipady=20,sticky = tk.W)

"""pin1 Label"""
pin1 = StringVar()
Scode1 = tk.Label(winScode,textvariable=pin1)
Scode1.config(background="#1a1a1a",fg="#F1F1F1",font=font40)
Scode1.grid(row=2,column=1,pady=10,rowspan=1,padx=10,sticky=tk.N)

"""Just Say To"""
scodesym = tk.Label(winScode,text='To')
scodesym.config(background="#1a1a1a",fg="#F1F1F1",font=font17)
scodesym.grid(row=3,column=1,rowspan=1,pady=10,padx=10)

"""pin2 Label"""
pin2 = StringVar()
Scode2 = tk.Label(winScode,textvariable=pin2)  
Scode2.config(background="#1a1a1a",fg="#F1F1F1",font=font40)
Scode2.grid(row=4,column=1,rowspan=1,pady=10,padx=10,sticky=tk.S)

"""Next 100 Step Button"""
btnScodeNxt100 = tk.Button(winScode,text="100>>",command=plusOneH)
btnScodeNxt100.config(background="#2a2a2a",fg="#F1F1F1",
                font=font14,activebackground="#f3f3f3",bd = 0,height=15)
btnScodeNxt100.grid(row=5,column=2,padx=5,pady=15,ipadx=15,ipady=15,sticky=tk.E)

"""Last 100 Step Button"""
btnScodeLst100 = tk.Button(winScode,text="<<100",command=  minesOneH)
btnScodeLst100.config(background="#2a2a2a",fg="#F1F1F1",
                font=font14,activebackground="#f3f3f3",bd = 0,height=15)
btnScodeLst100.grid(row=5,column=0,padx=5,pady=15,ipadx=15,ipady=15,sticky=tk.W)
    
"""step label"""
step = StringVar()
scodeStep = tk.Label(winScode,textvariable=step)
scodeStep.config(background="#2a2a2a",fg="#F1F1F1",font=font17)
scodeStep.grid(row=5,column=1,rowspan=1,ipady=25,ipadx=25,padx=2,pady=2,sticky=tk.S)


winScode.mainloop()





