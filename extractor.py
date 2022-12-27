import PyPDF2
import pyexpat
import textract
import nltk
import pyperclip
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file
filename = askopenfilename()
print(filename)


# fileurl = 'C:\Users\Usuario\Desktop\ClicOH\Programacion\Id-Extractor\scan1.pdf'
pdfFileObj = open(filename, 'rb')

pdfReader = PyPDF2.PdfReader(pdfFileObj)

num_pages = len(pdfReader.pages)
text = ""
count = 0
while count < num_pages:
    pageObj = pdfReader.pages[count]
    count += 1
    text += pageObj.extract_text()

if text != "":
    text = text
else:
    text = 'PDF escaneado no contiene texto...'

tokens = word_tokenize(text)
contador = 0
codigosFlex = []
for palabra in tokens:
    if (palabra.startswith('41')) and len(palabra) > 6 and not (palabra.endswith('Mercado')):
        contador += 1
        codigosFlex.append(palabra)
        print(palabra)

print('Cantidad de registros: ', contador)

pyperclip.copy(' '.join(str(e + '\n') for e in codigosFlex))
spam = pyperclip.paste()

input('Codigos copiados en tu portapapeles. Presione ENTER para salir  ....\n')

print(codigosFlex)
