import re

commands = []
with open('../../../README.md', 'r') as file:
    while line := file.readline():
        if command := re.findall('(git [^а-я"\n)]+("[а-яА-Я ]+")?)', line):
            commands.extend([c[0] for c in command])

for each in commands:
    print(each)
