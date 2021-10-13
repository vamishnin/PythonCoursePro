# class MyMeta(type):
#     pass

MyMeta = type('MyMeta', (type,), {})

MyClass = MyMeta('MyClass', tuple(), {'attr': 250})

obj = MyClass()
print(obj.attr)

