import os  # импорт модуля для работы с файлами
import tempfile  # импорт модуля для создания временных файлов


class WrapStrToFile:
    def __init__(self):
        self.__filepath = tempfile.mktemp()  # здесь инициализируется атрибут filepath, содер. путь до файла-хранилища

    # попытка чтения из файла, в случае успеха возвращаем содержимое
    # в случае неудачи возвращаем 'File doesn't exist'
    @property  # будет вызываться по [эксемпляр].content и выдавать указанные св-ва экземпляра
    def content(self):  # 3 метода имеют одно имя 'content', но различаются декораторами
        try:  # ожидаем исключение, ловим его
            with open(self.__filepath, 'r') as f:  # менеджер контекста для гарантир.закрытия файла после вып-я.блока
                return f.read()  # возвр.результат чтения файла
        except FileNotFoundError:  # отлавливаем исключение типа FileNotFoundError
            return "File doesn't exist"

    @content.setter  # вызовется при присваивании [эксемпляру].content какого либо значения
    def content(self, value):
        with open(self.__filepath, 'w') as f:  # менеджер контекста для гарантир.закрытия файла после вып. блока
            return f.write(value)              # вернуть записанное значение value

    @content.deleter    # вызовиться при удалении файла
    def content(self):
        os.remove(self.__filepath)


wstf = WrapStrToFile()
print(wstf.content)        # по wstf.content вызывается декоратор @property
wstf.content = 'test str'  # при присваивании значения вызывается @content.setter
print(wstf.content)        # Output: test_str - снова посмотрели свойства @property
wstf.content = 'text 2'    # переписали содержание файла
print(wstf.content)        # Output: text 2
del wstf.content           # При указании del вызывается @content.deleter
print(wstf.content)
