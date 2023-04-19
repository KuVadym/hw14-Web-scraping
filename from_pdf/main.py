# import PyPDF2

# pdf_file = open('images.pdf', 'rb')

# pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# num_pages = pdf_reader.numPages

# for page_num in range(num_pages):
#     page_obj = pdf_reader.getPage(page_num)
#     page_text = page_obj.extractText()
#     print(page_text)

from pdfminer.high_level import extract_text
from pdfminer.image import ImageWriter

pdf_file = "example.pdf"
text = extract_text(pdf_file)
print(text)