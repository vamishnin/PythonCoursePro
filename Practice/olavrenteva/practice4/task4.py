import os.path


def format_file(filepath: str, change_from: str = "\t", change_to: str = "    "):
    if not os.path.exists(filepath):
        print(f"{filepath} file doesn't exist")
        return

    with open(filepath, 'r') as read_file:
        result_file_content = ''
        for line in read_file:
            newline = line.replace(change_from, change_to)
            result_file_content += newline

    with open(filepath, 'w') as write_file:
        write_file.write(result_file_content)


format_file("FileForTask4")
format_file("FileForTask4", "    ", "\t")
