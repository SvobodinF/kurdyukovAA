import requests 
import json
from tkinter import *
import time 

def getUserData(userName):
    url = f"https://api.github.com/users/{userName}"

    return requests.get(url).json()

def saveResult(value):
    file = open("gitParse.json", "w")
    file.writelines(json.dumps(value))
    
keys = [
    'company',
    'created_at',
    'email',
    'id',
    'name',
    'url'
]

def getData():
    userData = getUserData(txt.get())

    n: dict = {}

    n['timestamp'] = time.time()

    for i in range(len(keys)):  
        n[keys[i]] = userData[keys[i]]
        
    saveResult(n)

window = Tk()  
window.title("Git Parser by Name")  
window.geometry('400x250')  
txt = Entry(window,width=20)  
txt.grid(column=0, row=0)  
btn = Button(window, text="Не нажимать!", command=getData)  
btn.grid(column=1, row=0)  
window.mainloop()
