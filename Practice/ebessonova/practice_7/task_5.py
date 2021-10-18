import re


with open('../../README.md', 'r') as f:
    git_text = f.read()

s = re.compile(r'"(git .*)"')
s1 = re.compile(r': (git .*)')

result_list = re.findall(s, git_text) + re.findall(s1, git_text)

for i in result_list:
    print(i)
