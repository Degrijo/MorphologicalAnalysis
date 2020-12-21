from PyPDF2 import PdfFileReader

from app.core.algorithms import frequency_word_case, short_word_case, my_case


def get_pdf_content(filename):
    with open(filename, 'rb') as file:
        doc = PdfFileReader(file)
        text = ''
        for i in range(doc.getNumPages()):
            text += doc.getPage(i).extractText()
    return text


def get_languages(filepath):
    text = get_pdf_content(filepath)
    return f'Frequency word case: ' + frequency_word_case(text) + \
           '\nShort word case: ' + short_word_case(text) + \
           '\nMy case: ' + my_case(text)


print(get_languages('../../datasets/test1.pdf'))
print(get_languages('../../datasets/test2.pdf'))
print(get_languages('../../datasets/test3.pdf'))
print(get_languages('../../datasets/test4.pdf'))
