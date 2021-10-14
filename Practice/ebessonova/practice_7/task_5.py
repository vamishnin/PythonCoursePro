import re


with open('../../README.md', 'r') as f:
    git_text = f.read()

s = re.compile(r'\"git .*\"')
s1 = re.compile(r'\: git .*')
res = re.findall(s, git_text)
res1 = re.findall(s1, git_text)

result_list = list()

# удаляем лишние элементы из команд
for el in res:
    el = el[1:len(el) - 1]
    result_list.append(el)

for el in res1:
    el = el[2:]
    result_list.append(el)

print(result_list)
