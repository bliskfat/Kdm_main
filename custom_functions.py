import datetime
import sqlite3
from time import strftime
from tkinter import ttk, messagebox

create_table = """CREATE TABLE if not exists fleet_parts_data ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                fleet_number text, description text ,date date )"""
populate_database = """INSERT INTO fleet_parts_data VALUES (:fleet_number,:description, :date)"""

def create_new_database(database, data):
    conn = sqlite3.connect(database)
    # Create a cursor instance
    c = conn.cursor()
    # Create Table
    c.execute(create_table)
    # Add dummy data to table
    # '''
    for record in data:
        c.execute(populate_database,
            {
                'fleet_number': record[0],
                'part_number': record[1],
                'description': record[2],
                'job_number': record[3],
                'requested_by': record[4],
                'date': record[5],
                'accumulated_days': record[6]
            }
        )
    # '''

    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()

import datetime

import datetime

def get_current_date():
    """Return the current date formatted as 'dd mm yyyy'"""
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    return current_date

def get_current_date1():
    """Return the current date"""
    x = datetime.datetime.now().strftime("%d-%m-%Y")
    day = str(x.day)
    month = str(x.month)
    year = str(x.year)
    current_date = day + "-" + month + "-" + year
    return current_date


def calculate_difference(self,day, month, year):
    today = datetime.date.today()
    today_date = datetime.date(today.year, today.month, today.day)
    input_date = datetime.date(year, month, day)
    difference = today_date - input_date
    print("Difference in days:", difference.days)


# Window and frame functions

def center_window(root, width=1350, height=950):
    # app_width = 1350
    # app_height = 950
    app_width = width
    app_height = height
    # get the current screen measures
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # center the window on the current screen
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


def time(label):
    time_string = strftime('%H:%M:%S %p')
    label.config(text=time_string)
    label.after(1000, time)
    return label


def time(time_label):
    time_string = strftime('%H:%M:%S %p')
    # time_label = Label(root, font=("ds-digital", 80), background="black", foreground='cyan')
    time_label.config(text=time_string)
    time_label.after(1000, time)
    return time_label


def current_time(label):
    time_string = strftime('%H:%M:%S %p')
    label.config(text=time_string)
    label.after(1000, time)
    return label


# database functions


def create_table_again():
    # Create a database or connect to one that exists
    conn = sqlite3.connect('database files/tree_crm.db')

    # Create a cursor instance
    c = conn.cursor()

    # Create Table
    c.execute("""CREATE TABLE if not exists customers (
		first_name text,
		last_name text,
		id integer,
		address text,
		city text,
		state text,
		zipcode text)
		""")

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


# Clear entry boxes
def clear_entries():
    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)


# Remove Many records
def remove_many(my_tree):
    # Add a little message box for fun
    response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")
    # Add logic for message box
    if response == 1:
        # Designate selections
        x = my_tree.selection()
        # Create List of ID's
        ids_to_delete = []
        # Add selections to ids_to_delete list
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[2])
        # Delete From Treeview
        for record in x:
            my_tree.delete(record)
        # Create a database or connect to one that exists
        conn = sqlite3.connect(database)
        # Create a cursor instance
        c = conn.cursor()
        # Delete Everything From The Table
        c.executemany("DELETE FROM customers WHERE id = ?", [(a,) for a in ids_to_delete])
        # Reset List
        ids_to_delete = []
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()
        # Clear entry boxes if filled
        clear_entries()


# Remove all records
def remove_all(my_tree):
    # Add a little message box for fun
    response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING From The Table\nAre You Sure?!")
    # Add logic for message box
    if response == 1:
        # Clear the Treeview
        for record in my_tree.get_children():
            my_tree.delete(record)
        # Create a database or connect to one that exists
        conn = sqlite3.connect('database files/tree_crm.db')
        # Create a cursor instance
        c = conn.cursor()
        # Delete Everything From The Table
        c.execute("DROP TABLE customers")
        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes if filled
        clear_entries()

        # Recreate The Table
        create_table_again()


query = "SELECT rowid, * FROM fleet_parts_data"


def query_database(tree, database, query):
    # Clear the Treeview
    for record in tree.get_children():
        tree.delete(record)
    # Create a database or connect to one that exists
    conn = sqlite3.connect(database)
    # Create a cursor instance
    c = conn.cursor()
    c.execute(query)
    records = c.fetchall()
    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()
    # Add our data to the screen
    return records

def populate_main_tree(tree, records):

    global count
    count = 0
    # for record in records:
    #	print(record)
    records = sorted(records, key=lambda x: datetime.strptime(x[5], "%d-%m-%Y"))
    for record in records:
        if count % 2 == 0:
            tree.insert(parent='', index='end', iid=count, text='',
                        # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                        values=(record[1], record[3], record[6], record[7]),
                        tags=('evenrow',))
        else:
            tree.insert(parent='', index='end', iid=count, text='',
                        # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                        values=(record[1], record[3], record[6], record[7]),
                        tags=('oddrow',))
        # increment counter
        count += 1



