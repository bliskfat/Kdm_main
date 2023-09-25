import sqlite3
from datetime import datetime
from fpdf import FPDF
#from pdf import current_time

database = "database files/kdm_stores.db"
lookup_record = "K Power"
current_time = datetime.now()


def query_pdf_data(lookup_record):
    """Query the database and return everything related to a specific category"""
    database = "database files/kdm_stores.db"
    # Create a database connection and cursor instance
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    with connection:
        # Query the database
        cursor.execute("SELECT rowid, * FROM vor_shelves_data WHERE kdm_division LIKE ?", (lookup_record,))
        records = cursor.fetchall()

        details = []
        columns = ["Fleet Number", "Parts Description", "In Stock Since", "Number Of Days in stock"]
        details.append(columns)
        current_time = datetime.now()
        for row in records:
            in_stock_since = datetime.strptime(row[5], "%d-%m-%Y")
            elapsed_time = (current_time - in_stock_since).days
            fleet_number = row[3]
            parts_desc = row[4]
            in_stock_since = row[5]
            number_of_days = elapsed_time
            item = [fleet_number, parts_desc, in_stock_since, number_of_days]
            details.append(item)
        # sort the results
        records = sorted(records, key=lambda x: datetime.strptime(x[5], "%d-%m-%Y"), reverse=False)
        # sort the results
        details = sorted(details[1:], key=lambda x: x[-1],reverse=True)
        # add the header to the file
        details.insert(0, columns)

    return records, details

# records, details  = query_pdf_data(lookup_record)

def create_pdf(data, kdm_division):
    current_time = current_time = datetime.now()
    col_widths = [30, 80, 40, 40]  # Adjust column widths as needed
    pdf = FPDF()
    pdf.add_page()
    pdf.image("images/kdm_logo.png", 60, 5, 100)
    pdf.ln(20)
    pdf.set_font("Arial", size=10)
    # pdf.set_font('helvetica', 'B', 10)
    pdf.cell(1)
    pdf.cell(100, 8, f'{kdm_division}  -  Report Created on {current_time}', border=False, ln=1, align='C')
    for row in data:
        for i in range(len(row)):
            pdf.cell(col_widths[i], 10, str(row[i]), border=1)
        pdf.ln()

    # Set position of the footer
    pdf.set_y(-12)
    # set font
    pdf.set_font('helvetica', 'I', 8)
    # Page number
    pdf.cell(0, 10, f'Page {pdf.page_no()}/{{nb}}', align='C')
    # get total page numbers
    pdf.alias_nb_pages()
    # Set auto page break
    pdf.set_auto_page_break(auto=True, margin=15)
    print("PDF - Class")

    date = current_time.date().strftime('%d-%m-%Y')
    filename = f"pdf_reports/{kdm_division}_{date}.pdf".lower()

    pdf.output(filename)
    #pdf.output("aligned_table.pdf")
    print(f"File {filename} created.")

#create_pdf(details, lookup_record)


