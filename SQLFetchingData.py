import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter import messagebox, END
from tkinter.messagebox import showinfo
import re

# Create a window with an appropriate title
window = tk.Tk()
window.geometry("800x600")
window.title('Welcome to tkinter Class SQL query Demo')

#DB
# ############  create a button that executes a command to display a filtered value from a connection to SQL table such as the
# product Model table on your SQL Database.  Display the filtered value in the list box for user selection.
# Display a message box to the user

def run_query_sql():
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                          'Server=XXX\SQLEXPRESS02;'
                          'Database=AdventureworksLT2019;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    cursor.execute(
        "SELECT DISTINCT  City FROM AdventureWorksLT2019.SalesLT.Address where CountryRegion = 'Canada'")
    # cursor.execute(
    #      "SELECT DISTINCT Name FROM [AdventureWorksLT2019].[SalesLT].[ProductModel]")
    city_lst = []
    for i in cursor:
        print(i)
        s1 = re.sub("[(,')]", "", str(i))
        city_lst.append(s1)
        print(str)

    label_db = tk.Label(text="Select City Name from List")
    label_db.place(x=100, y=100)
    lb_db = tk.Listbox(window,
                       height=15,
                       width=20,
                       foreground="white",
                       background="black",
                       selectmode='Single')
    for n in city_lst:
        lb_db.insert(END, n)
    lb_db.place(x=100, y=120)

    def select_city():
        for i in lb_db.curselection():
            showinfo(
                title='City from SQL Databse',
                message=lb_db.get(i)+ ' City is selected!'
            )
    btn = tk.Button(window, text='Selected City Name', command=select_city)
    query_btn.pack(fill='x', padx=50, pady=50)
    btn.place(x=100, y=400)


query_btn = tk.Button(window,
                   text='Click SQL Query for City',
                   fg='red',
                   command=run_query_sql)
query_btn.pack(fill='x', padx=15, pady=15, expand=True)
query_btn.place(x=80,y=100)



window.mainloop()
