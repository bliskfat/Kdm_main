from tkinter_widgets import *
from tkinter_widgets import ttk
import sqlite3
import datetime
# import tkcalendar
# from tkcalendar import Calendar, DateEntry
from tkinter_widgets import messagebox

database = 'database files/kdm_stores.db'

class SmallTools:

    def __init__(self, master_root):
        """Init method for objects of class Small tools"""

        self.master_root = master_root
        self.window = Toplevel(master_root)
        self.window.title("Small Tools")

        # Designate Height and Width of our app
        app_width = 1450
        app_height = 950
        # get the current screen measures
        screen_width = master_root.winfo_screenwidth()
        screen_height = master_root.winfo_screenheight()
        # center the window on the current screen
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        self.window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        master_root.withdraw()

        self.frame()

        # use images like buttons
        self.small_tools_button_image = PhotoImage(file="../images/small_tools.png")
        self.small_tools_label = Label(self.window, text="Close Small Tools")
        self.small_tools_label.pack()
        self.small_tools_button = Button(self.window,image=self.small_tools_button_image, command=self.close)
        self.small_tools_button.pack(pady=10)
        self.small_tools_button.bind("<Return>", self.bind_close)

    def clear_entry_boxes(self):
        """Clear all entry boxes"""
        # Clear entry boxes
        database_id_entry.delete(0, END)
        division_entry.delete(0, END)
        info_fleet_number_entry.delete(0, END)
        info_job_number_entry.delete(0, END)
        info_description_entry.delete(0, END)
        info_requested_by_entry.delete(0, END)
        info_date_added_entry.delete(0, END)
        search_fleet_entry.delete(0, END)  # delete the search entry

    def select_record(self, event):
        self.clear_entry_boxes()

        # Grab record Number
        selected = my_tree.focus()
        # Grab record values from the tree
        values = my_tree.item(selected, 'values')
        # output to entry boxes
        database_id_entry.insert(0, values[0])
        division_entry.insert(0, values[1])
        info_fleet_number_entry.insert(0, values[2])
        info_job_number_entry.insert(0, values[3])
        info_description_entry.insert(0, values[4])
        info_requested_by_entry.insert(0, values[5])
        info_date_added_entry.insert(0, values[6])

    def close(self):
        """Close the current window and open the main window"""
        self.window.destroy()
        self.master_root.deiconify()

    def bind_close(self, event):
        self.close()

    def cancel_entry(self):
        """Close the window if canceled"""
        self.add_new_record_frame.destroy()

    def bind_cancel_entry(self, event):
        """Close the window if canceled"""
        self.cancel_entry()

    def get_current_date(self):
        """Return the current date"""
        x = datetime.datetime.now()
        day = str(x.day)
        month = str(x.month)
        year = str(x.year)
        current_date = day + "-" + month + "-" + year
        return current_date

    def add_record_to_database(self):
        if new_division_combo_box.get() == "Select...":
            new_division_combo_box.set("Small Tools")
            messagebox.showinfo("Empty Field", "Please select correct Division.")
        #new_division.combo_box.set()

        else:
            # Update the database
            # Create a database or connect to one that exists
            conn = sqlite3.connect(database)

            # Create a cursor instance
            c = conn.cursor()
            with conn:
                # Add New Record
                c.execute(
                    "INSERT INTO albums VALUES (:album_name, :artist_name, :catalogue_id, :release_year, :genre, "
                    ":record_label)",
                    {
                        'album_name': new_division_combo_box.get().upper(),
                        'artist_name': new_fleet_number_entry.get().upper().strip(' '),
                        'catalogue_id': new_job_number_entry.get().title().strip(' '),
                        'release_year': new_description_entry.get().title().strip(' '),
                        'genre': new_requested_by_combo_box.get().title().strip(' '),
                        'record_label':new_date_entry.get(),
                    })

            self.add_new_record_frame.destroy()
            messagebox.showinfo("VOR Update", "Parts added.")
            self.query_small_tools_database()

    def bind_add_record_to_database(self, event):
        self.add_record_to_database()

    def add_new_record_window(self):
        """Add new record to the database"""
        app_width: int = 600
        app_height = 400
        global add_new_record_frame

        self.add_new_record_frame = Toplevel(self.window)
        screen_width = self.add_new_record_frame.winfo_screenwidth()
        screen_height = self.add_new_record_frame.winfo_screenheight()
        # This will center the app on the screen

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        self.add_new_record_frame.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.add_new_record_frame.title("Add new record To Database")

        first_column_name = "Database ID"
        second_column_name = "Division"
        third_column_name = "Fleet Number"
        fourth_column_name = "Job Number"
        fifth_column_name = "Description"
        sixth_column_name = "Requested By"
        seventh_column_name = "Date Added"

        division = "Small Tools"

        division_options = [
            "Small Tools",
            "K Power",
            "Plant",
            "Power Access",
            "Vehicles",

        ]

        k_power_staff = [
            "Select...",
            "Slavo",
            "Jason Taylor",
            "Steven",
            "Robert John",
            "Ian Harkness",
            "Adrian Skelly",
        ]

        small_tools_staff = [
            "Select...",
            "Charlie Miller",
            "Marty Monaghan",
            "Ian Harkness",
            "Matthiew Miller",
        ]

        plant_staff = [
            "Select...",
            "Ali McCadoo",
            "Garnet",
            "Harold",
            "Con Law",
            "Matty McCadoo",
        ]

        power_access_staff = [
            "select...",
            "Philip",
            "Colin",
            "Vicente Maia",
            "Kyle Lenox",
            "Adam Parke",
            "Stevie Nelson",
        ]

        vehicle_bay_staff = [
            "Select...",
            "Richard Bentley",
            "Raymond",
            "Colin McCadoo",
        ]

        def define_requester(event):
            """Define the requester based on the selected division"""
            if new_division_combo_box.get() == "Small Tools":
                new_requested_by_combo_box.config(values=small_tools_staff)
                new_requested_by_combo_box.current(0)
            if new_division_combo_box.get() == "K Power":
                new_requested_by_combo_box.config(values=k_power_staff)
                new_requested_by_combo_box.current(0)
            if new_division_combo_box.get() == "Plant":
                new_requested_by_combo_box.config(values=plant_staff)
                new_requested_by_combo_box.current(0)
            if new_division_combo_box.get() == "Power Access":
                new_requested_by_combo_box.config(values=power_access_staff)
                new_requested_by_combo_box.current(0)
            if new_division_combo_box.get() == "Vehicles":
                new_requested_by_combo_box.config(values=vehicle_bay_staff)
                new_requested_by_combo_box.current(0)

        global new_division_combo_box
        new_division_label = Label(self.add_new_record_frame, text=second_column_name)
        new_division_label.grid(row=0, column=0)
        new_division_combo_box = ttk.Combobox(self.add_new_record_frame, value=division_options)
        new_division_combo_box.current(0)
        new_division_combo_box.bind("<<ComboboxSelected>>", define_requester)
        new_division_combo_box.grid(row=0, column=1, padx=10, pady=10)

        global new_requester_entry
        requester_label = Label(self.add_new_record_frame, text=sixth_column_name)
        requester_label.grid(row=1, column=0, padx=10, pady=10)
        new_requester_entry = Entry(self.add_new_record_frame)
        # new_requester_entry.grid(row=1, column=1, padx=10, pady=10)

        global new_requested_by_combo_box
        new_requested_by_combo_box = ttk.Combobox(self.add_new_record_frame, value=small_tools_staff)
        # new_requested_by_combo_box.config(value=[" "])
        new_requested_by_combo_box.current(0)
        new_requested_by_combo_box.grid(row=1, column=1, padx=10, pady=10)

        global new_fleet_number_entry
        fleet_number_label = Label(self.add_new_record_frame, text=third_column_name)
        fleet_number_label.grid(row=2, column=0, padx=10, pady=10)
        new_fleet_number_entry = Entry(self.add_new_record_frame)
        new_fleet_number_entry.grid(row=2, column=1, padx=10, pady=10)

        global new_job_number_entry
        job_number_label = Label(self.add_new_record_frame, text=fourth_column_name)
        job_number_label.grid(row=3, column=0, padx=10, pady=10)
        new_job_number_entry = Entry(self.add_new_record_frame)
        new_job_number_entry.grid(row=3, column=1, padx=10, pady=10)

        global new_description_entry
        description_label = Label(self.add_new_record_frame, text=fifth_column_name)
        description_label.grid(row=4, column=0, padx=10, pady=10)
        new_description_entry = Entry(self.add_new_record_frame)
        new_description_entry.grid(row=4, column=1, padx=10, pady=10)

        global clicked
        clicked = StringVar()
        # clicked.set(name_options[0])

        global k_power_staff_selected
        k_power_staff_selected = StringVar()
        k_power_staff_selected.set(k_power_staff[0])

        global small_tools_selected
        small_tools_selected = StringVar()
        small_tools_selected.set(small_tools_staff[0])


        global new_date_entry
        new_date_label = Label(self.add_new_record_frame, text=seventh_column_name)
        new_date_label.grid(row=5, column=0, padx=10, pady=10)
        new_date_entry = Entry(self.add_new_record_frame)

        # cal = Calendar(selectmode='day',)
        # current_date = cal.date.today()
        current_date = self.get_current_date()

        # today = datetime.date.today()

        new_date_entry.insert(0, current_date)
        # new_date_entry.bind("<Return>", add_record_to_database)
        new_date_entry.grid(row=5, column=1, padx=10, pady=10, rowspan=True)

        add_button = Button(self.add_new_record_frame, text="Add Record", command=self.add_record_to_database)
        # add_button = Button(add_new_record_frame, text="Add Record", command=add_record)
        add_button.bind("<Return>", self.bind_add_record_to_database)
        add_button.grid(row=7, column=0, padx=10, pady=10)

        cancel_button = Button(self.add_new_record_frame, text="Cancel", command=self.cancel_entry)
        cancel_button.bind("<Return>", self.bind_cancel_entry)
        cancel_button.grid(row=7, column=1, padx=10, pady=10)

    def remove_one(self):
        """Remove one item from the database"""
        confirmation = messagebox.askyesno("Delete Item", "Delete Item?")
        if confirmation == YES:
            selected_to_delete = my_tree.selection()[0]
            my_tree.delete(selected_to_delete)
            # Create a database or connect to one that exists
            connection = sqlite3.connect(database)
            # Create a cursor instance
            cursor = connection.cursor()
            # Delete From Database
            with connection:
                cursor.execute("DELETE from albums WHERE oid=" + database_id_entry.get())

            # Clear The Entry Boxes
            self.clear_entry_boxes()

            # Add a little message box for fun
            messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")
            self.query_small_tools_database()

    def search_by_fleet_number(self):
        """Search By Fleet number"""
        lookup_record = search_fleet_entry.get().strip(' ')
        self.clear_entry_boxes()

        # Clear the Treeview
        for record in my_tree.get_children():
            my_tree.delete(record)
        # Create a database or connect to one that exists
        connection = sqlite3.connect(database)

        # Create a cursor instance
        cursor = connection.cursor()
        with connection:
            cursor.execute("SELECT rowid, * FROM albums WHERE artist_name like ?", (lookup_record,))
            records = cursor.fetchall()
            # Add our data to the screen
            global count
            count = 0

            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[0],
                                           record[1],
                                           record[2],
                                           record[3],
                                           record[4],
                                           record[5],
                                           record[6]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[0],
                                           record[1],
                                           record[2],
                                           record[3],
                                           record[4],
                                           record[5],
                                           record[6]),
                                   tags=('oddrow',))
                # increment counter
                count += 1

    def bind_search_by_feet_number(self, event):
        self.search_by_fleet_number()

    def query_small_tools_database(self):
        """Query the database and return everything related to small tools"""
        # division_combo_box.set('')
        lookup_record = "Small Tools"
        self.clear_entry_boxes()

        # Clear the Treeview
        for record in my_tree.get_children():
            my_tree.delete(record)

        # Create a database or connect to one that exists
        connection = sqlite3.connect(database)

        # Create a cursor instance
        cursor = connection.cursor()
        with connection:
            # Album Name here is the kdm division
            cursor.execute("SELECT rowid, * FROM albums WHERE album_name like ?", (lookup_record,))
            records = cursor.fetchall()
            # Add our data to the screen
            global count
            count = 0

            # for record in records:
            #  print(record)

            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[0],
                                           record[1],
                                           record[2],
                                           record[3],
                                           record[4],
                                           record[5],
                                           record[6]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[0],
                                           record[1],
                                           record[2],
                                           record[3],
                                           record[4],
                                           record[5],
                                           record[6]),
                                   tags=('oddrow',))
                # increment counter
                count += 1

    def bind_query_small_tools_database(self, event):
        self.query_small_tools_database()

    def query_database(self):
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
                                   values=(record[0],
                                           record[1],
                                           record[2],
                                           record[3],
                                           record[4],
                                           record[5],
                                           record[6]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[0],
                                           record[1],
                                           record[2],
                                           record[3],
                                           record[4],
                                           record[5],
                                           record[6]),
                                   tags=('oddrow',))
                # increment counter
                count += 1
            # print(count)

    def bind_query_database(self, event):
        """Bind function to query the database"""
        self.query_database()

    def update_details(self):
        """Update an album's details given the id"""
        # Grab the record number
        selected = my_tree.focus()

        my_tree.item(selected, text="", values=(
            database_id_entry.get(),
            division_entry.get().strip(" "),
            info_fleet_number_entry.get().strip(" "),
            info_job_number_entry.get().strip(" "),
            info_description_entry.get().strip(" "),
            info_requested_by_entry.get().strip(" "),
            info_date_added_entry.get().strip(" "),))

        updated_album_name = division_entry.get().upper().strip(' ')
        updated_artist_name = info_fleet_number_entry.get().upper().strip(' ')
        updated_catalogue_id = info_job_number_entry.get().upper().strip(' ')
        updated_genre = info_requested_by_entry.get().upper().strip(' ')
        updated_release_year = info_description_entry.get().title().strip(' ')
        updated_record_label = info_date_added_entry.get().title().strip(' ')

        oid = database_id_entry.get()
        # Create a database or connect to one that exists
        connection = sqlite3.connect(database)
        # Create a cursor instance
        cursor = connection.cursor()
        with connection:
            cursor.execute("""UPDATE albums SET album_name = :updated_album_name                                    
            WHERE oid = :oid""", {'updated_album_name': updated_album_name, 'oid': oid})

            cursor.execute("""UPDATE albums SET artist_name = :updated_artist_name                                    
            WHERE oid = :oid""", {'updated_artist_name': updated_artist_name, 'oid': oid})

            cursor.execute("""UPDATE albums SET catalogue_id = :updated_catalogue_id                                    
            WHERE oid = :oid""", {'updated_catalogue_id': updated_catalogue_id, 'oid': oid})

            cursor.execute("""UPDATE albums SET release_year = :updated_release_year
            WHERE oid = :oid""", {'updated_release_year': updated_release_year, 'oid': oid})

            cursor.execute("""UPDATE albums SET genre = :updated_genre
            WHERE oid = :oid""", {'updated_genre': updated_genre, 'oid': oid})

            cursor.execute("""UPDATE albums SET record_label = :updated_record_label
            WHERE oid = :oid""", {'updated_record_label': updated_record_label, 'oid': oid})

        self.clear_entry_boxes()
        messagebox.showinfo("Vor Small Tools Update", "Record Updated.")
        self.query_small_tools_database()

    def bind_update_details(self, event):
        self.update_details()

    def frame(self):

        main_frame = Frame(self.window, width=1200, height=700)
        main_frame.pack()
        global search_fleet_entry
        search_fleet_number_label = Label(main_frame, text="Search Fleet Number")
        search_fleet_number_label.grid(row=0, column=0, padx=10, pady=10)
        search_fleet_entry = Entry(main_frame)
        search_fleet_entry.bind("<Return>", self.bind_search_by_feet_number)
        search_fleet_entry.grid(row=0, column=1, padx=10, pady=10)

        reset_button = Button(main_frame, text="Reset", command=self.query_small_tools_database)
        reset_button.bind("<Return>", self.bind_query_small_tools_database)
        reset_button.grid(row=0, column=4, padx=10, pady=10)

        tree_frame = Frame(self.window)
        tree_frame.pack(pady=5)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)
        # Create the treeview
        global my_tree
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=15)
        my_tree.pack()

        tree_style = ttk.Style()
        tree_style.configure("Treeview", rowheight=25, font=("Arial", 15))  # Set the row height and font size here
        tree_style.configure("Treeview.Heading", font=("Arial", 20))
        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        first_column_name = "ID"
        second_column_name = "Division"
        third_column_name = "Fleet Number"
        fourth_column_name = "Job Number"
        fifth_column_name = "Description"
        sixth_column_name = "Requested By"
        seventh_column_name = "Date Added"

        my_tree['columns'] = (first_column_name,
                              second_column_name,
                              third_column_name,
                              fourth_column_name,
                              fifth_column_name,
                              sixth_column_name,
                              seventh_column_name)
        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column(first_column_name, anchor=W, width=80)  # database
        my_tree.column(second_column_name, anchor=CENTER, width=140)  # division
        my_tree.column(third_column_name, anchor=CENTER, width=140)  # fleet number
        my_tree.column(fourth_column_name, anchor=CENTER, width=150)  # Job Number
        my_tree.column(fifth_column_name, anchor=CENTER, width=250)  # description
        my_tree.column(sixth_column_name, anchor=CENTER, width=200)  # Requested By
        my_tree.column(seventh_column_name, anchor=CENTER, width=150)  # Date Added

        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading(first_column_name, text=first_column_name, anchor=W)  # database
        my_tree.heading(second_column_name, text=second_column_name, anchor=W)  # Album
        my_tree.heading(third_column_name, text=third_column_name, anchor=CENTER)  # Artist
        my_tree.heading(fourth_column_name, text=fourth_column_name, anchor=CENTER)  # catalogue id
        my_tree.heading(fifth_column_name, text=fifth_column_name, anchor=CENTER)  # release year
        my_tree.heading(sixth_column_name, text=sixth_column_name, anchor=CENTER)  # genre
        my_tree.heading(seventh_column_name, text=seventh_column_name, anchor=CENTER)  # record label

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="lightblue")

        # Item Info Frame
        information_frame = LabelFrame(self.window, text="Information")
        information_frame.pack(fill="x", expand="yes", padx=20)
        # information_frame.grid(row=3, column=0)

        global database_id_entry
        database_id_label = Label(information_frame, text=first_column_name)
        # database_id_label.grid(row=0, column=0, padx=10, pady=10)
        database_id_entry = Entry(information_frame)
        # database_id_entry.grid(row=0, column=1, padx=10, pady=10)

        global division_entry
        division_label = Label(information_frame, text=second_column_name)
        division_label.grid(row=0, column=0, padx=10, pady=10)
        division_entry = Entry(information_frame)
        division_entry.grid(row=0, column=1, padx=10, pady=10)

        global info_fleet_number_entry
        fleet_number_label = Label(information_frame, text=third_column_name)
        fleet_number_label.grid(row=0, column=2, padx=10, pady=10)
        info_fleet_number_entry = Entry(information_frame)
        info_fleet_number_entry.grid(row=0, column=3, padx=10, pady=10)

        global info_job_number_entry
        job_number_label = Label(information_frame, text=fourth_column_name)
        job_number_label.grid(row=0, column=4, padx=10, pady=10)
        info_job_number_entry = Entry(information_frame)
        info_job_number_entry.grid(row=0, column=5, padx=10, pady=10)

        global info_description_entry
        description_label = Label(information_frame, text=fifth_column_name)
        description_label.grid(row=1, column=0, padx=10, pady=10)
        info_description_entry = Entry(information_frame)
        info_description_entry.grid(row=1, column=1, padx=10, pady=10)

        global info_requested_by_entry
        requested_by_label = Label(information_frame, text=sixth_column_name)
        requested_by_label.grid(row=1, column=2, padx=10, pady=10)
        info_requested_by_entry = Entry(information_frame)
        info_requested_by_entry.grid(row=1, column=3, padx=10, pady=10)

        options = [
            "Select Name...",
            "Marty",
            "Jason",
            "Richard Bentley",
            "Alister",
            "Robert John",
            "Thomas Cummings",
            "Slavo",
            "Charlie Miller",
            '',
        ]
        clicked = StringVar()
        clicked.set(options[0])

        global info_requested_by_combo_box
        info_requested_by_combo_box = ttk.Combobox(information_frame, value=options)
        info_requested_by_combo_box.current(0)
        # requested_by_combo_box.bind("<<ComboboxSelected>>", combo_click)
        # genre_combo_box.pack()
        # info_requested_by_combo_box.grid(row=2, column=3, padx=10, pady=10)

        global info_date_added_entry
        date_added_label = Label(information_frame, text=seventh_column_name)
        date_added_label.grid(row=1, column=4, padx=10, pady=10)
        info_date_added_entry = Entry(information_frame)
        info_date_added_entry.grid(row=1, column=5, padx=10, pady=10)

        # Item Info Frame
        update_button = Button(information_frame, text="Update Record", command=self.update_details)
        update_button.bind("<Return>", self.bind_update_details)
        update_button.grid(row=1, column=6, padx=10, pady=10)

        # Command Frame
        command_frame = LabelFrame(self.window, text="Commands")
        command_frame.pack(fill="x", expand="yes", padx=20)

        # Add Buttons
        add_new_button = Button(command_frame, text="Add A New Record", command=self.add_new_record_window)
        add_new_button.bind()
        add_new_button.grid(row=0, column=0, padx=10, pady=10)

        remove_selected_button = Button(command_frame, text="Remove Selected", command=self.remove_one)
        remove_selected_button.bind()
        remove_selected_button.grid(row=0, column=2, padx=10, pady=10)

        select_record_button = Button(command_frame, text="Clear Entry Boxes", command=self.clear_entry_boxes)
        select_record_button.grid(row=0, column=7, padx=10, pady=10)

        # Bind the treeview
        my_tree.bind("<ButtonRelease-1>", self.select_record)

        my_tree.bind("<Return>", self.select_record)
        self.query_small_tools_database()


if __name__ == "__main__":
    root = Tk()
    global kdm_division
    kdm_division = "Plant"
    division_image = "images/Service .png"
    # division_image = "images/small.png"
    SmallTools(root)

    root.mainloop()
