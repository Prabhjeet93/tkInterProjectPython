import tkinter as tk
from tkinter import ttk
import pyodbc
from tkinter import messagebox, END
# Utilize tkinter class to accomplish the following:
#
# Create a window with an appropriate title
from tkinter.messagebox import showinfo

window = tk.Tk()
window.geometry("800x600")    ## size of the window defined
window.title('Demo of TKINTER Class in Python')  ## Title of the window defined
window_title = tk.Label(text = "Welcome to the Class March 23st tkinter assignment",    ## main heading of the page defined
                        foreground="blue",   ## color of the text defined
                        background="black",   ## background color of the label box is defined
                        width = 80,    ### width of the label box is defined
                        height=2)    ### Height of the label box is defined
window_title.pack()   ## calling the pack method for the window title text
# create a list box, radio button selection, combo box with values from values in an array defined within the program.

#List box created.
label = tk.Label(text="Select Any Subject")   ### Heading of the List is defined and stored in a variable
label.pack(fill='x', padx=4, pady=4)    ### pack method called for the heading text
label.place(x=5, y = 100)     ## Position of the heading text is defined on application UI
subjects = ("Python", 'Business Comm', 'Networking','Principle of CS', 'Information Security','Artificial Intelligence','Cloud Computing','Chemistry', 'Physics')   ## data for the list box is defined in a list
lb = tk.Listbox(window,    ## creating a List box to show above list values
                height = 10,   ## height of the List box is mentioned
                width = 20,     ## width of the List box is mentioned
                foreground="green",     ## color of the List box's data is mentioned
                background="red",     ## Background color of the List box is mentioned
                selectmode = 'multiple')     ## how many values can be selected in the list is defined. It could be single or multiple
for num in subjects:   #for loop to traverse list to insert in the list box
    lb.insert(END, num)   ## inserting list values in the list box
lb.place(x=5, y = 130)     ## Position of the list box is mentioned.

#Radio button upgraded
label = tk.Label(text="Select Any Course")        ### Heading of the Radio button is defined and stored in a variable
label.pack(fill='x', padx=4, pady=4)    ### pack method called for the heading text
label.place(x=200, y = 100)              ## place of the heading text is defined on application UI
v0= tk.IntVar()     ## A variable defined using IntVar() function holds integer data where we can set integer data and can retrieve it as well using getter and setter methods.
v0.set(1)           ## setting the selected value in radio button
r1 = tk.Radiobutton(window, text='Cyber Security',variable=v0,value=1)     ## Radio button1 created and stored in the variable r1 with text and value fields
r2 = tk.Radiobutton(window, text='Database Management System',variable=v0,value=2)    ## Radio button created and stored in the variable r2 with text and value fields
r3 = tk.Radiobutton(window, text='Python Developer',variable=v0,value=3)  ## Radio button created and stored in the variable r3 with text and value fields
r1.place(x=200, y = 120)     ## Position of the r1 radio button is mentioned.
r2.place(x=200, y = 140)     ## Position of the r2 radio button is mentioned.
r3.place(x=200, y = 160)     ## Position of the r3 radio button is mentioned.

# creating a combo box or dropdown and displaying message after selecting a value from it. with the defined array values.

label = ttk.Label(text="Please select a Semester:")   ### Heading of the combo box/ dropdown is defined and stored in a variable
label.pack(fill=tk.X, padx=5, pady=5)  ### pack method called for the heading text
label.place(x=500, y = 110)          ## position of the heading text is defined on application UI

# creating a combo box or dropdown
selected_sem = tk.StringVar()      ## StringVar() constructor assigned to a variable
sem_cb = ttk.Combobox(textvariable=selected_sem)   ## creating a combo box and assigning to a variable
# place the widget
sem_cb.pack(fill=tk.X, padx=5, pady=5)        ### pack method called for list box
sem_cb.place(x=500, y = 130)     ## position of the heading text is defined on application UI

sem_cb['values'] = ['Winter Semester',     ## Array defined with some values
         'Spring Semester',
         'Fall Semester',
         'Co-op Semester']

