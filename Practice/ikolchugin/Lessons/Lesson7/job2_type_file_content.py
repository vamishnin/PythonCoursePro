from subprocess import Popen, PIPE
from os.path import normpath


def get_file_content(filename):
    proc = Popen(['type', filename], stdout=PIPE, stderr=PIPE, shell=True)

    # я считал, что нет необходимости в явном вызове, в proc.communicate() уже есть вызов wait.
    # Возможно, есть какие-то подводные камни, но мне пока не встречалось.
    # proc.wait()

    res = proc.communicate()

    if proc.returncode:
        print(res[1].decode('cp866'))
    return res[0].decode('utf-8')


print(__file__)
print(normpath(__file__))

content = get_file_content(normpath(__file__))
print(content)
