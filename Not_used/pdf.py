import sqlite3
from datetime import datetime
from fpdf import FPDF

database = "database files/kdm_stores.db"
logo = "images/kdm_logo.png"


global lookup_record
class PDF(FPDF):


    def header(self):
        # Logo
        self.image("../images/kdm_logo.png", 60, 20, 100)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, "Plant", border=True, ln=1, align='R')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')



def query_kdm_division():
        """Query the database and return everything related to a specific category"""
        global database
        global lookup_record
        lookup_record = "Power Access"
        database = "database files/kdm_stores.db"
        # Create a database connection and cursor instance
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        with connection:
            # Query the database
            cursor.execute("SELECT rowid, * FROM vor_shelves_data WHERE kdm_division LIKE ?", (lookup_record,))
            records = cursor.fetchall()
            records = sorted(records, key=lambda x: datetime.strptime(x[5], "%d-%m-%Y"))

        return records

def populate_pdf(records,pdf):

        records = sorted(records, key=lambda x: datetime.strptime(x[5], "%d-%m-%Y"))
        global count
        count = 0
        current_time = datetime.now()
        # for record in records:
        #	print(record)
        for record in records:
            in_stock_since = datetime.strptime(record[5], "%d-%m-%Y")  # Assuming the date is in the sixth column

            elapsed_time = (current_time - in_stock_since).days
            #print(f" {record[3]} -- {record[4]} -- In stock since: {record[5]} -- number of days in stock {elapsed_time}")
            text = f"{record[0]}{record[3]}{record[4]}{record[5]} {elapsed_time}"

            pdf.cell(0, 10, text, ln=1)
            count += 1

        # increment counter


def new_pdf():
    # Create a PDF object
    pdf = PDF('P', 'mm', 'Letter')
    # get total page numbers
    pdf.alias_nb_pages()
    # Set auto page break
    pdf.set_auto_page_break(auto=True, margin=15)
    #Add Page
    pdf.add_page()

# specify font
    pdf.set_font('helvetica', 'BIU', 16)

    pdf.set_font('times', '', 12)
    return pdf
pdf  = new_pdf()

records = query_kdm_division()
#records = sorted(records, key=lambda x: x['in_stock_since'])
sorted_records = sorted(records, key=lambda x: datetime.strptime(x[5], "%d-%m-%Y"))

#print(records)
current_time = datetime.now()

date = current_time.date().strftime('%d-%m-%Y')
pdf_file = f"new{date}_{lookup_record}.pdf"
#pdf.output(pdf_file)
pdf.output(f"pdf_reports/{pdf_file}")

