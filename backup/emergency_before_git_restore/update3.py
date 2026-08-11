import re

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix grammatical issues introduced by literal replace
text = text.replace('Is there a up to 3 trial classes class available?', 'Are there up to 3 trial classes available?')
text = text.replace('We offer a completely up to 3 trial classes class', 'We offer up to 3 trial classes')
text = text.replace('schedule your free session within 24 hours', 'schedule your first trial class within 24 hours')
text = text.replace('Book Your Free Quran Trial Class', 'Book Up to 3 Quran Trial Classes')
text = text.replace('Experience a free Quran class with our certified tutor', 'Experience up to 3 Quran trial classes with our certified tutor')
text = text.replace('your free trial class', 'your trial classes')
text = text.replace('a completely free trial class', 'up to 3 trial classes')
text = text.replace('schedule your free trial class', 'schedule your first trial class')
text = text.replace('free trial form', 'trial form')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)
