import os, PyPDF2

os.chdir(os.path.dirname(__file__))

pdfFileObj = open('Benz.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
pageObj.extractText()
