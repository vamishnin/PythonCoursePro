import re

git_re = re.compile(r'git\s[a-z]+(?:\s-(?:\w|(?:-\w+)+))?(?:\s\".*\"|\s(?:https|git).*?\.git|(?:\s\w+(?:\.\w+)?){0,2})')

with open('../../../README.md', 'r', encoding='utf-8') as f:
    git_commands = []
    while line := f.readline():
        for res in re.findall(git_re, line):
            git_commands.append(res)


for i in sorted(set(git_commands)):
    print(i)
