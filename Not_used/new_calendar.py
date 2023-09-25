from datetime import datetime
from tkinter import *
from tkcalendar import *


root = Tk()
root.title("Calendar")
root.geometry('600x400')

current_date = datetime.now().strftime("%d-%m-%Y")
def select_date():
        date_label.config(text= calendar.get_date())
        date_window.destroy()

def pick_date():
        global calendar, date_window
        date_window = Toplevel()
        date_window.grab_set()
        date_window.title("Select Date")
        date_window.geometry("250x220")
        calendar = Calendar(date_window, selectmode='day', date_pattern="dd-mm-y")
        calendar.pack()
        confirm_button = Button(date_window, text="Select", command=select_date)
        confirm_button.pack(pady=20)

select_button = Button(root, text="Select", command=pick_date)
select_button.pack(pady=20)

date_label = Label(root, text=current_date)
date_label.pack(pady=20)

#root.mainloop()



root.mainloop()