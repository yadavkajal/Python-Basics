from tkinter import *
from tkinter import filedialog
window=Tk()
window.title("Automation")
def fileopen():
    file1=filedialog.askopenfile()
    label=Label(text=file1).pack()
def fileopen1():
    file2=filedialog.askopenfile()
    label2=Label(text=file2).pack()
button1=Button(text="Select Incident file",width=40,command=fileopen).pack()
button2=Button(text="SelectRequestFile",width=40,command=fileopen1).pack()

window.mainloop()
