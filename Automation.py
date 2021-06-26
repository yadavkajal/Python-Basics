from tkinter import *
from tkinter import filedialog
import pandas as pd
import sys
sys.path.append('\\PythonVersion\\lib\\site-packages\\win32')
sys.path.append('\\PythonVersion\\lib\\site-packages\\win32\\lib')
import win32com.client as client


def openFile():
    filepath = filedialog.askopenfilename()

    """---------------------------------------
    To check filepath is working
    #print(filepath)
    #file = open(filepath, 'r')
    #print(file.read())
    #file.close()
    ------------------------------------------"""
    #To read a specific columns
    cols=[0,1,4,5,6,7]
    df=pd.read_excel(filepath,usecols=cols)
    #To sort data according to location
    for i in df:
        if(var1==(i[1]=="SINGAPORE (SG)")):
           sheet1= df.to_excel(var1)
           print(sheet1)
        else:
            exit
    
    
    print(df)
    #s=smtplib.SMTP(host='mdssupportservices@us.mcd.com',
    outlook=client.Dispatch("Outlook.Application")
    mail=outlook.Session.Accounts['mdssupportservices@us.mcd.com']
    #to create a new message or new mail
    message=outlook.CreateItem(0)
    message.To='AP-DL-MDS_Market-Comms-Taiwan <MDS_Market-Comms-Taiwan@apmea.mcd.com>;Speck Hung <Speck.Hung@tw.mcd.com>'
    message.Cc='US-APMEA MDS Support Team <mds.l3support@us.mcd.com>; Ang Eric (Contractor) <Eric.Ang@apmea.mcd.com>;mdssupportservices@us.mcd.com'
    message.Subject='MDS TW - Updates required from market end'
    message.Body='Hi Market Team,\n\nBelow table consists of all the ticket/s which requires Market team’s inputs.\nWe request you to review, take actions and revert with the latest updates.\nMoreover, please update the ticket with latest information\n'
    message._oleobj_.Invoke(*(64209,0,8,0,mail))
    message.Display()

    
    """-----------------------------------------
    #To send the mail which we have configured
    message.Save()
    message.Send()
    --------------------------------------------"""
    
window = Tk()
button = Button(text="Click to upload Sheet", command=openFile)
button.pack()
window.mainloop()

