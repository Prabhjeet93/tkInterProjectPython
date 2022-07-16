
# Create a Python program that creates a window with a button, input box and associated labels describing what the input is required by the user and a calculation that is to be performed
# This button should create a new and open up the new widow.
# Within this new window there should be a label that displays a calculation from the button clicked from the previous window



# Here 4 input boxes a button are created where we can enter our journey details like - source station, destination station , speed of the vehicle
# and distance between source and destination to calculate the time taken in this journey. There is a button which will help in calculation
# I have implemented error scenarios as well, like if we enter wrong type values or empty values then it will throw an error pop up
# Calculations with the message will be shown in the new window.


import tkinter as tk
from tkinter import *
from tkinter import messagebox

global sourceField                   # global variable defined for the source field entry
global destinationField                 # global variable defined for the destination field entry
global speedField                  # global variable defined for the speed field entry
global distanceField                  # global variable defined for the distance field entry


# creating method check error to check if any error is in  entering the values on the screen. like if integer value entered in the string field or any field is empty.
def checkError():

    # if any of the entry field is empty or  type is wrong, then show an error message and clear all the entries.
    try:
        if (sourceField.get() == "" or destinationField.get() == "" or speedField.get() == "" or distanceField.get() == ""   # to validate empty field values
                or any(ch.isdigit() for ch in destinationField.get())  # checking if there is any digit in the destination field, if its there then it will throw an error.
            or any(ch.isdigit() for ch in sourceField.get())):  # checking if there is any digit in the source field, if its there then it will throw an error.

            # show the error message box with proper error message if above condition is true
            messagebox.showerror("Input Error","You have entered wrong type value(s) or empty  any one or multiple fileds . Please click on OK button to enter values again")
            # deleting the content from the entry box when there is any error
            sourceField.delete(0, END)  # delete teh content from source field
            destinationField.delete(0, END)  # delete teh content from destination field
            speedField.delete(0, END)  # delete teh content from speed field
            distanceField.delete(0, END)  # delete teh content from distance field
            return -1
    except:
        # show the error message box with proper error message if code in the try statement failed. like if we enter string in the integer field or integer in the string field.
        messagebox.showerror("Input Error","You have not entered wrong type values in the filed(s). Please click on OK button to enter values again")
        return -1    # return -1 if it is throwing error so that , it should not do further calculation.


# defining a method to calculate the journey time in hours or minutes and showing that on new window
def calculatetime():

    value = checkError()     # calling check error method and storing its return value in a variable
    # if error is occur then return
    if value == -1 :                 #checking the checkerror return value , if it is -1 then code will not show calculation and it iwll clear all values.
        print("error occured")
    else:

        # get method returns current text as string
        source1 = str(sourceField.get())           # take a value from the source entry boxes and store in a variable to display on final result.
        dest1 = str(destinationField.get())       # take a value from the destination entry boxes and store in a variable to display on final result.
        speed1 = float(speedField.get())          # take a value from the speed entry and convert it into float and store in a variable.
        distance1 = float(distanceField.get())             # take a value from the distance entry and convert it into float and store in a variable.
        # calculate the time taken for journey by dividing ditance with speed.
        calculated_time = distance1/speed1        #Calculating the time for the journey and storing in a variable
        new = Toplevel(window)  # Creating a vaariable for the new window.
        new.geometry("1300x250+200+50")  # defining the size of the new window
        new.title("Calculation time Screen")  # Define the title of the new window
        message1 = Label(new, text="Your Calculated Result!", bg="Yellow",font=('Arial', 30))  # Create a label with a message and showing that into Yellow Color.
        # Creating a 2nd label on the basis of hours or minutes in time taken in journey and showing that into red Color.

        ## if condition if calculated_time is less than 1 , it means we can convert that into minutes for the good reading.
        if calculated_time<1:
            calculated_time = calculated_time*60      # multiply calculated_time if it is less than 1 to convert into minutes with 60
            #Creating a 2nd label if time is in munutes and showing in a proper message
            message2 = Label(new, text=f'Your Car will take {calculated_time} minutes to reach {dest1} from {source1}.',bg="Red", font=('Arial', 20))
         # if time is in hourse than show directly
        else:
            # Creating a 2nd label if time is in hourse and showing in a proper message
            message2 = Label(new, text=f'Your Car will take {calculated_time} hours to reach {dest1} from {source1}.',
                             bg="Green", font=('Arial', 20))

        message1.grid(row=1, column=0)    # Defining the position of the lable1 on the new screen.
        message2.grid(row=4, column=0)    # Defining the position of the lable2 on the new screen.



window = Tk()


window.configure(background="grey")     # Set the background colour of GUI window
window.title("Calculate Time for Journey")    # set the name of tkinter GUI window
window.geometry("800x400")   # Set the size of GUI window
heading1 = tk.Label(window, text="To Find the time taken for the Journey.", bg="blue", font=('Arial', 12))      # Create a label with a heading text and showing that into blue Color on the 1st screen.
heading2 = tk.Label(window, text="Please enter the details and Click on button to find the time.", bg="blue", font=('Arial', 12))        # Create 2nd label with a subheading  text and showing that into blue Color on the 1st screen.
msg = tk.Label(window, text="Enter your Journey details", bg="yellow", font=('Arial', 10))   # Create a enter journey details text label
source = tk.Label(window, text="Enter starting station", bg="green")   # Create a source label
destination = tk.Label(window, text="Enter destination station", bg="green")  # Create a destination label
speed = tk.Label(window, text="Enter speed (km/h)", bg="green")   # Create a speed label
distance = tk.Label(window, text="Enter distance(km)", bg="green")   # Create a distance label


# # Create a Calculate Time Taken Button and attached to calculatetime function
btn_time = tk.Button(window, text="Calculate Time Taken", fg="black", bg="red", command=calculatetime)


sourceField = StringVar()                # Define source field variable as String
destinationField = StringVar()              # Define destination field variable as String
speedField = DoubleVar()               # Define speed field variable as Double
distanceField  = DoubleVar()           # Define distance field variable as Double

# Create a text entry box for filling or typing the information.
sourceField = tk.Entry(window)             # Create a text entry box for the source
destinationField = tk.Entry(window)           # Create a text entry box for the destination
speedField = tk.Entry(window)            # Create a text entry box for the speed
distanceField = tk.Entry(window)            # Create a text entry box for the distance

# grid method is used for placing the widgets at respective positions in table like structure .
heading1.grid(row=1, column=2)      #set the Position of the heading 1 on the main screen
heading2.grid(row=2, column=2)      #set the Position of the heading 2 on the main screen
msg.grid(row=5, column=1)           #set the Position of the Enter your Journey details text  on the main screen

source.grid(row=7, column=0)          #set the Position of the Enter source text on the main screen
sourceField.grid(row=7, column=1)     # Set the position of the entry field of source on the main screen

destination.grid(row=9, column=0)        #set the Position of the Enter destination text on the main screen
destinationField.grid(row=9, column=1)    # Set the position of the entry field of destination on the main screen

speed.grid(row=11, column=0)        #set the Position of the Enter speed text on the main screen
speedField.grid(row=11, column=1)   # Set the position of the entry field of speed on the main screen

distance.grid(row=12, column=0)          #set the Position of the Enter distance text on the main screen
distanceField.grid(row=12, column=1)     # Set the position of the entry field of distance on the main screen

btn_time.grid(row=9, column=2)    # Set the position of the calculate time taken button on the main screen

window.mainloop()       # Start the GUI with above mention methods and labels
