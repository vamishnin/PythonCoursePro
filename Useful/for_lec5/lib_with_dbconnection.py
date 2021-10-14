from dbconnection import DBConnection


def fun():
    d = DBConnection('exampledb')
    print(f'do stuff with connection {d}')
    print(f"This is fun: {id(d)}")
