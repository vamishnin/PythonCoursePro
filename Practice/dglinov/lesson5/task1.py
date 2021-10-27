'''
Написать класс Man, который принимает имя в конструкторе. Имеет метод solve_task, который просто выводит "I'm not ready yet".
'''
class Man:
    def __init__(self, name) -> None:
        self.name = name
    
    def solve_task(self):
        print("I`m not ready yet")


if __name__ == '__main__':
    m = Man('Ivan')
    print(f'{m.name}: ', end = '')
    m.solve_task()

