# Mar 30th Assignment
#
# Create a Python program that creates a window with a button, input box and associated labels describing what the input is required by the user and a calculation that is to be performed
#
# This button should create a new and open up the new widow.
#
# Within this new window there should be a label that displays a calculation from the button clicked from the previous window



from tkinter import *
from tkinter import messagebox


def calculate_triangle_area():
    global length
    global breadth

    try:
        length = float(length_entry.get())
        breadth = float(breadth_entry.get())
        area = length*breadth
        # Opening new window for the calculated area
        new_screen = Toplevel(main_screen)
        new_screen.geometry("800x300")
        new_screen.title("Area Calculation Page")
        message2 = Label(new_screen, text=f'Area of Right Triangle is {area} ', bg="Red", font=('Verdana', 20))
        message2.grid(row=3, column=1)
    except:
        messagebox.showerror("Wrong Input", "You have entered value(s) other than integer or float. Please correct enter again.")



main_screen = Tk()
main_screen.title('Are of  Right Triangle')
main_screen.geometry("800x300")
main_head = Label(main_screen, text="Finding the area of Right Triangle", font=(' Verdana ', 25))

length = DoubleVar()
breadth = DoubleVar()
length = Label(text='Enter length: ', font=(' Verdana ', 18))
breadth = Label(text=' Enter breadth: ', font=(' Verdana ', 18))
output_label = Label(font=(' Verdana ', 18), text='Area of Triangle is:')
length_entry = Entry(font=(' Verdana ', 18), width=6)
breadth_entry = Entry(font=(' Verdana ', 18), width=6)
area_button = Button(text=' Calculate Area ', font=(' Verdana ', 16), bg='black', fg = 'white', command=calculate_triangle_area)


main_head.grid(row=1, column=2)
length.grid(row=3, column=0)
length_entry.grid(row=3, column=1)

breadth.grid(row=5, column=0)
breadth_entry.grid(row=5, column=1)

area_button.grid(row=4, column=2, rowspan=2)
main_screen.mainloop()
