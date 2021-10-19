def read_strings(file_name: str):
    with open(file_name, "r") as reader:
        for i in reader:
            yield i


if __name__ == "__main__":
    gen = read_strings("Practice/akolosov/test.txt")
    for i, s in enumerate(gen):
        print(f"String {i+1}: {s}")
