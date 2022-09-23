import pdfplumber
import time

start = time.time()

relatorio = pdfplumber.open("diario.pdf")
pgs = relatorio.pages[0]

i = 0

while (i < 1000):
    pagina = relatorio.pages[i]
    arquivo = pagina.extract_text()
    print(arquivo)
    i = i + 1

print("Tempo de execução")

end = time.time()

print(end - start)
