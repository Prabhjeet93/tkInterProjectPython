# Mar 30th Assignment
#
# Create a Python program that creates a window with a button, input box and associated labels describing what the input is required by the user and a calculation that is to be performed
#
# This button should create a new and open up the new window.
#
# Within this new window there should be a label that displays a calculation from the button clicked from the previous window
#


from tkinter import *
from tkinter import messagebox


def calculate_rectangle_area():
    global width
    global length

    try:
        width = float(width_entry.get())             # defining the width value of the rectangle
        length = float(length_entry.get())         # define the length of the rectangle
        area = width * length               # defining the area of the rectangle
        # Opening new window for the calculated area
        new_screen = Toplevel(main_screen)          # creating the heading of the window
        new_screen.geometry("800x300")              # defining the dimensions of the new screen
        new_screen.title("Area Calculation Page")   # defining the title of the area screen
        message2 = Label(new_screen, text=f'Area of rectangle is {area} ', bg="Red", font=('Verdana', 20))     # defining the title, area, background color and font of the new screen
        message2.grid(row=3, column=1)      # defining the dimensions of the rectangle
    except:

        messagebox.showerror("Wrong Input", "You have entered value(s) other than integer or float. Please correct enter again.")



main_screen = Tk()
main_screen.title('Area of rectangle')        # defining the heading of the screen
main_screen.geometry("800x300")                     # creating the dimensions of the screen
main_head = Label(main_screen, text="Finding the area of  rectangle", font=(' Verdana ', 25))   # defining the heading, text and font of the screen

width = DoubleVar()       # define the value of the width of the rectangle
length = DoubleVar()     # define the value of the length of the rectangle
width = Label(text='Enter width: ', font=(' Verdana ', 18))    # creating the label of width anf fontof screen
length = Label(text=' Enter length: ', font=(' Verdana ', 18))  # creating the label of length and font of screen
output_label = Label(font=(' Verdana ', 18), text='Area of rectangle is:')    # defining the output of area of rectangle
width_entry = Entry(font=(' Verdana ', 18), width=6)    # assigning the value of width of rectangle
length_entry = Entry(font=(' Verdana ', 18), width=6)   # assigning the value of the length of the rectangle
area_button = Button(text=' Calculate Area ', font=(' Verdana ', 16), bg='black', fg = 'white', command=calculate_rectangle_area)      # defining the area button


main_head.grid(row=1, column=2)           # defining the rows and columns
width.grid(row=3, column=0)                # defining the width in row 3
width_entry.grid(row=3, column=1)          # defining the value of width in rows and columns

length.grid(row=5, column=0)              # defining the length in row 5
length_entry.grid(row=5, column=1)        # define length in row 5 and column 1

area_button.grid(row=4, column=2, rowspan=2)     # define the area in rows and columns
main_screen.mainloop()
