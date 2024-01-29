from PyPDF3 import PdfFileMerger
pdfs=['pdf1.pdf','pdf2.pdf']
merger=PdfFileMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("merged.pdf")
merger.close()