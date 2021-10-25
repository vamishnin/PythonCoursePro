import re


if __name__ == "__main__":
    re_git = re.compile(
        r'git [a-z]+(?:(?: \-[-a-z]+(?:(?: ".*")|(?: [a-z_]+)))?(?: [a-zA-Z._:/@]+)?(?: [a-z]+)?)?')
    with open("Practice/README.md", "r") as reader:
        for line in reader:
            result = re.findall(re_git, line)
            for i in result:
                print(i)