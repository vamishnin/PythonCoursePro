import pickle, random, itertools


class Human: 
    def __init__(self, name, lastname, age, addr, hobby_): 
        self.name = name
        self.last_name = lastname
        self.age = age
        self.address = addr
        self.hobby = hobby_
        
    def __repr__(self): 
        return '<Human(name={}, last_name={}, age={}, address={}, hobby={})>'.format(self.name, self.last_name, self.age, self.address, self.hobby) 

def create_Humanity(count):
    my_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    my_combination = list(itertools.combinations(my_alphabet, 6))
    humanity = []
    
    for i in range(count):
        name = ''.join(random.choice(my_combination))
        last_name = ''.join(random.choice(my_combination))
        age = random.randint(1, 100)
        addr = ''.join(random.choice(my_combination))
        hobby = ''.join(random.choice(my_combination))
        human = Human(name, last_name, age, addr, hobby)
        humanity.append(human)
    
    return humanity

def serialize_Objects(filepath, objs):
    with open(filepath, 'wb') as handle:
        pickle.dump(objs, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
def deserialize_Objects(filepath):
    with open(filepath, 'rb') as handle:
        objs = pickle.load(handle)
        return objs
    
humans = create_Humanity(10)
for i in humans:
    print('i = {}'.format(i))

serialize_Objects('human.data', humans)
res = deserialize_Objects('human.data')

print('Deserialized result')
for i in res:
    print('i = {}'.format(i))