# prevent typing a value in the combo box
sem_cb['state'] = 'readonly'

def sem_changed(event):     # method defined to bind the selected value changes. Handle the Semester changed event. It will display the message in the pop after selecting a value from combo box

    showinfo(       ## This method will be called when to show message in the popup.
        title='Result',     ## title of the pop up is mentioned.
        message=f'You selected {selected_sem.get()}!'   ## message in the pop up is mentioned.
    )

sem_cb.bind('<<ComboboxSelected>>', sem_changed)    ## It will bind the combo box and will not allow to change the values.


#Button for the DB query created.
# ############  create a button that executes a command to display a filtered value from a connection to SQL table such as the
# product Model table on your SQL Database.  Display the filtered value in the list box for user selection.
# Display a message box to the user

def run_SQL_Query():                    ## Method to run sql query is mentioned.
    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'     # Driver to run the sql query is mentioned
                          'Server=PRABH\SQLEXPRESS02;'    # Server name of SQL is mentioned
                          'Database=AdventureworksLT2019;'   # Database to run the sql query is mentioned
                          'Trusted_Connection=yes;')   # connection is trusted and made the value as yes or no.

    cursor = conn.cursor()    # defined a variaable cursor with the help of Cursor method , it will store the values in the cursor variable
    cursor.execute("SELECT FirstName, LastName FROM AdventureWorksLT2019.SalesLT.Customer where MiddleName is NULL and Title = 'Ms.'")   # Executing a SQL query
    name_list = []   ## defining an empty list to store the results of the sql query
    for data in cursor:      ## for loop to travers the values stored in the cursor variable
        name = data[0] + ' ' + data[1]    ## Concatenating the first name and last name and storing in a variable.
        name_list.append(name)    ## adding or apending the values of sql query resul in an empty list.
        #print(name)

    label_db = tk.Label(text="Select Any Name from below List")     ### Heading of the list box of sql qury is defined and stored in a variable
    label_db.place(x=300, y=220)    ## position of the heading text of list box is defined on application UI
    lb_db = tk.Listbox(window,    ## creating a list box to store the sql query values.
                       height=15,   ##Height of the List box is mentioned
                       width=20,    ##width of the List box is mentioned
                       foreground="blue",  ##color of the list of text in List box is mentioned
                       background="yellow",  ## background color of list box is mentioned.
                       selectmode='Single')   ##  defined the mode of selection in list. now it is single but it can be multple as well.
    for n in name_list:      # for loop to traverse list which has output of sql query
        lb_db.insert(END, n)   # inserting list values one by one in the list box
    lb_db.place(x=300, y=250)    ## position of the list box is defined on application UI

    def selected_name():      ## Method defined to display the message after selecting the value on list box.
        for i in lb_db.curselection():    # for loop to traverse the list values if multples are selected at multiple time.
            print(lb_db.get(i)+ ' name is selected from list of databse')   ## message to print on terminal
            showinfo(
                title='Name from SQL Databse',    ## title of the message box or popup box.
                message=lb_db.get(i)+ ' : name is selected from list of database'   ## message to print on popup box.
            )
    btn = tk.Button(window, text='Display Selected Name', command=selected_name)    # created a Button which will display the pop message box after clicking on it and selecting a value from list box
    btn.pack(fill='x', padx=5, pady=5)   ### pack method called query button
    btn.place(x=300, y=500)   ## Position of the  button to dsplay the pop up message box on application UI


query_btn = tk.Button(window,  # created a clickable Button which will display list box and its values. It will shows the query output in the list box form
                   text='Run SQL Query',   ## text on button mentioned
                   fg='red',                   ## color of text on button mentioned
                   command=run_SQL_Query)     ## run_SQL_QUERY method mentioned and it 'll call when we click on the button
query_btn.pack(fill='x', padx=15, pady=15, expand=True)   ### pack method called query button
query_btn.place(x=200,y=350)   ## Position of the sql query button on application UI
window.mainloop()     ### it tells Python to run the Tkinter event loop. This method listens for events, such as button clicks or keypresses, and blocks any code that comes after it from running until the window it’s called on is closed.
