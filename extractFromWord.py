from docx import *
import re
import json

document = Document('randomNames.docx')


for para in document.paragraphs:
    text = para.text
    if "Mother" in text:
        email_list = re.findall(r"[a-z0-9\-+_]+@[a-z0-9\-+_]+\.[a-z]+", text)
        for email in email_list:
            print(email)






