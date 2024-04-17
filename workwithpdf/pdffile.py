import PyPDF4
f = open('Working_Business_Proposal.pdf','rb')# read binary
pdf_reader = PyPDF4.PdfFileReader(f)
#print(pdf_reader.numPages)
#page_one = pdf_reader.getPage(0)
#page_one_text = page_one.extractText()
#print(page_one_text)
#f.close()

#first_page = pdf_reader.getPage(0)
#pdf_writer = PyPDF4.PdfFileWriter()
#print(type(first_page))
#pdf_writer.addPage(first_page)
#pdf_output = open('Some_BrandNew_Doc.pdf','wb')
#pdf_writer.writer(pdf_output)
#f.close()
#pdf_output.close() 
pdf_text = []
for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print(pdf_text[1])# here we got page number 1 text