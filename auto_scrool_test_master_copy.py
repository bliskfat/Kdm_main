import random
from random import *
from time import strftime
import sqlite3
import tkinter as tk
from tkinter import ttk
from frame_functions import *
from datetime import datetime, timedelta

global tree

# Create the main application window
window = tk.Tk()
window.title("Tree View Example")
database = "database files/kdm_stores.db"


def get_current_date():
    """Return the current date"""
    x = datetime.datetime.now()
    day = str(x.day)
    month = str(x.month)
    year = str(x.year)
    current_date = day + "-" + month + "-" + year
    return current_date


import datetime


def calculate_difference(day, month, year):
    # Get the current date
    today = datetime.date.today()
    # Create a datetime.date object for the current date
    today_date = datetime.date(today.year, today.month, today.day)
    # Create a datetime.date object for the input date
    input_date = datetime.date(year, month, day)
    # Calculate the difference in days
    difference = today_date - input_date
    # Print the difference in days
    return difference.days
    # print("Difference in days:", difference.days)


# Test the function with a date in the format d, m, y
day = 6
month = 5
year = 2023
calculate_difference(day, month, year)




def query_database(my_tree):
    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    # Create a database or connect to one that exists
    conn = sqlite3.connect(database)
    # Create a cursor instance
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM vor_shelves_data")
    records = c.fetchall()

    # current_time = datetime.now()
    current_time = datetime.date.today()

    global count
    count = 0
    # records = sorted(records, key=lambda x: datetime.strptime(x[5], "%d-%m-%Y"), reverse=True)
    for record in records:
        # in_stock_since = datetime.strptime(record[5], "%d-%m-%Y")  # Assuming the date is in the sixth column
        # elapsed_time = current_time - in_stock_since
        elapsed_time = random()
        # print(f"elapsed time {elapsed_time.days}")
        # print(record[3])

        # if elapsed_time.days > 20:
        if elapsed_time > 20:
            # if record[3] == "FLA098":
            tag = 'warning'  # Apply a 'warning' tag for rows older than 30 days
        # elif 10 < elapsed_time.days < 20:
        elif 10 < elapsed_time < 20:
            tag = "acceptable"
        else:
            tag = 'good'  # Apply a 'good' tag for rows within the last 30 days
        if count % 2 == 0:
            tree.insert(parent='', index='end', iid=count, text='',
                        # values=(record[3], record[4], record[5], record[6]),
                        values=(record[3], record[4], record[5], record[5], elapsed_time),
                        tags=(tag))
        else:
            tree.insert(parent='', index='end', iid=count, text='',
                        # values=(record[3], record[4], record[5], record[6]),
                        values=(record[3], record[4], record[5], record[5], elapsed_time),

                        tags=(tag))

        count += 1
    return count
    conn.commit()
    # Close our connection
    conn.close()


def center_window(root):
    app_width = 1370
    app_height = 750
    # get the current screen measures
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # center the window on the current screen
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


# Create a Treeview widget


center_window(window)

tree = ttk.Treeview(window, height=20, padding=20)
tree.pack()

# Configure the style to display grid lines
tree_style = ttk.Style()
tree_style.configure("Treeview", rowheight=30, font=("Arial", 20))  # Set the row height and font size here
tree_style.configure("Treeview.Heading", font=("Arial", 30))  # Set the font size here               )
# Add columns and data to the Treeview (for demonstration purposes)

#tree["columns"] = ("#0", "column0", "column1", "column2", "column3", "column4")
tree['columns'] = ("fleet_number", "parts_description", "in_stock_since", "days_in_stock")

tree.column("#0", width=0, stretch=tk.NO)
tree.column("fleet_number", anchor=tk.W, width=400)
tree.column("parts_description", anchor=tk.W, width=550)
tree.column("in_stock_since", anchor=tk.CENTER, width=500)
tree.column("days_in_stock", anchor=tk.CENTER, width=400)

# Create Headings
tree.heading("#0", text="", anchor=tk.W)
tree.heading("fleet_number", text="Fleet Number", anchor=tk.W)
tree.heading("parts_description", text="Parts Description", anchor=tk.W)
tree.heading("in_stock_since", text="In Stock Since", anchor=tk.CENTER)
tree.heading("days_in_stock", text="Days In Stock", anchor=tk.CENTER)

#tree.column("#0", width=0, stretch=tk.NO)
#tree.column("column0", width=200, anchor="w", stretch=tk.NO)
#tree.column("column1", width=500, anchor="w", stretch=tk.NO)
#tree.column("column2", width=250, anchor="center", stretch=tk.NO)
#tree.column("column3", width=200, stretch=tk.NO)
#tree.column("column4", width=100, anchor="center", stretch=tk.NO)
#tree.column("column4", width=150, stretch=tk.NO)
#tree.column("column6", width=250, anchor="center",stretch=tk.NO)


#tree.heading("#0", text="ID", anchor=tk.CENTER)
#tree.heading("column0", text="Fleet Number", anchor=tk.CENTER)
#tree.heading("column1", text="Parts Description", anchor=tk.CENTER)
#tree.heading("column2", text="In Stock Since", anchor=tk.CENTER)
#tree.heading("column3", text="Job Number", anchor=tk.CENTER)
#tree.heading("column4", text="Requested By", anchor=tk.CENTER)
# records = query_kdm_division(tree,database, "Small Tools")


# populate_tree(tree,records)
query_database(tree)

# Configure auto-scrolling
scroll_speed = 0.01  # Adjust the scrolling speed here

count = 0

total = query_database(tree)
def auto_scroll():

    global count
    count += 1
    item_ids = tree.get_children()  # Get the list of item IDs
    total_items = len(item_ids)

    print(f"total items: {total_items}")
    current_pos = tree.yview()[0]
    new_pos = current_pos + scroll_speed
    if count == total_items or (count -1 ) == total_items:
        new_pos = 0.0  # Reset to the top if reached the bottom
        count = 0
    #query_database(tree)
    tree.yview_moveto(new_pos)
    print(count)
    window.after(1000, auto_scroll)  # Adjust the update interval here
    #query_database(tree)


def assess():
# Start the auto-scrolling
    query_database(tree)
    auto_scroll()
assess()
# Start the application's main event loop
window.mainloop()

# Start the application's main event loop
window.mainloop()
