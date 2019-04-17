# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:12:21 2018

@author: gitsar
"""

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

from random import seed
from random import random
from random import randint
from numpy.random import randint

window = tk.Tk()

window.configure(background="#4196E9")

""" create a button when clicked opens the plot window """
window.geometry("300x300")
l1= tk.Label(window,background="#024D95",foreground="#F4FAFF", text="First value").grid(row=1,column=1)
l2= tk.Label(window,background="#024D95",foreground="#F4FAFF", text="Second Value").grid(row=2,column=1)

e1 = tk.Entry(window)
e2 = tk.Entry(window)

value1=value2=0
arrayInt1=arrayInt2=[]

e1.grid(row=1, column=3)
e2.grid(row=2, column=3)
 
#functions


def ShowEntries():
    value1 = e1.get()
    value2 = e2.get()
   
    messagebox.showinfo("Valeurs Entrees","Valuers saisies: "+value1+","+value2 )
    e1.delete(0,END)
    e2.delete(0,END)    
 
def generateRandomNumbers():
    try:
        
        minVal = int(e1.get())
        maxVal = int(e2.get())
        generatedNum = randint(minVal,maxVal)
        #e1.delete(0,END)
        #e2.delete(0,END)
        messagebox.showinfo("Nombre Generé ",generatedNum )
        print(generatedNum)
    except ValueError:
        messagebox.showinfo("Errors!","Please Fill the Fields" )
        pass
     


def randomFillArray():
    arrayInt1 =randint(0, 10, 20)
    print("first array:\n")
    print(arrayInt1)
   
    arrayInt2 = randint(0,10,20)
    print("second array:\n")
    print(arrayInt2)
    
    plt.plot(arrayInt1,arrayInt2)
    
    
    
     
#setting the GUI

    
btnShowEntries = tk.Button(window, text="Show Values",background="#0E1A26",foreground="#ACB2B8", command = ShowEntries)
btnShowEntries.place(x=50,y=60)

btnGenerate = tk.Button(window, text="generate",background="#0E1A26",foreground="#ACB2B8", command = generateRandomNumbers)  
btnGenerate.place(x=200,y=60)
    
btnFillArray = tk.Button(window, text="Generate Graph",background="#0E1A26",foreground="#ACB2B8", command = randomFillArray)
btnFillArray.place(x=50,y=90)  

window.mainloop()
     


"""  """