from tempfile import mktemp
import os

class WrapStrToFile: 
    def __init__(self): 
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища 
        self.filepath = mktemp("tmp", "prefix")

    @property 
    def content(self): 
        # попытка чтения из файла, в случае успеха возвращаем содержимое 
        # в случае неудачи возвращаем 'File doesn't exist' 
        try:
            f = open(self.filepath, 'r')
            file_content = f.read()
            f.close()
            return file_content
        except Exception:
            return 'File is not exist'

    @content.setter 
    def content(self, value): 
        # попытка записи в файл указанного содержимого 
        f = open(self.filepath, 'w')
        f.write(value)
        f.close()

    @content.deleter 
    def content(self): 
        # удаляем файл: os.remove(имя_файла) 
        os.remove(self.filepath)
    
    @property
    def filename(self):
        return self.filepath

wstf = WrapStrToFile()
print(f'filename = {wstf.filename}') 
print(wstf.content)  # Output: File doesn't exist 
wstf.content = 'test str' 
print(wstf.content)  # Output: test_str 
wstf.content = 'text 2' 
print(wstf.content)  # Output: text 2 
del wstf.content     # после этого файла не существует
