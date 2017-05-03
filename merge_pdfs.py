import PyPDF2, os

def merge_pdf(src_path='.', output_file='combinedminutes.pdf'):
    pdfFiles = []
    for filename in os.listdir(src_path):
        if filename.endswith('.pdf'): pdfFiles.append(os.path.join(src_path, filename))
    pdfFiles.sort(key=str.lower)
    pdfWriter = PyPDF2.PdfFileWriter()   
    pdfOutputFile = open('combinedminutes.pdf', 'wb')
    for pdf in pdfFiles:
        pdfFile = open(pdf,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
        pdfWriter.write(pdfOutputFile)
        pdfFile.close()
    pdfOutputFile.close()

import argparse

parser = argparse.ArgumentParser(description='Merge PDF')
parser.add_argument('src_path', type=str, help='Source Directory')
parser.add_argument('-o', dest='output', type=str, help='Target file')

args = parser.parse_args()
merge_pdf(args.src_path, args.output)