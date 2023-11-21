from pdfquery import PDFQuery

pdf = PDFQuery('customers.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]


# Use str.join() to concatenate the array elements into a single string
output_text = '\n'.join(text)

with open('output.txt', 'w') as file:
    # Write your program's output to the file
    file.write(output_text)

print(output_text[0:50])



# import pandas as pd
# import pdfquery

# #read the PDF
# pdf = pdfquery.PDFQuery('customers.pdf')
# pdf.load()


# #convert the pdf to XML
# pdf.tree.write('customers.xml', pretty_print = True)
# pdf