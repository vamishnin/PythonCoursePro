from tempfile import mktemp
import os

class WrapStrToFile: 
    def __init__(self): 
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища 
        self.__filepath = mktemp("tmp", "prefix")

    @property 
    def content(self): 
        # попытка чтения из файла, в случае успеха возвращаем содержимое 
        # в случае неудачи возвращаем 'File doesn't exist' 
        try:
            with open(self.__filepath, 'r') as f:
                file_content = f.read()
                return file_content
        except Exception:
            return 'File is not exist'

    @content.setter 
    def content(self, value): 
        # попытка записи в файл указанного содержимого 
        with open(self.__filepath, 'w') as f:
            f.write(value)

    @content.deleter 
    def content(self): 
        # удаляем файл: os.remove(имя_файла) 
        os.remove(self.__filepath)
    
    @property
    def filename(self):
        return self.__filepath

wstf = WrapStrToFile()
print(f'filename = {wstf.filename}') 
print(wstf.content)  # Output: File doesn't exist 
wstf.content = 'test str' 
print(wstf.content)  # Output: test_str 
wstf.content = 'text 2' 
print(wstf.content)  # Output: text 2 
del wstf.content     # после этого файла не существует
