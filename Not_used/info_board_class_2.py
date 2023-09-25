from configparser import ConfigParser
from tkinter_widgets import *

from custom_functions import *


# division = "Small Tools
class InfoWhiteBoard:
    query_1 = "SELECT rowid, * FROM fleet_parts_data"
    database = "database files/kdm_stores.db"
    date = get_current_date()

    def __init__(self, division, division_image):
        self.root = Tk()
        self.root.title('KDM Hire Parts Board - In Stock')
        # configure the size of the window

        app_width = 1400
        app_height = 950
        # get the current screen measures
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # center the window on the current screen
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        self.center_window()
        # Read our config file and get colors
        self.parser = ConfigParser()
        self.parser.read("treebase.ini")
        self.saved_primary_color = self.parser.get('colors', 'primary_color')
        self.saved_secondary_color = self.parser.get('colors', 'secondary_color')
        self.saved_highlight_color = self.parser.get('colors', 'highlight_color')
        self.kdm_logo = PhotoImage(file="../images/kdm_logo.png")
        self.division_image = PhotoImage(file=division_image)
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

        self.label_frame = Frame(self.root, background="darkblue")
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
            query_division(self.my_tree, self.database, division)
            self.root.after(1000, update)
            # return self.time_label

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

        self.time_label = Label(self.label_frame, font=("Arial", 30))
        self.time = time()
        self.time_label.grid(row=5, column=5)
        self.time_label.after(1000, time)
        self.tree_frame.pack(pady=10)
        time()
        self.time_label.grid(row=1, column=5)

        #
        query_division(self.my_tree, self.database, division)

        # Start the auto-scrolling
        # self.auto_scroll()
        # self.root.attributes('-fullscreen', True)
        self.root.mainloop()
        # sleep(100)
        # self.root.withdraw()
        # self.root.after()

    def center_window(self):
        w = 1200
        h = 950
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()


if __name__ == "__main__":
    plant = "Plant"
    plant_image = ("images/plant.png")

    small_tools = "Small Tools"
    small_tools_image = ("images/small_tools.png")
    app = InfoWhiteBoard(plant, plant_image)
