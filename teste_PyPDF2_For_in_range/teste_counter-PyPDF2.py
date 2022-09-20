import PyPDF2
import time
import collections


start = time.time()

pdf_file = open('diario.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
c = collections.Counter(range(number_of_pages))

for i in c:
    page = read_pdf.getPage(i)
    page_content = page.extractText()
    print(page_content)

print("Tempo de execução")

end = time.time()

print(end - start)
