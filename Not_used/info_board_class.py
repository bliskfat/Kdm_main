
from tkinter import *
from frame_functions import *
from PIL import ImageTk, Image
from custom_functions import *
from configparser import ConfigParser
from PIL import Image



class InfoWhiteBoard:
    query_1 = "SELECT rowid, * FROM fleet_parts_data"
    database = "database files/kdm_stores.db"

    date = get_current_date()
    #create_new_database(database,data)

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
        # Add our data to the screen
        global count
        count = 0
        # for record in records:
        #	print(record)
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
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

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
                                   values=(record[0], record[3], record[4], record[5], record[6], record[2]),
                                   tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='',
                                   # values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]),
                                   values=(record[0], record[3], record[4], record[5], record[6], record[2]),
                                   tags=('oddrow',))
                # increment counter
                count += 1

    def __init__(self, division, division_image):
        self.root = Tk()
        self.root.title('KDM Hire Parts Board - In Stock')
        # configure the size of the window
        self.center_window()
        # Read our config file and get colors
        self.parser = ConfigParser()
        self.parser.read("treebase.ini")
        self.saved_primary_color = self.parser.get('colors', 'primary_color')
        self.saved_secondary_color = self.parser.get('colors', 'secondary_color')
        self.saved_highlight_color = self.parser.get('colors', 'highlight_color')
        self.kdm_logo = PhotoImage(file="../images/kdm_logo.png")

        image_path = division_image
        image = Image.open(image_path)
        image = image.resize((200, 150), Image.LANCZOS)
        self.division_image = ImageTk.PhotoImage(image)

        #self.division_image = PhotoImage(file=division_image)
        self.division = division
        self.date = get_current_date()
        # Add Menu
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)

        # Search Menu
        self.search_menu = Menu(self.my_menu, tearoff=0)
        self.my_menu.add_cascade(label="Search", menu=self.search_menu)
        # Drop down menu
        self.search_menu.add_command(label="Search", command=lookup_records)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Reset", command=query_database)

        # Add Some Style
        self.style = ttk.Style()
        # Pick A Theme
        self.style.theme_use('default')
        # Configure the Treeview Colors
        self.style.configure("Treeview",
                             background="#D3D3D3",
                             foreground="black",
                             rowheight=40,
                             fieldbackground="#D3D3D3")

        self.style.configure("Treeview.Heading", font=("Arial", 50))  # Set the font size here for the column headings
        # configure the rows in the tree
        self.style.configure("Treeview", font=("Arial", 30))  # Set the font size here
        # Change Selected Color #347083
        self.style.map('Treeview',
                       background=[('selected', self.saved_highlight_color)])

        self.label_frame = Frame(self.root)
        self.label_frame.pack(pady=30)
        # use images like buttons in Division Frame



        self.division_button = Button(self.label_frame, image=self.division_image)
        self.division_button.grid(row=0, column=0, padx=10)

        self.date_label = Label(self.label_frame, text=self.date, font=("Arial", 30))
        self.date_label.grid(row=1, column=0)

        self.division_label = Label(self.label_frame, text=division, font=("Arial", 30))
        self.division_label.grid(row=1, column=3)

        self.kdm_logo_image = Label(self.label_frame, image=self.kdm_logo)
        self.kdm_logo_image.grid(row=0, column=3, pady=10, padx=20)
        # Create a Treeview Frame

        self.division_image_button_2 = Button(self.label_frame, image=self.division_image)
        self.division_image_button_2.grid(row=0, column=5, padx=10)
        self.time_label = Label(self.label_frame, font=("Arial", 30))
        self.tree_frame = Frame(self.root)
        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended", height=13)

        def time():
            time_string = strftime('%H:%M:%S %p')
            # time_label = Label(root, font=("ds-digital", 80), background="black", foreground='cyan')
            self.time_label.config(text=time_string)
            self.time_label.after(1000, time)
            return self.time_label

        self.time_label = Label(self.label_frame, font=("Arial", 30))
        self.time = time()
        self.time_label.grid(row=1, column=5)
        self.time_label.after(1000, time)
        self.tree_frame.pack(pady=10)

        time()
        self.time_label.grid(row=1, column=5)

        # Create The Treeview
        self.my_tree.pack()

        def update():
            records = query_kdm_division(self.my_tree,database, self.division)
            populate_main_tree(self.my_tree, records)

            #query_fleet_database(self.my_tree,database, division)
            self.root.after(1000, update)
            #return self.time_label
        update()
        # Define Our Columns
        self.my_tree['columns'] = ("fleet_number", "parts_description", "in_stock_since", "status")

        # Format Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("fleet_number", anchor=W, width=350)
        self.my_tree.column("parts_description", anchor=W, width=400)
        self.my_tree.column("in_stock_since", anchor=CENTER, width=404)
        self.my_tree.column("status", anchor=CENTER, width=200)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("fleet_number", text="Fleet Number", anchor=W)
        self.my_tree.heading("parts_description", text="Parts Description", anchor=W)
        self.my_tree.heading("in_stock_since", text="In Stock Since", anchor=CENTER)
        self.my_tree.heading("status", text="Status", anchor=CENTER)

        self.blue = "blue"
        self.gray = "lightgray"
        self.white = "white"

        # Create Striped Row Tags
        self.my_tree.tag_configure('oddrow', background=self.gray)
        self.my_tree.tag_configure('evenrow', background=self.white)

        #
        query_division(self.my_tree, database,self.division)

        # Start the auto-scrolling
        # self.auto_scroll()
        self.root.attributes('-fullscreen', True)
        self.root.mainloop()

    def center_window(self):
        w = 1400
        h = 900
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()


if __name__ == "__main__":
    division = "Power Access"
    division_image = ("images/plant.png")
    app = InfoWhiteBoard(division, division_image)