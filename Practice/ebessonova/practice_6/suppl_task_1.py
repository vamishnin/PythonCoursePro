# Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно

def text_iter_by_paragraph(filename, paragraph_symbol):
    text = list()
    with open(filename, 'r') as f:
        for i in f.read().split(paragraph_symbol):
            text.append(i)

    return iter(text)


text_iter = text_iter_by_paragraph('text_P.txt', 'P\n')
while True:
    try:
        print(next(text_iter))
    except StopIteration:
        break
