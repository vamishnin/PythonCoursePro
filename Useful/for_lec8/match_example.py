#================================Example_1=================================================

class Const:
    const = 'move'


while True:
    match input('Input command (move, stop, any other): '):
        case Const.const:
            print("I'm moving")
        case 'stop' | 'STOP' | 'Stop' as cmd:
            print(f"I'm {cmd}ping")
            break
        case cmd:
            print(f"I'm {cmd}ing")

#================================Example_2=================================================

for i in range(1, 101):
    match (i % 3, i % 5):
        case (0, 0):
            print("FizzBuzz")
        case (0, _):
            print("Fizz")
        case (_, 0):
            print("Buzz")
        case _:
            print(i)

#================================Example_3=================================================

class Tank:
    def __init__(self, power):
        self.power = power
    def __repr__(self):
        return f"Tank({self.power})"

def add(arg1, arg2):
    match (arg1, arg2):
        case (int(), int()) | (str(), str()) | (list(), list()):
            res = arg1 + arg2
        case (list(), _):
            res = arg1.copy()
            res.append(arg2)
        case (Tank(), Tank()):
            res = Tank(arg1.power + arg2.power)
        case _:
            res = None
    return res


print(f"{add(1, 2)=}")
print(f"{add('hello', 'world')=}")
print(f"{add([1, 2], [3, 4])=}")
print(f"{add([1, 2], 3)=}")
print(f"{add(Tank(10), Tank(20))=}")

#================================Example_4=================================================

def processing(data):
    match data:
        case {'GET': uri}:
            print(f'Requested URI: {uri}')
        case {'POST': new_info}:
            print(f'Update: {new_info}')
        case s if isinstance(data, str):
            print(f'Unknown string received: {s}')
        case _:
            print('Incorrect request')

processing({'GET': 'ya.ru'})
processing({'POST': [1, 2, 3]})
processing('abc')
processing(404)
