from pdf2docx import Converter
pdf_file='Invoice-031-Updated-Anjal-Thapa.pdf'
docx_file='clcoding.docx'
cv=Converter(pdf_file)
cv.convert(docx_file)
cv.close()
