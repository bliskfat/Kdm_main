import sqlite3
from sqlite3 import Error

database = "database files/kdm_stores.db"


def create_database(database):
    # Create a database or connect to one that exists
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


def create_service_kits_table(database):
    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # Create Table
        cursor.execute("""CREATE TABLE if not exists service_kits (                      
                id INTEGER PRIMARY KEY AUTOINCREMENT,                                                                                                
            	fleet_number text,                                                                                                                       
            	date date,                                                                   
            	status text)                                                                 
            	""")
        print("Table Created")


def populate_service_kits_table(service_kit_data):
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # for record in data:
        # print(f' record ={record[0]}')
        cursor.executemany("""
            INSERT INTO service_kits (fleet_number, date
            VALUES (?, ?)
            """, service_kit_data )


def delete(query):
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # for record in data:
        # print(f' record ={record[0]}')
        records = cursor.fetchall()
        for record in records:
            print(record)
        print("deleted")

query = "SELECT rowid, * FROM vor_shelves_data WHERE kdm_division LIKE ?"
delete(query)

service_kits_data =[
    ["ARV262","09-08-2023","Complete"],
    ["ARV214","09-08-2023","Complete"],
    ["ARV223","09-08-2023","Complete"],
    ["ARV192","09-08-2023","Complete"],
    ["ARV157","09-08-2023","Complete"],
    ["VH196","09-08-2023","Complete"],
    ["ARV145","09-08-2023","Complete"],
    ["VH082", "09-08-2023", "Complete"],
    ["VH175", "09-08-2023", "Complete"],
    ["VH201", "09-08-2023", "Complete"],
    ["VH181", "09-08-2023", "Complete"],
    ["VC005", "09-08-2023", "Complete"],
    ["VH085", "09-08-2023",  "Complete"],
    ["VH188",  "09-08-2023",  "Complete"],
    ["VH192",  "09-08-2023", "Complete"],
    ["ARV131",  "09-08-2023",  "Complete"],
    ["ARV180",  "09-08-2023", "Complete"],
    ["ARV218",  "09-08-2023", "Complete"],
    ["ARV187",  "09-08-2023",  "Complete"],
    ["ARV213",  "09-08-2023",  "Complete"],
    ["ARV105",  "09-08-2023",  "Complete"],
    ["ARV133",  "09-08-2023",  "Complete"],
    ["ARV230",  "09-08-2023", "Complete"],
    ["ARV181",  "09-08-2023", "Complete"]

]

#create_service_kits_table(database)
populate_service_kits_table(service_kits_data)

#create_database(database)
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
    [vehicles, "VT020", "ABS LEAD", "09-08-2023", "21 days"],
    [vehicles, "ARV199", "DOOR STRAP", '27-12-2022', "2 days"],
    [vehicles, "WV003", 'TAIL LIGHT', "11-11-2022", "10 days"]

]

oil_filters = [
    ["OC155", 'GS-O1-A'],
    ["OC196", 'GS-O2-C'],
    ["LF699", 'GS-O3-B'],
    ["LF16015", 'GS-O4-E'],
    ["LF3682", 'GS-O5-F'],
    ["OC244", 'GS-O6-G'],
    ["OC47", 'GS-O7-A'],
    ["OC155", 'GS-O8-B']
]

def populate_table():
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # for record in data:
        # print(f' record ={record[0]}')
        cursor.executemany("""
            INSERT INTO vor_shelves_data (kdm_division, fleet_number, description, date, status)
            VALUES (?, ?, ?, ?, ?)
            """, data )


def populate_table1(data, database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    try:
        cursor.executemany("""
            INSERT INTO vor_shelves_data (kdm_division, fleet_number, description, date, status)
            VALUES (?, ?, ?, ?, ?)
        """, data)
        connection.commit()
        print("Records inserted successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error occurred while inserting records:", e)
    finally:
        connection.close()


# populate_table1(data, database)
# populate_table()

def populate_table_two(data, database, table):
    query = f"""
            INSERT INTO {table} (kdm_division, fleet_number, description, date, status)
            VALUES (?, ?, ?, ?, ?)
        """
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Records inserted successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error occurred while inserting records:", e)
    finally:
        connection.close()


table = 'vor_shelves_data'

#populate_table_two(data, database, table)

#database = 'databases files/new_db.db'

def create_connection(database_file):
    """Create a database connection to a SQlite database"""
    connection = None
    try:
        connection = sqlite3.connect(database_file)
        print(sqlite3.version)
    except Error as e:
        print('Error')
        print(e)
    finally:
        if connection:
            connection.close()



def create_oil_filter_table(database):
    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # Create Table
        cursor.execute("""CREATE TABLE if not exists oil_filters (                      
                    id INTEGER PRIMARY KEY AUTOINCREMENT,                                        
                    part_number text NOT NULL,                                                           
                	location text)                                                                                                                            
                	""")

create_oil_filter_table(database)

def populate_oil_filter_table(data, database):
    query = f"""
            INSERT INTO oil_filters (part_number,location)
            VALUES (?, ?)
        """
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Records inserted successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error occurred while inserting records:", e)
    finally:
        connection.close()


populate_oil_filter_table(oil_filters, database)
def create_fuel_filter_table(database):
    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # Create Table
        cursor.execute("""CREATE TABLE if not exists fuel_filters (                      
                    id INTEGER PRIMARY KEY AUTOINCREMENT,                                        
                    part_number text NOT NULL,                                                           
                	location text)                                                                                                                            
                	""")

def populate_fuel_filter_table(data, database):
    query = f"""
            INSERT INTO fuel_filters (part_number,location)
            VALUES (?, ?)
        """
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Records inserted successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error occurred while inserting records:", e)
    finally:
        connection.close()

def create_air_filter_table(database):
    # Create a database or connect to one that exists
    connection = sqlite3.connect(database)
    # Create a cursor instance

    cursor = connection.cursor()
    with connection:
        # Create Table
        cursor.execute("""CREATE TABLE if not exists air_filters (                      
                    id INTEGER PRIMARY KEY AUTOINCREMENT,                                        
                    part_number text NOT NULL,                                                           
                	location text)                                                                                                                            
                	""")

def populate_air_filter_table(data, database):
    query = f"""
            INSERT INTO air_filters (part_number,location)
            VALUES (?, ?)
        """
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        connection.commit()
        print("Records inserted successfully.")
    except sqlite3.Error as e:
        connection.rollback()
        print("Error occurred while inserting records:", e)
    finally:
        connection.close()


#create_connection(database)