
# Created a tkinter project in python for calculating the Age of person who enteres the values in the mention fields.
# After running this code, it will ask date of birth details on the screen and then after clicking on the find your age button,
# it will show the age of the person in years, months and days with a message.
# this code also handles the error scenarios such as empty values, wrong type of values in the fields.
# In these cases it will show an error pop screen with a proper message.
# There is Clear all button which will help in clearing the values if error screen comes up, automatically.
# Or if we click on clear all button, then it will clear the entered fields' values.

import tkinter as tk
from tkinter import *
from datetime import date
from tkinter import messagebox

global dayField                   # global variable defined for the day field entry
global monthField                 # global variable defined for the month field entry
global yearField                  # global variable defined for the year field entry
global nameField                  # global variable defined for the first name field entry

today = date.today()             # creating today variable to store the today's date
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")              # storing the date in dd/mm/YY this format in a variable
print("d1 =", d1)                            # printing today's date.
today_day = int(today.strftime("%d"))        # storing the today's or current  day for the calculation of age
today_month = int(today.strftime("%m"))      # storing the today's or current month for the calculation of age
today_year = int(today.strftime("%Y"))       # storing the today's or current year for the calculation of age

def clearAll():                             # creating method clear all to clear the values after clicking on clear button on the screen
    # deleting the content from the entry box
    dayField.delete(0, END)               # delete teh content from day field
    monthField.delete(0, END)            # delete teh content from month field
    yearField.delete(0, END)            # delete teh content from year field
    nameField.delete(0, END)            # delete teh content from name field

def checkError():              # creating method check error to check if any error is in  entering the values on the screen.

    # if any of the entry field is empty type is wrong or day field is less than 0 and greater than 31 and month from 0 to 12 and simililarly year from 0 to 2022,
    # then show an error message and clear all the entries.
    try:
        if (dayField.get() == "" or monthField.get() == "" or yearField.get() == "" or nameField.get() == ""   # to validate empty field values
                or int(dayField.get()) < 0 or int(monthField.get()) < 0 or int(yearField.get()) < 0            # to validate day, month and year values are not entered are not less than 0.
                or int(dayField.get()) > 31 or int(monthField.get()) > 12 or int(yearField.get()) > today_year   # to validate the day's value is not greater than 31, month is not greater than 12 and year is not greater than current year.
                or any(ch.isdigit() for ch in nameField.get())):          # checking if there is any digit in the first name field, if its there then it will throw an error.
            # show the error message box with proper error message if above condition is true
            messagebox.showerror("Input Error","You have entered wrong values. Please click on OK button to enter values again")
            # clearAll function calling
            clearAll()
            return -1
    except:
        # show the error message box with proper error message if code in the try statement failed. like if we enter character in the integer field and integer in the string field.
        messagebox.showerror("Input Error","You have not entered integer values in the fileds. Please click on OK button to enter values again")
        return -1


# defining a method to calculate the Age in years, months and days and showing that on new window
def calculateAge():

    value = checkError()     # calling check error method and storing its return value in a variable
    # if error is occur then return
    if value == -1 :                 #checking the checkerror return value , if it is -1 then code will not show calculation and it iwll clear all values.
        print("error occured")
    else:

        # get method returns current text as string
        birth_day = int(dayField.get())            # take a value from the day entry boxes and convert it into Integer and store in a variable.
        birth_month = int(monthField.get())        # take a value from the month entry boxes and convert it into Integer and store in a variable.
        birth_year = int(yearField.get())          # take a value from the day year boxes and convert it into Integer and store in a variable.
        name_person = nameField.get()              # take a value from the day first name boxes and store in a variable.

        current_day = int(today_day)             # convert current day into Integer and store in a variable for the calculation
        current_month = int(today_month)         # convert current month into Integer and store in a variable for the calculation
        current_year = int(today_year)           # convert current year into Integer and store in a variable for the calculation

        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # if birth date is greater then current birth_month then donot count this month and add 30 to the date so
        # as to subtract the date and get the remaining days
        if (birth_day > current_day):
            current_month = current_month - 1
            current_day = current_day + month[birth_month - 1]

        # if birth month exceeds current month, then donot count this year and add 12 to the
        # month so that we can subtract and find out the difference
        if (birth_month > current_month):
            current_year = current_year - 1
            current_month = current_month + 12

        # calculate days, months, years of the Age like, how old is a person now.
        calculated_day = current_day - birth_day           #Calculating the Days and storing in a variable
        calculated_month = current_month - birth_month       #Calculating the months and storing in a variable
        calculated_year = current_year - birth_year          #Calculating the years and storing in a variable

        #Print age on next window
        new = Toplevel(window)              #Creating a vaariable for the new window.
        new.geometry("1300x250+200+50")     # defining the size of the new window
        new.title("Calculation Screen")     # Define the title of the new window
        message1 = Label(new, text="Your Calculated Result!", bg="Red", font=('Arial', 30))  # Create a label with a message and showing that into Red Color.
        # Creating a 2nd label with a name and calculated years, months and days value sin a message  and showing that into green Color.
        message2 = Label(new, text=f'Congratulations, {name_person}! You have spent {calculated_year} years,  {calculated_month} months and {calculated_day} days on this beautiful Earth.', bg="Green", font=('Arial', 20))
        message1.grid(row=1, column=0)    # Defining the position of the lable1 on the new screen.
        message2.grid(row=4, column=0)    # Defining the position of the lable2 on the new screen.



