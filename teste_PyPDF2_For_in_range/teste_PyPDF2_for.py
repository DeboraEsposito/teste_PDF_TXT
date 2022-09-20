import PyPDF2
import time

start = time.time()
pdfFileObj = open('diario.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
count = pdfReader.numPages
for i in range(count):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())

print("Tempo de execução")

end = time.time()

print(end - start)
