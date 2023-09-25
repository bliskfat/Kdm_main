from tkinter import *
from PIL import Image
from time import strftime

from kdm_division_info_class import KdmDivisionClass
from user_interface_main import output_label, select_small_tools, select_k_power


class KdmDivisionSelectionApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Kdm Division Selection")
        self.create_widgets()

    def select_small_tools():
        output_label.config(text=" ")
        output_label.config(text="Small Tools Selected")
        kdm_division = "Small Tools"
        division_image = "images/small_tools.png"
        KdmDivisionClass(root, kdm_division, division_image)
        # SmallTools(root)
        # small_tools = SmallTools(root)

    def bind_selected_small_tools(event):
        select_small_tools()

    def select_k_power():
        output_label.config(text=" ")
        output_label.config(text="K-Power Selected")
        kdm_division = "K Power"
        division_image = "images/kpower.png"
        KdmDivisionClass(root, kdm_division, division_image)

    def bind_selected_k_power(event):
        select_k_power()

    def select_power_access():
        output_label.config(text=" ")
        output_label.config(text="Power Access Selected")
        kdm_division = "Power Access"
        division_image = "images/power access.png"
        KdmDivisionClass(root, kdm_division, division_image)

    def bind_selected_power_access(event):
        select_power_access()

    def select_plant():
        output_label.config(text=" ")
        output_label.config(text="Plant Selected")
        kdm_division = "Plant"
        division_image = "images/plant.png"
        KdmDivisionClass(root, kdm_division, division_image)

    def bind_selected_plant(event):
        select_plant()

    def selected_service_kits():
        output_label.config(text=" ")
        output_label.config(text="Service Kits Selected")
        # service_kits = ServiceKits(root)

    def bind_selected_service_kits(event):
        selected_service_kits()

    def select_lorrybay():
        output_label.config(text=" ")
        output_label.config(text="Lorrybay Selected")
        kdm_division = "Vehicles"
        division_image = "images/lorry bay.png"
        KdmDivisionClass(root, kdm_division, division_image)

    def bind_selected_lorrybay(event):
        select_lorrybay()

    def selected_tools():
        output_label.config(text=" ")
        output_label.config(text="Tools Selected")
        # SmallToolsInfoBoard(root)
        # tools

    def bind_selected_tools(event):
        selected_tools()

    def selected_used_parts():
        output_label.config(text=" ")
        output_label.config(text="Used parts Selected")
        # used_parts_blob = UsedPartsBlob(root)
        # used_parts_blob = UsedPartsBlobCopy(root)
        # used_parts_blob = UsedPartsRefactored(root)

    def bind_selected_used_parts(event):
        selected_used_parts()

    def select_information_board():
        output_label.config(text=" ")
        output_label.config(text="Information board")

        division = "Small Tools"
        # division = "Power Access"
        # division = "Vehicles"
        # division = "Small Tools"
        # division = division
        division_image = "Images/kpower.png"
        InfoWhiteBoard(division, division_image)
        # SmallToolsInfoBoard(root)
        # Vehicles = 'Vehicles'
        # App(root,Vehicles)
        # root.withdraw()
        # SmallToolsInformationBoard(root)
        # Info_board_1(root)

    def bind_information_board(event):
        select_information_board()

    def create_widgets(self):
        # Designate Height and Width of our app
        app_width = 1400
        app_height = 950
        # get the current screen measures
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        # center the window on the current screen
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        # Define Frames
        general_frame = Frame(self.root)
        general_frame.pack(pady=10, padx=10)

        division_frame = Frame(general_frame)
        division_frame.grid(row=1, column=0)

        logo_frame = Frame(general_frame)
        logo_frame.grid(row=0, column=0, pady=10)

        tools_and_spares_frame = Frame(general_frame, bg='lightgrey')
        tools_and_spares_frame.grid(row=2, column=0, pady=10)

        used_parts_frame = Frame(general_frame, bg='lightgrey')
        used_parts_frame.grid(row=3, column=0, pady=10)

        service_kits_frame = Frame(general_frame, bg='lightgrey')
        service_kits_frame.grid(row=4, column=0, pady=10)

        kdm_logo = PhotoImage(file="../images/kdm_logo.png")
        kdm_logo_image = Label(logo_frame, image=kdm_logo)
        kdm_logo_image.grid(row=0, column=1, pady=20, padx=20)

        def time():
            time_string = strftime('%H:%M:%S %p')
            time_label.config(text=time_string)
            time_label.after(1000, time)

        time_label = Label(logo_frame, font=("Arial", 30))
        time = time()
        time_label.grid(row=0, column=0)
        time_label.after(1000, time)
        time()
        # Define your buttons, labels, and other widgets here
        # use images like buttons in Division Frame
        small_tools_button = Button(division_frame, image=small_tools_button_image, command=select_small_tools)
        small_tools_button.grid(row=2, column=0, padx=10)
        small_tools_button.bind("<Return>", bind_selected_small_tools)
        small_tools_label = Label(division_frame, text="Small Tools")
        small_tools_label.grid(row=3, column=0)

        kpower_button = Button(division_frame, image=kpower_button_image, command=select_k_power)
        kpower_button.grid(row=2, column=1, padx=10)
        kpower_button.bind("<Return>", bind_selected_k_power)
        kpower_label = Label(division_frame, text="K-Power")
        kpower_label.grid(row=3, column=1)

        power_access_button = Button(division_frame, image=power_access_button_image, command=select_power_access)
        power_access_button.grid(row=2, column=2, padx=10)
        power_access_button.bind("<Return>", bind_selected_k_power)
        power_access_label = Label(division_frame, text="Power Access")
        power_access_label.grid(row=3, column=2)

        plant_image_button = Button(division_frame, image=plant_button_image, command=select_plant)
        plant_image_button.grid(row=2, column=3, padx=10)
        plant_image_button.bind("<Return>", bind_selected_plant)
        plant_label = Label(division_frame, text="Plant")
        plant_label.grid(row=3, column=3)

        lorrybay_image_button = Button(division_frame, image=lorrybay_button_image, command=select_lorrybay)
        lorrybay_image_button.grid(row=2, column=4, padx=10)
        lorrybay_image_button.bind("<Return>", bind_selected_lorrybay)
        lorry_bay_label = Label(division_frame, text="Lorrybay")
        lorry_bay_label.grid(row=3, column=4)

        # tools set up
        tools_button = Button(division_frame, image=tools_button_image, command=selected_tools)
        tools_button.grid(row=4, column=3, padx=10)
        tools_button.bind("<Return>", bind_selected_tools)
        tools_label = Label(division_frame, text="Tools")
        tools_label.grid(row=5, column=3)

        # used parts set up
        used_parts_button = Button(used_parts_frame, image=used_part_button_image, command=selected_used_parts)
        used_parts_button.grid(row=4, column=2, padx=10, pady=10)
        used_parts_button.bind("<Return>", bind_selected_used_parts)
        used_parts_label = Label(used_parts_frame, text="Used Parts")
        used_parts_label.grid(row=5, column=2)

        service_kit_image_button = Button(division_frame, image=service_kit_button_image, command=selected_service_kits)
        service_kit_image_button.grid(row=4, column=2, padx=10)
        service_kit_image_button.bind("<Return>", bind_selected_service_kits)
        service_kits_label = Label(division_frame, text="Service Kits")
        service_kits_label.grid(row=5, column=2)

        # use images like buttons in Division Frame
        board_button = Button(division_frame, image=blueboard_button_image, command=select_information_board)
        board_button.grid(row=4, column=1, padx=10, pady=20)
        board_button.bind("<Return>", bind_information_board)
        board_button_label = Label(division_frame, text="Information Board")
        board_button_label.grid(row=5, column=1)

        output_label = Label(self.root, text=" ")
        output_label.pack()

    def run(self):
        self.root.mainloop()


# Create an instance of the KdmDivisionSelectionApp class and run the application
app = KdmDivisionSelectionApp()
app.run()
