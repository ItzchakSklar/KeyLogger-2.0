from abc import ABC,abstractmethod
from datetime import datetime
from json import dumps

# מחלקה מופשטת של כותב. מורישה מתודה של כתןב.
class IWriter(ABC):
    @abstractmethod
    def write(data: str) -> None:
        pass

# מחלקת כתיבה למילון
class DictWriter(IWriter):

    def __init__(self):
        self.dct = {}

    @staticmethod
    def cur_min():
        return datetime.now().strftime("%d/%m/%Y, %H:%M")

    def write(self, key: str) -> None:
        if self.cur_min not in self.dct:
            self.dct[self.cur_min] = key
        else:
            self.dct[self.cur_min] += key
        
# json מחלקת כתיבה לקובץ 
class FileWriter(IWriter):

    def __init__(self):        
        self.file_path = ""

    def add_file_path(self, path: str) -> None:
        self.file_path = path

    def write(self, data: str) -> None:
        with open(self.file_path, "a") as file:
            dumps(data, file)