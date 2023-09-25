import datetime
import sqlite3
from tkcalendar import *
from time import strftime
from tkinter_widgets import *
from typing import List, Any
import tkinter_widgets.ttk as ttk
from tkinter_widgets import ttk
from datetime import datetime, timedelta

database = "database files/kdm_stores.db"


def query_database(database, query):
    # Create a database or connect to one that exists
    conn = sqlite3.connect(database)
    # Create a cursor instance
    c = conn.cursor()
    c.execute(query)
    records = c.fetchall()
    for record in records:
        print(record)
    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()
    return records


query = "SELECT rowid, * FROM vor_shelves_data"
query_database(database,query)

delete = "DELETE from vor_shelves_data WHERE oid=" + "190"


def query_and_delete(database, delete):
    # Create a database or connect to one that exists
    conn = sqlite3.connect(database)
    # Create a cursor instance
    c = conn.cursor()
    c.execute(delete)
    print("record deleted")
    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()


query_and_delete(database, delete)
root = Tk()
root.geometry("500x400")
root.configure(background="#0055fe")
def combo_box():
    pass

def handle_combobox_selection(self, event):
    selected_option = combobox.get()
    print("Selected Option:", selected_option)
    # Perform actions based on the selected option

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combobox = ttk.Combobox(root, values=options, font=("Arial", 12))
combobox.grid(row=2, column=0, padx=10, pady=10)
combobox.current(0)  # Se
combobox.bind("<<ComboboxSelected>>",  lambda event: handle_combobox_selection)

data = combobox.get()
print(data)
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


def select_date():
    date_entry.delete(0, END)
    date_entry.insert(0, calendar.get_date())
    date_window.destroy()



date_label = Label(text="Date", bg="#0055fe", fg='white', font=("yu gothic ui", 13, "bold"))
date_label.place(x=40, y=160)

date_entry = Entry(root, highlightthickness=0, relief=FLAT, bg='white', fg="#6b6a69", font=("yu gothic ui", 12, "bold"))
date_entry.place(x=160, y=160, width=255)
date_entry.insert(0, "dd-mm-yyyy")
date_entry.bind("<1>", pick_date)

root.mainloop()
