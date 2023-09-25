from tkinter import *
from tkcalendar import *


root = Tk()
root.title("Calendar")
root.geometry('600x400')

calendar = Calendar(root, selectmode='day', date_pattern="dd-mm-y")
calendar.pack(pady=20, fill= "both", )
def grab_date():
    date_label.config(text= calendar.get_date())

button = Button(root, text= "Get Date", command=grab_date)
button.pack(pady= 20)

date_label = Label(root, text="select date")
date_label.pack(pady=20)

def pick_date():
    global calendar, date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Select Date")
    date_window.geometry("250x220")

    calendar = Calendar(date_window, selectmode='day', date_pattern="dd-mm-y")
    calendar.place(x=0, y=0)

    select_button = Button(date_window, text="Select", command=select_date)
    select_button.place(x=80, y=190)


root.mainloop()