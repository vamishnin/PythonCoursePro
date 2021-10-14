'''
Написать класс WrapStrToFIle, который будет иметь одно вычисляемое свойство (property) под названием content. 
В конструкторе класс должен инициализовать атрибут filepath, путем присваивания результата функции mktemp   библиотеки tempfile.
При попытке чтения свойства content должен внутри кода свойства открываться файл, 
используя атрибут filepath (с помощью функции open, из этого файла читается все содержимое и возвращается из свойства. 
Если файл не существует, то возникает ошибка, поэтому должна быть обертка вокруг открытия файла на чтение (try...except),  
с помощью которого будет возвращаться 'Файл еще не существует'. При присваивании значения свойству content файл 
по указанному пути должен открываться  на запись и записываться содержимое. 
Не забудьте закрывать файл после чтения или записи. При удалении атрибута content, должен удаляться и файл.
'''
from os import remove
from tempfile import mktemp
from time import sleep

class FailedToWriteIntoFileError(Exception):
    pass

class WrapStrToFile():
   
    def __init__(self):
        self.__filepath = mktemp(dir = './')

#Определяем поведение атрибута content
#При попытке получения значения атрибута пробуем открыть файл и прочитать содержимое
    @property
    def content(self):
        try:
            with open(self.__filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return 'Файл еще не существует'

#При попытке изменить значения атрибута пробуем открыть файл и записать в него (файл) новое значение
    @content.setter 
    def content(self, line):
        try:
            with open(self.__filepath, 'w') as f:
                f.write(line)
            print('')
        except FailedToWriteIntoFileError:
            return 'Не удается записать новое значения атрибута в файл'

#При попытке удаления атрибута удаляем и файл
    @content.deleter
    def content(self):
        try:
            remove(self.__filepath)
            print("Файл удален")
        except FileNotFoundError:
            return 'Не удается удалить файл'


if __name__ == '__main__':

    line = "При присваивании значения свойству content файл по указанному пути должен открываться  на запись и записываться содержимое"
    
    #print(WrapStrToFile.content)
    #<property object at 0x7fb289461cc0>
    
    str_to_file = WrapStrToFile()

    del str_to_file.content
    
    print(str_to_file.content)
    
    str_to_file.content = line
    print(str_to_file.content)
    
    str_to_file.content = line[::-1]
    print(str_to_file.content)
    
    sleep(2)
    del str_to_file.content
    print(str_to_file.content)
