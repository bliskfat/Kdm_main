from tkinter_widgets import *
from tkinter_widgets import ttk
import sqlite3
import datetime
from tkcalendar import Calendar, DateEntry

from custom_functions import *
from PIL.ImageTk import PhotoImage

# variables
#kdm_logo = PhotoImage(file="images/kdm_logo.png")
date = get_current_date()
division_image = "/Volumes/Back Up/Backup/KDM_Stores_V1/images/plant.png"
#kdm_logo = PhotoImage(file="images/kdm_logo.png")

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
root.title("Cycling Frames")
define_size(root, 1200,800)


# Create multiple frames
def time():
    time_string = strftime('%H:%M:%S %p')
    # time_label = Label(root, font=("ds-digital", 80), background="black", foreground='cyan')
    time_label.config(text=time_string)
    time_label.after(1000, time)
    return time_label



# Add Some Style
frames = []

frame_1 = Frame(root)
main_frame = Frame(frame_1, background="white", width=1700, height=1000)
time_label = Label(main_frame, font=("Arial", 30))
time = time()
time_label.grid(row=1, column=5)
time_label.after(1000, time)

tree_frame = Frame(main_frame)
my_tree = ttk.Treeview(tree_frame, selectmode="extended", height=13)
tree_frame.grid(row=1, column=5)
time
time_label.grid(row=1, column=5)



main_frame.pack(pady=20)
division_button = Button(main_frame)
division_button.grid(row=0, column=0, padx=10)


frame_2 = Frame(root, bg="blue", width=1400, height=1000)
frame_3 = Frame(root, bg="green", width=1400, height=1000)
frame_4 = Frame(root, bg="yellow", width=1400, height=1000)
#frames.append(Frame(root, bg="red", width=1400, height=1000))

frames.append(frame_1)
frames.append(frame_2)
frames.append(frame_3)
frames.append(frame_4)

#frames.append(Frame(root, bg="green", width=200, height=100))
#frames.append(Frame(root, bg="blue", width=200, height=100))

# Set the content for each frame
for i, frame in enumerate(frames):
    Label(frame, text=f"This is Frame {i+1}", fg="white", bg=frame["bg"]).pack(expand=True)

# Hide all frames except the first one
for frame in frames[1:]:
    frame.pack_forget()

# Initialize the index to start with the first frame
current_frame_index = 1

# Schedule the first frame cycle after 5 seconds
root.after(5000, cycle_frames)

# Start the main event loop for the main window
root.mainloop()