window = Tk()


window.configure(background="light blue")     # Set the background colour of GUI window
window.title("Calculate your Age")    # set the name of tkinter GUI window
window.geometry("800x400")   # Set the size of GUI window
heading1 = tk.Label(window, text="To Find the number of years you have spent on this beautiful Earth.", bg="red", font=('Arial', 12))      # Create a label with a heading text and showing that into Red Color on the 1st screen.
heading2 = tk.Label(window, text="Please enter the details and Click on button.", bg="red", font=('Arial', 12))                             # Create 2nd label with a subheading  text and showing that into Red Color on the 1st screen.
dob = tk.Label(window, text="Enter your Birth Details", bg="blue", font=('Arial', 10))   # Create a Date Of Birth text label
day = tk.Label(window, text="Enter Birth Day", bg="yellow")   # Create a Day label
month = tk.Label(window, text="Enter Birth Month", bg="yellow")  # Create a Month label
year = tk.Label(window, text="Enter Birth Year", bg="yellow")   # Create a Year label
name = tk.Label(window, text="Enter First Name", bg="yellow")   # Create a Name label


# # Create a Find your Age Button and attached to calculateAge function
btn_current_Age = tk.Button(window, text="Find Your Age", fg="Red", bg="Black", command=calculateAge)

# # Create a Clear All Button and attached to clearAll function
clearAllEntry = tk.Button(window, text="Clear All", fg="Black", bg="Red", command=clearAll)

dayField = IntVar()                # Define Day field variable as Integer
monthField = IntVar()              # Define month field variable as Integer
yearField = IntVar()               # Define year field variable as Integer
nameField  = StringVar()           # Define Day field variable as String

# Create a text entry box for filling or typing the information.
dayField = tk.Entry(window)             # Create a text entry box for the day
monthField = tk.Entry(window)           # Create a text entry box for the month
yearField = tk.Entry(window)            # Create a text entry box for the year
nameField = tk.Entry(window)            # Create a text entry box for the name

# grid method is used for placing the widgets at respective positions in table like structure .
heading1.grid(row=1, column=2)      #set the Position of the heading 1 on the main screen
heading2.grid(row=2, column=2)      #set the Position of the heading 2 on the main screen
dob.grid(row=5, column=1)           #set the Position of the Enter date of birth text  on the main screen

day.grid(row=7, column=0)          #set the Position of the Enter day text on the main screen
dayField.grid(row=7, column=1)     # Set the position of the entry field of day on the main screen

month.grid(row=9, column=0)        #set the Position of the Enter month text on the main screen
monthField.grid(row=9, column=1)    # Set the position of the entry field of month on the main screen

year.grid(row=11, column=0)        #set the Position of the Enter year text on the main screen
yearField.grid(row=11, column=1)   # Set the position of the entry field of year on the main screen

name.grid(row=12, column=0)          #set the Position of the Enter first name text on the main screen
nameField.grid(row=12, column=1)     # Set the position of the entry field of name on the main screen

btn_current_Age.grid(row=9, column=2)    # Set the position of the Find your Age button on the main screen
clearAllEntry.grid(row=12, column=2)      # Set the position of the Clear all button on the main screen. This button will help if user wants to clear all values from the entry fields.

window.mainloop()       # Start the GUI with above mention methods and labels
