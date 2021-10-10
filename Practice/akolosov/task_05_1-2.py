import random
import time


class Man:

    def __init__(self, name: str):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        return super().solve_task()


if __name__ == "__main__":
    person_one = Man("Vasya")
    print(f"{person_one.name} is ordered to solve task")
    person_one.solve_task()

    person_second = Pupil("Peten'ka")
    print(f"{person_second.name} is ordered to solve task")
    person_second.solve_task()
