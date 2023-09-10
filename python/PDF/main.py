import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endwith('.pdf'):
        merger.append(file)
    merger.write('combined.pdf')