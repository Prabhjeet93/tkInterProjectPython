import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter import messagebox, END
# Utilize tkinter class to accomplish the following:
#
# Create a window with an appropriate title
from tkinter.messagebox import showinfo

window = tk.Tk()
window.geometry("800x600")
window.title('Welcome to the Class tkinter assignment')
#window_title = tk.Label(text = "Welcome to the CYSE 1002-B 6184 Class March 23st tkinter assignment",foreground="blue",background="black",width = 500,height=5)
#window_title.pack()

#Combo box
label = ttk.Label(text="Please select a Semester:")
label.pack(fill=tk.X, padx=5, pady=5)
label.place(x=400, y = 110)

# create a combobox
selected_sem = tk.StringVar()
sem_cb = ttk.Combobox(textvariable=selected_sem)
# place the widget
sem_cb.pack(fill=tk.X, padx=5, pady=5)
sem_cb.place(x=400, y = 130)



sem_cb['values'] = [('Winter', 'First Semester selected!'),
         ('Spring', 'Second Semester selected!'),
         ('Fall', 'Third Semester selected!'),
         ('Internship', 'Co-op Semester selected!')]

# prevent typing a value
sem_cb['state'] = 'readonly'



# bind the selected value changes
def sem_changed(event):
    ##""" Handle the Semester changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_sem.get()}!'
    )

sem_cb.bind('<<ComboboxSelected>>', sem_changed)



#radio button selection
def show_selected_sem():
    showinfo(
        title='Result',
        message=selected_sem.get()
    )
selected_sem = tk.StringVar()
sizes = (('Winter', 'First Semester selected!'),
         ('Spring', 'Second Semester selected!'),
         ('Fall', 'Third Semester selected!'),
         ('Internship', 'Co-op Semester selected!'))
label = tk.Label(text="Select Any Semester?")
label.pack(fill='x', padx=4, pady=4)
label.place(x=200, y = 110)

# radio buttons
count = 5
for size in sizes:
    r = tk.Radiobutton(
        text=size[0],
        value=size[1],
        variable=selected_sem
    )
    r.pack(padx=4, pady=4)
    r.place(x=200+count, y=140+count)


# # button
# button = tk.Button(
#     text="Get Selected Semester",
#     command=show_selected_sem)
#
# button.pack(fill='x', padx=5, pady=5)
# button.place(x=200,y=300)

#combo box

window.mainloop()
