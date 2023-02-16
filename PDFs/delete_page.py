from PyPDF2 import PdfWriter, PdfReader
pages_to_keep = [1, 2, 10] # page numbering starts from 0


infile = PdfReader('source.pdf', 'rb')
output = PdfWriter()

for i in pages_to_keep:
    p = infile.pages[i] 
    output.add_page(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)