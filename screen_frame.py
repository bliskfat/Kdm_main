from time import strftime
from tkinter import *
import datetime
from PIL import ImageTk, Image
from frame_functions import *

logo_image = "images/kdm_logo.png"
font_style = "Arial"
font_size = 40
# Placeholder InfoWhiteBoard class
class InfoBoard(Frame):
    def __init__(self, category, image_paths, master=None):
        super().__init__(master)
        self.count = 0
        self.tree = None
        self.date_label = None
        self.time_label = None
        self.photo = None
        self.image_label_2 = None
        self.image_label_1 = None
        self.logo_label = None
        self.logo = None
        self.bg = "white",
        self.category = category
        self.image_paths = image_paths
        self.current_image_index = 0
        self.date = get_current_date()
        self.create_widgets()

    def auto_scroll1(self):
        scroll_speed = 0.01  # Adjust the scrolling speed here
        current_pos = self.tree.yview()[0]
        self.tree.yview_moveto(current_pos + scroll_speed)
        if current_pos >= 0.9:
            self.tree.yview_moveto(0.0)  # Reset to the top if reached the bottom
        self.master.after(1000, self.auto_scroll)  # Adjust the update interval here


    #scroll_speed = 0.01
    def auto_scroll(self):
        scroll_speed = 0.01

        self.count += 1
        item_ids = self.tree.get_children()  # Get the list of item IDs
        total_items = len(item_ids)
        print(f"total items: {total_items}")
        current_pos = self.tree.yview()[0]
        new_pos = current_pos + scroll_speed

        # if new_pos >= 1.0:
        if self.count  == total_items:
            new_pos = 0.0  # Reset to the top if reached the bottom
            self.count = 0

        self.tree.yview_moveto(new_pos)
        print(self.count)
        self.master.after(1000, self.auto_scroll)
    #self.auto_scroll()
    # added
    def time(self):
        time_string = strftime('%H:%M:%S %p')
        # time_label = Label(root, font=("ds-digital", 80), background="black", foreground='cyan')
        self.time_label.config(text=time_string)
        self.time_label.after(1000, self.time)
        return self.time_label

    # end
    def update_image(self):
        if self.image_paths:
            image_path = self.image_paths[self.current_image_index]
            image = Image.open(image_path)
            image = image.resize((200, 150), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            # division image 1
            self.image_label_1.config(image=self.photo)
            # division image 2
            self.image_label_2.config(image=self.photo)
            # update the image
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.after(5000, self.update_image)

    def create_widgets(self):
        label = Label(self, text=self.category, font=(font_style, font_size))
        label.grid(row=1, column=1, columnspan=1)
        logo = Image.open(logo_image)
        logo = logo.resize((800, 150), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo)
        self.logo_label = Label(self)
        self.logo_label.config(image=self.logo)
        self.logo_label.grid(row=2, column=1, columnspan=1,pady=20)
        # division image 2
        self.image_label_1 = Label(self)
        self.image_label_1.grid(row=2, column=0, columnspan=1)
        # division image 2
        self.image_label_2 = Label(self)
        self.image_label_2.grid(row=2, column=2, columnspan=1)
        # added
        self.time_label = Label(self, font=(font_style, 30))
        # self.time = self.time()
        # self.time_label.grid(row=1, column=0)
        self.time_label.after(1000, self.time)
        self.time()
        self.time_label.grid(row=1, column=0)

        self.date_label = Label(self, text=self.date, font=(font_style, 30))
        self.date_label.grid(row=1, column=2)
        # end

        self.update_image()

        style = ttk.Style()
        # Pick A Theme
        style.theme_use('default')
        # Configure the Treeview Colors
        style.configure("Treeview", background="#D3D3D3", foreground="black",
                        rowheight=40, fieldbackground="#D3D3D3")

        style.configure("Treeview.Heading", font=("Arial", 60))  # Set the font size here for the column headings
        # configure the rows in the tree
        style.configure("Treeview", font=("Arial", 40),rowheight=50)  # Set the font size here
        # Change Selected Color #347083
        style.map('Treeview', background=[('selected', "blue")])

        self.tree = ttk.Treeview(self, selectmode="extended", height=13)
        self.tree.grid(row=3, column=0, columnspan=3)
        self.tree['columns'] = ("fleet_number", "parts_description", "in_stock_since", "days_in_stock")

        # Format Our Columns
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("fleet_number", anchor=W, width=200)
        self.tree.column("parts_description", anchor=W, width=350)
        self.tree.column("in_stock_since", anchor=CENTER, width=300)
        self.tree.column("days_in_stock", anchor=CENTER, width=400)

        # Create Headings
        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("fleet_number", text="Fleet Number", anchor=W)
        self.tree.heading("parts_description", text="Parts Description", anchor=W)
        self.tree.heading("in_stock_since", text="In Stock Since", anchor=CENTER)
        self.tree.heading("days_in_stock", text="Days In Stock", anchor=CENTER)

        gray = "lightgray"
        white = "white"

        # Create Striped Row Tags
        self.tree.tag_configure('oddrow', background=gray)
        self.tree.tag_configure('evenrow', background=white)

        self.tree.tag_configure('warning', background='red')
        self.tree.tag_configure('acceptable', background='orange')
        self.tree.tag_configure('good', background='green')

        def update():
            records = query_kdm_division(self.tree, database, self.category)
            populate_tree(self.tree,records)
            #self.auto_scroll()
            self.master.after(1000, update)
            #self.auto_scroll()

        update()

def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")

def define_size(root, width, height):
    # Designate Height and Width of our app
    app_width = width
    app_height = height
    # get the current screen measures
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # center the window on the current screen
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


def cycle_frames():
    global current_frame_index
    # Hide the current frame
    if current_frame_index is not None:
        frames[current_frame_index].pack_forget()
    # Move to the next frame in the cycle
    current_frame_index = (current_frame_index + 1) % len(frames)
    # Show the next frame
    frames[current_frame_index].pack()
    # Schedule the next frame cycle after 5 seconds
    root.after(5000, cycle_frames)


# Create the main window
root = Tk()
root.title("KDM Hire - Info Board")
define_size(root, 1900, 990)

# Create multiple frames (replace image paths with your actual image paths)
frames = []

divisions = [
    ("Small Tools", ["images/small_tools.png", "images/small_tools.png"]),
    ("Plant", ["images/plant.png", "images/plant.png"]),
    ("Vehicles", ["images/lorry bay.png"]),
    ("K Power", ["images/kpower.png"]),
    ("Power Access", ["images/power access.png", "images/power access.png"])
]

for division, image_paths in divisions:
    frame = InfoBoard(division, image_paths, root)
    frame.auto_scroll()
    frames.append(frame)
    frame.pack_forget()

# Initialize the index to start with the first frame
current_frame_index = 0

# Schedule the first frame cycle after 5 seconds
root.after(5000, cycle_frames)

# Start the main event loop for the main window
root.mainloop()
