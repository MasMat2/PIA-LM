import camelot

# PDF file to extract tables from
file = "HORARIOS FEB-JUN 2021.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

print(tables[0].to_excel("test.xlsx"))