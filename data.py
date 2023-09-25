import sqlite3
from datetime import datetime

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

k_power = "K Power"
power_access = "Power Access"
plant = "Plant"
vehicles = "Vehicles"
small_tools = "Small Tools"

k_power = "K Power"
power_access = "Power Access"
plant = "Plant"
vehicles = "Vehicles"
small_tools = "Small Tools"


data = [
    [vehicles, "ARV201", "Fuel PIPE", "26-06-2023", "23 Days"],
    [plant, "FL250", "BEARING", "22-06-2023", "45 days"],
    [plant, "DU083", "JCB HEADLIGHT", "01-05-2022", "60 days"],
    [plant, "SLA20", 'WIRE ROPE', "01-02-2023", "40 days"],
    [k_power, "RGN352", 'CLUTCH KIT', "02-02-2023", "52 days"],
    [plant, "FL023", "AIR FILTER", "02-02-2023", "25 days"],
    [small_tools, "FB052", "SOLENOID", "23-12-2022", "37 days"],
    [small_tools, "YPW001", "FUEL PUMP", "03-05-2023", "12 days"],
    ["K Power", "RTA0023", "16A PLUG", "17-02-2023", "3 days"],
    ["K Power", "LT112", 'JACK LEG', "18-11-2022", "25 days"],
    [small_tools, "GNT015", "IGNITION SWITCH", "26-05-2023", "17 days"],
    ["K Power", "RGN112", 'FUEL GAUGE', "12-06-2022", "22 days"],
    [plant, "FL251", 'GLASS ROOF', "31-05-2022", '22 days'],
    [plant, "YFL20", 'WIPER MOTOR', "05-06-2023", "322 days"],
    [vehicles, "ARV202", 'WHEEL BRACE', "05-06-2023", "100 days"],
    [vehicles, "VH060", "ANGLE MIRROR", "05-06-2022", "10 days"],
    [vehicles, "VH122", 'FLOOR MAT', "05-06-2003", "3 days"],
    [vehicles, "VT020", "ABS LEAD", "09-04-2023", "21 days"],
    [vehicles, "ARV199", "DOOR STRAP", '27-12-2022', "2 days"],
    [vehicles, "WV003", 'TAIL LIGHT', "11-11-2022", "10 days"]

]


def insert_dummy_data(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    dummy_data = [
        ("Fleet001", "Repair", "CPR123", "01-07-2023", "05-07-2023", "Returned"),
        ("Fleet002", "Replace", "CPR124", "02-07-2023", "06-07-2023", "Pending"),
        ("Fleet003", "Repair", "CPR125", "03-07-2023", None, "In Progress"),
        ("Fleet004", "Replace", "CPR126", "04-07-2023", "07-07-2023", "Returned"),
        ("Fleet005", "Repair", "CPR127", "05-07-2023", None, "Pending"),
        ("Fleet006", "Replace", "CPR128", "06-07-2023", None, "In Progress"),
        ("Fleet007", "Repair", "CPR129", "07-07-2023", None, "Pending"),
        ("Fleet008", "Replace", "CPR130", "08-07-2023", None, "In Progress"),
        ("Fleet009", "Repair", "CPR131", "09-07-2023", "13-07-2023", "Returned"),
        ("Fleet010", "Replace", "CPR132", "10-07-2023", None, "Pending"),
        # ... (other data)
    ]

    with connection:
        for data in dummy_data:
            formatted_data = (
                data[0], data[1], data[2],
                datetime.strptime(data[3], '%d-%m-%Y').date(),
                datetime.strptime(data[4], '%d-%m-%Y').date() if data[4] else None,
                data[5]
            )
            cursor.execute("""
                INSERT INTO returns (fleet_number, return_motive, cpr_number, date_created, date_returned, status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, formatted_data)

    print("Dummy data inserted")

