from configparser import ConfigParser
from tkinter_widgets import *
from tkinter_widgets import ttk
from PIL import Image, ImageTk
import sqlite3
import datetime

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def query_division(tree, database, division):
    # Function to query the database and populate the Treeview with data
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM fleet_parts_data WHERE division=?", (division,))
    records = cursor.fetchall()

    # Clear the Treeview
    tree.delete(*tree.get_children())

    # Insert data into the Treeview
    for record in records:
        tree.insert("", "end", values=record)

    connection.close()

class InfoWhiteBoard:
    query_1 = "SELECT rowid, * FROM fleet_parts_data"
    #database = "database files/kdm_stores.db"
    database = 'database files/vor_shelves.db'

    def __init__(self, division, division_image_path):
        self.root = Tk()
        self.root.title('KDM Hire Parts Board - In Stock')

        app_width = 1400
        app_height = 950
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        self.parser = ConfigParser()
        self.parser.read("treebase.ini")
        self.saved_highlight_color = self.parser.get('colors', 'highlight_color')

        self.division = division
        self.date = get_current_date()

        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)

        self.search_menu = Menu(self.my_menu, tearoff=0)
        self.my_menu.add_cascade(label="Search", menu=self.search_menu)
        self.search_menu.add_command(label="Search", command=self.lookup_records)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Reset", command=self.query_database)

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Treeview",
                             background="#D3D3D3",
                             foreground="black",
                             rowheight=40,
                             fieldbackground="#D3D3D3")

        self.style.configure("Treeview.Heading", font=("Arial", 50))
        self.style.configure("Treeview", font=("Arial", 30))
        self.style.map('Treeview',
                       background=[('selected', self.saved_highlight_color)])

        self.label_frame = Frame(self.root, background="darkblue")
        self.label_frame.pack(pady=30)

        self.kdm_logo = ImageTk.PhotoImage(Image.open("../images/kdm_logo.png"))
        self.division_image = ImageTk.PhotoImage(Image.open(division_image_path))

        self.division_button = Button(self.label_frame, image=self.division_image)
        self.division_button.grid(row=0, column=0, padx=10)

        self.date_label = Label(self.label_frame, text=self.date, font=("Arial", 30))
        self.date_label.grid(row=1, column=0)

        self.division_label = Label(self.label_frame, text=division, font=("Arial", 30))
        self.division_label.grid(row=1, column=3)

        self.kdm_logo_image = Label(self.label_frame, image=self.kdm_logo)
        self.kdm_logo_image.grid(row=0, column=3, pady=10, padx=20)

        self.division_image_button_2 = Button(self.label_frame, image=self.division_image)
        self.division_image_button_2.grid(row=0, column=5, padx=10)

        self.time_label = Label(self.label_frame, font=("Arial", 30))
        self.time = self.update_time()
        self.time_label.grid(row=1, column=5)
        self.time_label.after(1000, self.update_time)

        self.tree_frame = Frame(self.root)
        self.tree_frame.pack(pady=10)

        self.my_tree = ttk.Treeview(self.tree_frame, selectmode="extended", height=13)
        self.my_tree.pack()

        self.my_tree['columns'] = ("fleet_number", "parts_description", "in_stock_since", "status")

        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("fleet_number", anchor=W, width=350)
        self.my_tree.column("parts_description", anchor=W, width=400)
        self.my_tree.column("in_stock_since", anchor=CENTER, width=404)
        self.my_tree.column("status", anchor=CENTER, width=200)

        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("fleet_number", text="Fleet Number", anchor=W)
        self.my_tree.heading("parts_description", text="Parts Description", anchor=W)
        self.my_tree.heading("in_stock_since", text="In Stock Since", anchor=CENTER)
        self.my_tree.heading("status", text="Status", anchor=CENTER)

        self.gray = "lightgray"
        self.white = "white"

        self.my_tree.tag_configure('oddrow', background=self.gray)
        self.my_tree.tag_configure('evenrow', background=self.white)

        self.update()

        self.root.mainloop()

    def update(self):
        query_division(self.my_tree, self.database, self.division)
        self.root.after(1000, self.update)

    def query_database(self):
        # Your implementation for querying the database (omitted for brevity)
        pass

    def lookup_records(self):
        # Your implementation for searching records (omitted for brevity)
        pass

    def update_time(self):
        time_string = datetime.datetime.now().strftime('%H:%M:%S %p')
        self.time_label.config(text=time_string)
        return self.time_label

    def center_window(self):
        w = 1200
        h = 950
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.root.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

if __name__ == "__main__":
    plant = "Plant"
    plant_image = "images/plant.png"

    small_tools = "Small Tools"
    small_tools_image = "images/small_tools.png"
    app = InfoWhiteBoard(plant, plant_image)
