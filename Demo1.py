# Create a window with an appropriate title

# create a list box, radio button selection, combo box with values from values in an array defined within the program.
import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter import messagebox, END
from tkinter.messagebox import showinfo

window = tk.Tk()
window.geometry("800x600")
window.title('Welcome to tkinter Class')


#list ---

label = tk.Label(text="State List")
label.pack(fill='x', padx=7, pady=7)
label.place(x=20, y = 120)
subject_list = tk.Label(text = "States")
subjects = ('Alberta','British Columbia','Manitoba','New Brunswick','Nova Scotia','Ontario','Prince Edward Island','Quebec','Saskatchewan')
lb = tk.Listbox(window,
                height = 20,
                width = 30,
                foreground="white",
                background="black",
                selectmode = 'multiple')
for num in subjects:
    lb.insert(END, num)
lb.place(x=20, y = 140)


#Radio button

#Radio button
label = tk.Label(text="Select people status")
label.pack(fill='x', padx=7, pady=7)
label.place(x=300, y = 120)
v0= tk.IntVar()
v0.set(1)
radio_btn1 = tk.Radiobutton(window, text='Citizen',variable=v0,value=1)
radio_btn2 = tk.Radiobutton(window, text='Permanent Residence',variable=v0,value=2)
radio_btn3 = tk.Radiobutton(window, text='Work Permit',variable=v0,value=3)
radio_btn4 = tk.Radiobutton(window, text='Student',variable=v0,value=4)
radio_btn5 = tk.Radiobutton(window, text='Immigrant',variable=v0,value=5)
radio_btn1.place(x=300, y = 160)
radio_btn2.place(x=300, y = 180)
radio_btn3.place(x=300, y = 200)
radio_btn4.place(x=300, y = 220)
radio_btn5.place(x=300, y = 240)

# Combo box

label = ttk.Label(text="Language selection",foreground='green')
label.pack(fill=tk.X, padx=10, pady=10)
label.place(x=550, y = 120)


select_lang = tk.StringVar()   # create a combobox
lang_box = ttk.Combobox(textvariable=select_lang)

lang_box.pack(fill=tk.X, padx=10, pady=10)  # place the widget
lang_box.place(x=550, y = 150)

lang_box['values'] = ['English',
         'French',
         'Punjabi',
         'Urdu']

lang_box['state'] = 'readonly'   # prevent typing a value

def lang_bind(event):     # bind the selected value changes
    showinfo(
        title='Result',
        message=f'You have selected {select_lang.get()} language from Combobox!'
    )

lang_box.bind('<<ComboboxSelected>>', lang_bind)

window.mainloop()
