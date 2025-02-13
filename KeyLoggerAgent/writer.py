from abc import ABC,abstractmethod
from datetime import datetime

# מחלקה מופשטת של כותב. מורישה מתודה של כתןב.
class IWriter(ABC):
    @abstractmethod
    def write(self, data: str) -> None:
        pass

# מחלקת כתיבה למילון
class DictWriter(IWriter):

    def __init__(self):
        self.dct = {}

    def get_dict(self) -> dict:
        current_dict = self.dct.copy()
        self.dct = {}
        return current_dict
    
    @staticmethod
    def cur_min():
        return datetime.now().strftime("%d/%m/%Y, %H:%M")

    def write(self, data: str) -> None:
        if self.cur_min() not in self.dct:
            self.dct[self.cur_min()] = data
        else:
            self.dct[self.cur_min()] += data
        
# מחלקת כתיבה לקובץ טקסט
class FileWriter(IWriter):

    def __init__(self, path = "C:/Users/User/OneDrive/GitProjects/KeyloggerFile/keylogger.txt"):
        self.file_path = path

    def change_file_path(self, path: str) -> None:
        self.file_path = path

    def write(self, data: str) -> None:
        with open(self.file_path, "a") as file:
            file.write(data+"\n")