class Hero:
    def __init__(self):
        self.attr = {'power': 1, 'speed': 1, 'health': 1}

    def improve(self):
        for attr in self.attr:
            value = getattr(self, attr)
            setattr(self, attr, value * 2)


h = Hero()

h.child = Hero()
h.improve()

h.attr['child'] = Hero()
