dict_ = {'one': 1, 'two': 2, 'three': 3}

text = 'Count one, two, three, one'

for rep_key in dict_.keys():
    text = text.replace(rep_key, str(dict_[rep_key]))

print(f'Text with replacements: {text}')

