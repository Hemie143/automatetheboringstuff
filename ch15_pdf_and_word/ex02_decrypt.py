import PyPDF2


pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf.bak', 'rb'))
print(pdfReader.isEncrypted)

# pdfReader.getPage(0)              # Triggers an exception

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf.bak', 'rb'))
pdfReader.decrypt('rosebud')
pageObj = pdfReader.getPage(0)
print(pageObj)
