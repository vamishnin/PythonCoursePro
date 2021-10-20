def read_file_lines(filepath):
    with open(filepath, 'r') as file:
        while line := file.readline():
            yield line.strip('\n')


for each in read_file_lines('for_tasks_1_2'):
    print(each)
