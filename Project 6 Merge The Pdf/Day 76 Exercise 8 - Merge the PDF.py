# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.


# visit this documetnation on how to use teh pypdf module - https://pypdf.readthedocs.io/en/latest/
# Documentation for any module can be googled



# NOTE: we need to install pyPDF2 using pip 

from PyPDF2 import PdfWriter    #importing pdfwriter method form pypdf2 module
import os

merger = PdfWriter() #creating object named merger of pdfweriter moudles
files = [file for file in os.listdir() if file.endswith(".pdf")]    #listts all the pdf files in this folder and storing in files variable

# for loop runs untill there are files in this foler
for pdf in files:
    merger.append(pdf) #appends every file with each other

merger.write("merged-pdf.pdf")  # a new pdf will be created with the name merge pdf
merger.close()