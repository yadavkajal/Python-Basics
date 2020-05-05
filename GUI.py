from tkinter import *
import pandas as pd
from tkinter import filedialog
window=Tk()
window.title("Automation")
#To open a file and read that
def fileopen():
    #global Inc
    file1=filedialog.askopenfilename()
    Inc=pd.read_excel(file1)
    print(Inc)
def fileopen1():
    file2=filedialog.askopenfilename()
    Req=pd.read_excel(file2)
    print(Req)
def fileopen2():
    file3=filedialog.askopenfilename()
    Prb=pd.read_excel(file3)
    print(Prb)
button1=Button(text="Select Incident file",width=40,command=fileopen).pack()
button2=Button(text="SelectRequestFile",width=40,command=fileopen1).pack()
button3=Button(text="SelectProblemFile",width=40,command=fileopen1).pack()
window.mainloop()
