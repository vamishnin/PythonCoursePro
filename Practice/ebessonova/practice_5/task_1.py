class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print('I\'m not ready yet')


if __name__ == "__main__":
    man = Man('Ivan')
    print(man.name)
    man.solve_task()
