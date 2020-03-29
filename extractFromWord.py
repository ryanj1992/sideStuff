from docx import *
import re

document = Document('randomNames.docx')

emails = []
for para in document.paragraphs:
    text = para.text
    if "Mother" in text:
        email_list = re.findall(r"[a-z0-9\-+_]+@[a-z0-9\-+_]+\.[a-z]+", text)
        for email in email_list:
            emails.append(email)

output = Document()
for email in emails:
    p = output.add_paragraph(email)
output.save('emails.docx')








