from fpdf import FPDF
from PIL import Image
import csv
filename = '123_oct23.csv'
data_list = []
with open(filename,'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        data_list.append(row)
data_list.pop(0)
for i in data_list:
    print(i)
size=len(data_list)
print(size)

# class PDF(FPDF):
    # def header(self):
    #     self.image('header.png', 40, 8, 120)
    #     self.ln(25)

pdf = FPDF('P', 'mm', 'A4')
watermark='watermark.pdf'
for i in range(0,size):
    total = 0
# creating the pdf layout
# Adding header to the page
    # Set page break
    pdf.set_auto_page_break(auto=True,margin=15)
    # Adding a page
    pdf.add_page()
    logo = Image.open('logo.png')
    pdf.image('logo.png', x=20, y=40, w=70)
    pdf.image('logo.png', x=120, y=40, w=70)



    # Adjust the position and size as needed

    pdf.image('header.png', 40, 0, 110)
    pdf.ln(20)
    # Office copy
    pdf.set_font('helvetica','B',16)
    # Fee receipt heading
    pdf.cell(0,10,'FEE RECEIPT',align='C')
    pdf.ln()
    pdf.set_font('helvetica', 'BU', 11)
    pdf.cell(0, 8, 'OFFICE COPY', align='C', )
    pdf.ln()
    pdf.set_font('helvetica', '', 11)

    # Setting current list
    currlist=data_list[i]
    #Adding student details
    #Use fstring to finally add details using CSV file
    pdf.cell(140,5,f'Name:{currlist[0]}')
    pdf.cell(90, 5, f'Duration:{currlist[4]}')
    pdf.ln()
    pdf.cell(140,5,f'Class:{currlist[1]}')
    pdf.cell(90, 5, f'Last Date:{currlist[5]}')
    pdf.ln()
    pdf.cell(0,5,f'Contact Number:{currlist[3]}')
    pdf.ln()
    pdf.cell(0,5,f'Gender:{currlist[6]}')
    pdf.ln()
    pdf.set_font('helvetica','BU',14)
    pdf.cell(0,10,'CHARGES',align='C')
    pdf.ln()
    pdf.set_font('helvetica','',11)
    pdf.cell(140,5,f'Previous Balance:{currlist[10]}')
    pdf.cell(90,5,f'Rs.{currlist[11]}')
    pdf.ln()
    pdf.cell(140,5,'Tuition fees')
    pdf.cell(90, 5,f'Rs. {currlist[7]}')
    total += int(currlist[7])
    total = total+int(currlist[9])
    total+=int(currlist[11])
    pdf.ln()
    pdf.cell(140,5,'Transport Charges')
    pdf.cell(90, 5, f'Rs.{currlist[9]}')
    pdf.ln()
    pdf.set_font('helvetica','BU',14)
    pdf.cell(140,5,'Total:')
    pdf.cell(90,5,f'Rs.{total}')
    pdf.ln(5)
    pdf.cell(0,9,'Payment Details(To be filled by parent)',align='C')
    pdf.ln()
    pdf.set_font('helvetica','B',12)
    pdf.cell(140,10,'Received amount:________________')
    pdf.cell(90,10,'Date:_____________')
    pdf.ln()
    pdf.cell(70,10,'Payment Mode:_____________')
    pdf.cell(90,8,'Cheque Details:____________________________________')
    pdf.ln()
    pdf.ln()
    pdf.cell(100,5,'Parent Signature:')
    pdf.cell(90,5,'School Stamp')
    pdf.ln(10)
    cut=""
    pdf.set_font('helvetica', 'B', 14)
    for i in range(0,130):
        cut+="-"
    pdf.cell(0,10,cut,align='C')
    pdf.ln(32)
    #Student copy

    pdf.image('header.png',40,145,110)
    pdf.image('logo.png', x=20, y=180, w=70)
    pdf.image('logo.png', x=120, y=180, w=70)
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'FEE RECEIPT', align='C')
    pdf.ln()
    pdf.set_font('helvetica','BU',11)
    pdf.cell(0,8,'STUDENT COPY',align='C')
    pdf.ln()
    #Receipt heading font size

    #Details font size
    pdf.set_font('helvetica','',11)
    pdf.cell(140, 5, f'Name:{currlist[0]}')
    pdf.cell(90, 5, f'Duration:{currlist[4]}')
    pdf.ln()
    pdf.cell(140, 5, f'Class:{currlist[1]}')
    pdf.cell(90, 5, f'Last Date:{currlist[5]}')
    pdf.ln()
    pdf.cell(0, 5, f'Contact Number:{currlist[3]}')
    pdf.ln()
    pdf.cell(0, 5, f'Gender:{currlist[6]}')
    pdf.ln()
    pdf.set_font('helvetica','BU',14)
    pdf.cell(0,10,'CHARGES',align='C')
    pdf.ln()
    pdf.set_font('helvetica', '', 11)
    pdf.cell(140, 5, f'Previous Balance:{currlist[10]}')
    pdf.cell(90, 5, f'Rs.{currlist[11]}')
    pdf.ln()
    pdf.cell(140, 5, 'Tuition fees')
    pdf.cell(90, 5,f'Rs. {currlist[7]}')
    pdf.ln()
    pdf.cell(140, 5, 'Transport Charges')
    pdf.cell(90, 5, f'Rs.{currlist[9]}')
    pdf.ln()
    pdf.set_font('helvetica','BU',14)
    pdf.cell(140,5,'Total:')
    pdf.cell(90, 5, f'Rs.{total}')
    pdf.ln(5)
    pdf.cell(0, 7, 'Payment Details(To be filled by parent)', align='C')
    pdf.ln()
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(140, 10, 'Paid amount:________________')
    pdf.cell(90, 10, 'Date:_____________')
    pdf.ln()
    pdf.cell(70, 10, 'Payment Mode:_____________')
    pdf.cell(90, 8, 'Cheque Details:____________________________________')
    pdf.ln()
    pdf.ln()
    pdf.cell(100, 5, 'Parent Signature:')
    pdf.cell(90, 5, 'School Stamp')

    #Marking PDF end
    pdf.ln(20)
    
    #Saving the pdf
pdf.output('123_oct23.pdf')
print('Successfully executed')