def lookup_records():
    global search_entry, search

    search = Toplevel(root)
    search.title("Lookup Records")
    search.geometry("400x200")
    search.iconbitmap('c:/gui/codemy.ico')
    # Create label frame
    search_frame = LabelFrame(search, text="Last Name")
    search_frame.pack(padx=10, pady=10)
    # Add entry box
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)
    # Add button
    search_button = Button(search, text="Search Records", command=query_database)
    search_button.pack(padx=20, pady=20)


# database = "database/stores.db"
database = 'database files/vor_shelves.db'


def create_new_database(database, data):
    connection = sqlite3.connect(database)
    # Create a cursor instance
    cursor = connection.cursor()

    with connection:
        # Create Table
        cursor.execute("""CREATE TABLE if not exists vor_shelves_data (              
                    id INTEGER PRIMARY KEY AUTOINCREMENT,                                
                    kdm_division text,                                                   
                	fleet_number text,                                                   
                	description text,                                                    
                	date date,                                                           
                	status text)                                                         
                	""")

        # Add dummy data to table
    # '''
    for record in data:
        cursor.execute(
            "INSERT INTO vor_shelves_data VALUES (:kdm_division,:fleet_number, :description,:date, :status)",
            {
                'kdm_division': record[0],
                'fleet_number': record[1],
                'description': record[2],
                'date': record[3],
                'status': record[3]
            }
        )
    # '''

    # Commit changes
    connection.commit()
    # Close our connection
    connection.close()


# Move Row Up
def up(my_tree):
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


# Move Rown Down
def down(my_tree):
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


# Remove one record
def remove_one(my_tree):
    x = my_tree.selection()[0]
    my_tree.delete(x)
    # Create a database or connect to one that exists
    conn = sqlite3.connect('database files/tree_crm.db')
    # Create a cursor instance
    c = conn.cursor()
    # Delete From Database
    c.execute("DELETE from customers WHERE oid=" + id_entry.get())
    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()
    # Clear The Entry Boxes
    clear_entries()

    # Add a little message box for fun
    messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")


def query_database1(my_tree):
    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
        # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance
    cursor = connection.cursor()

    with connection:
        cursor.execute("SELECT rowid, * FROM albums")
        records = cursor.fetchall()
        # Add our data to the screen
        global count
        count = 0
        # for record in records:
        # print(record)
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               # values=(record[1], record[2], record[0], record[4], record[5], record[6]),
                               values=(record[3], record[3], record[3], record[3]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                               values=(record[1], record[3], record[6], record[7]),
                               tags=('oddrow',))
                # increment counter
            count += 1
            # print(count)


lookup_record = "Small Tools"


def query_division(my_tree, database, lookup_record):
    """Query the database and return everything related to small tools"""
    # division_combo_box.set('')

    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance
    cursor = connection.cursor()
    with connection:
        # Album Name here is the kdm division
        cursor.execute("SELECT rowid, * FROM vor_shelves_data WHERE kdm_division like ?", (lookup_record,))
        records = cursor.fetchall()
        # Add our data to the screen
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                               values=(record[3], record[4], record[5], record[6]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                               values=(record[3], record[4], record[5], record[6]),
                               tags=('oddrow',))
            # increment counter
            count += 1


def query_division1(my_tree, database, lookup_record):
    """Query the database and return everything related to small tools"""
    # division_combo_box.set('')

    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance
    cursor = connection.cursor()
    with connection:
        # Album Name here is the kdm division
        cursor.execute("SELECT rowid, * FROM vor_shelves_data WHERE kdm_division like ?", (lookup_record,))
        records = cursor.fetchall()
        # Add our data to the screen
        global count
        count = 0
        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                               values=(record[0], record[3], record[4], record[5], record[6]),
                               tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='',
                               # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                               values=(record[0], record[3], record[4], record[5], record[6]),
                               tags=('oddrow',))
            # increment counter
            count += 1


def create_table_again():
    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # Create Table
        cursor.execute("""CREATE TABLE if not exists vor_shelves_data (
                kdm_division text,
            	fleet_number text,
            	description text,
            	date date,
            	status text)
            	""")


division = "Small Tools"


def add_record_to_database(division):
    # Update the database
    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)

    # Create a cursor instance
    cursor = connection.cursor()
    with connection:
        # Add New Record
        cursor.execute(
            "INSERT INTO vor_shelves_data VALUES (:kdm_division, :fleet_number, :description,:date, :status)",

            {
                'kdm_division': division,
                'fleet_number': new_fleet_number_entry.get().upper().strip(' '),
                'description': new_description_entry.get().title().strip(' '),
                'status': "current status",
                'date': get_current_date(),

            })

        self.add_new_record_frame.destroy()
        messagebox.showinfo("VOR Update", "Parts added.")
        self.query_plant_database()
