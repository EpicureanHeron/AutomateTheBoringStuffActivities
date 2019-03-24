import PyPDF2

def firstEx():
    pdfFileObj = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    print(pdfReader.numPages)
    print(pageObj.extractText())

def secondEx():
    pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
    print(pdfReader.isEncrypted)

    try:

        print(pdfReader.getPage(0))
    except:
        print('failed')
    print(pdfReader.decrypt('rosebud'))
    pageObj = pdfReader.getPage(0)


