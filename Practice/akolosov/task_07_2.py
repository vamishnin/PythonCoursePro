import subprocess as sp


def cat_file(name: str):
    """
    Return:
        (0, Content_of_file)
        (1, Content_of_error)
        (2, None) - incorrect input data
    """
    if not isinstance(name, str):
        return 2, None

    proc = sp.Popen(['cat', name], stdout=sp.PIPE, stderr=sp.PIPE)
    res = proc.communicate()
    if proc.returncode == 0:
        return 0, res[0]
    else:
        return 1, res[1]
    


if __name__ == "__main__":
    res = cat_file("task_07_2.py")
    if res[0] == 0:
        print(f"Content of the file is:\n{res[1]}")
    elif res[0] == 1:
        print(f"Error mesage is:\n{res[1]}")
    else:
        print("Wrong data")
    print("================")
    res = cat_file("Practice/akolosov/task_07_2.py")
    if res[0] == 0:
        print(f"Content of the file is:\n{res[1]}")
    elif res[0] == 1:
        print(f"Error mesage is:\n{res[1]}")
    else:
        print("Wrong data")
    print("================")
    res = cat_file(123)
    if res[0] == 0:
        print(f"Content of the file is:\n{res[1]}")
    elif res[0] == 1:
        print(f"Error mesage is:\n{res[1]}")
    else:
        print("Wrong data")
