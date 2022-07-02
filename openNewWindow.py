#Import tkinter library
from tkinter import *
from tkinter import ttk
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
win.title("PythonClass")
#Define a new function to open the window

def open_win():
   new= Toplevel(win)
   new.geometry("750x250+200+50")
   new.title("New Window")
   #Create a Label in New window
   Label(new, text="Python Class", font=('Verdana 50 bold')).pack(pady=30)
   Label(win, text="2+2", font=('Verdana 17 bold')).pack(pady=30)

#Create a label
Label(win, text= "Click the below button to Open a New Window", font= ('Verdana 17 bold')).pack(pady=30)
#Create a button to open a New Window
ttk.Button(win, text="Open New Wind ", command=open_win).pack()
win.mainloop()
