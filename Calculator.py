from tkinter import *
window=Tk()
window.geometry("324x360")
window.title("Calculator")
window.resizable(0,0)
eq=StringVar()

exp=""
def press(num):
    global exp
    exp=exp+str(num)
    eq.set(exp)
def beqclick():
    try:
        global exp
        res=str(eval(exp))
        eq.set(res)
        exp=""
    except:
        eq.set("Error")
        exp=""
t1=Entry(window,width=50,textvariable=eq)
t1.grid(row=0,column=0,columnspan=4)
b1=Button(window,text="1",height=2,width=5,command=lambda:press(1))
b1.grid(row=1,column=0)
b2=Button(window,text="2",height=2,width=5,command=lambda:press(2))
b2.grid(row=1,column=1)
b3=Button(window,text="3",height=2,width=5,command=lambda:press(3))
b3.grid(row=1,column=2)
badd=Button(window,text="+",height=2,width=5,command=lambda:press("+"))
badd.grid(row=1,column=3)
b4=Button(window,text="4",height=2,width=5,command=lambda:press(4))
b4.grid(row=2,column=0)
b5=Button(window,text="5",height=2,width=5,command=lambda:press(5))
b5.grid(row=2,column=1)
b6=Button(window,text="6",height=2,width=5,command=lambda:press(6))
b6.grid(row=2,column=2)
bsub=Button(window,text="-",height=2,width=5,command=lambda:press("-"))
bsub.grid(row=2,column=3)
b7=Button(window,text="7",height=2,width=5,command=lambda:press(7))
b7.grid(row=3,column=0)
b8=Button(window,text="8",height=2,width=5,command=lambda:press(8))
b8.grid(row=3,column=1)
b9=Button(window,text="9",height=2,width=5,command=lambda:press(9))
b9.grid(row=3,column=2)
bdiv=Button(window,text="/",height=2,width=5,command=lambda:press("/"))
bdiv.grid(row=3,column=3)
b0=Button(window,text="0",height=2,width=5,command=lambda:press(0))
b0.grid(row=4,column=1)
def bdotclick():
    entry.set(".")
bdot=Button(window,text=".",height=2,width=5,command=bdotclick)
bdot.grid(row=4,column=0)

beq=Button(window,text="=",height=2,width=5,command=beqclick)
beq.grid(row=4,column=2)
bmul=Button(window,text="X",height=2,width=5,command=lambda:press("*"))
bmul.grid(row=4,column=3)
