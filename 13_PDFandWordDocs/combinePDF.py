import PyPDF2
import os
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

for pdf in pdfFiles:
    pdfFile = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
   

pdfOutputFile = open('outputCombined.pdf', 'wb')

pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()