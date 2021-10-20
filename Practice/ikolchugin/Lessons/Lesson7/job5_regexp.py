import re
import itertools

git_re = re.compile(r'(git\s([a-z])+(\s-(\w|(-\w+)+))?(\s\".*\"|\s(https|git).*?\.git|(?:\s\w+(?:\.\w+)?){0,2}))')

with open('../../../README.md', 'r', encoding='utf-8') as f:
    git_commands = []
    while line := f.readline():
        for res in re.findall(git_re, line):
            # print(res)
            git_commands.append(tuple(itertools.filterfalse(lambda x: not x.startswith('git '), res))[0])


for i in sorted(set(git_commands)):
    print(i)