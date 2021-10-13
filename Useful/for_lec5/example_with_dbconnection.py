from dbconnection import DBConnection
from lib_with_dbconnection import fun


conn = DBConnection('exampledb')
print(f"This is example {id(conn)}")
print(f'do stuff with connection {conn}')
fun()
