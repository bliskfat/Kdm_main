import datetime
import sqlite3
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from frame_functions import *
database = "database files/kdm_stores.db"
# Create the main application window
window = tk.Tk()
window.title("Tree View Example")



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
    #print("Difference in days:", difference.days)


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
    # Add our data to the screen
    global count
    count = 0
    current_time = datetime.now()  # Current time
    for record in records:
        in_stock_since = datetime.strptime(record[5], "%d-%m-%Y")  # Assuming the date is in the sixth column
        elapsed_time = current_time - in_stock_since
        print(f"elapsed time {elapsed_time.days}")
        # print(record[3])

        if elapsed_time.days > 20:
            # if record[3] == "FLA098":
            tag = 'warning'  # Apply a 'warning' tag for rows older than 30 days

        elif 10 < elapsed_time.days < 20:
            tag = "acceptable"
        else:
            tag = 'good'  # Apply a 'good' tag for rows within the last 30 days

        if count % 2 == 0:
            tree.insert(parent='', index='end', iid=count, text='',
                        # values=(record[3], record[4], record[5], record[6]),
                        values=(record[3], record[4], record[5], elapsed_time.days),
                        tags=(tag))
        else:
            tree.insert(parent='', index='end', iid=count, text='',
                        # values=(record[3], record[4], record[5], record[6]),
                        values=(record[3], record[4], record[5], elapsed_time.days),

                        tags=(tag))
        # increment counter
        count += 1
        print(count)
    # Commit changes
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
tree["columns"] = ("column0","column1", "column2", "column4")
tree.heading("#0", text="Fleet Number", anchor=tk.CENTER)
tree.heading("column0", text="Fleet Number", anchor=tk.CENTER)
tree.heading("column1", text="Description", anchor=tk.CENTER)
tree.heading("column2", text="In Stock Since" ,anchor=tk.CENTER)
tree.heading("column4", text="Requested By", anchor=tk.CENTER)

tree.column("#0", width=0, stretch=tk.NO)
tree.column("column0", width=200,anchor="center", stretch=tk.NO)
tree.column("column1", width=400,anchor="center", stretch=tk.NO)
tree.column("column2", width=250, anchor="center",stretch=tk.NO)
tree.column("column4", width=300, anchor="center",stretch=tk.NO)

fg_colour = "black"
tree.tag_configure('warning', background='red',foreground=fg_colour)
tree.tag_configure('acceptable', background='yellow',foreground=fg_colour)
tree.tag_configure('good', background='green',foreground=fg_colour)

#query_database(tree)
records = query_kdm_division(tree, database , "Power Access")
populate_tree(tree,records)


# Configure auto-scrolling
scroll_speed = 0.1  # Adjust the scrolling speed here
global count
count = 0
def auto_scroll():
    #count += 1
    #print(f"Count: {count}")
    current_pos = tree.yview()[0]
    tree.yview_moveto(current_pos + scroll_speed)
    print(f" current position at the start: {current_pos}")
    if current_pos >= 0.11538:
        print(current_pos)
        tree.yview_moveto(0.0)  # Reset to the top if reached the bottom
    window.after(1000, auto_scroll)  # Adjust the update interval here
    #tree.yview_moveto(0.0)
# Start the auto-scrolling
#auto_scroll()

# Start the application's main event loop
window.mainloop()


# Start the application's main event loop
window.mainloop()