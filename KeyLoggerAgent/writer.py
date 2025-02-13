from abc import ABC,abstractmethod
from datetime import datetime


class IWriter(ABC):
    """Abstract class for Interface Writer with write method"""
    @abstractmethod
    def write(self, data: str) -> None:
        pass

class DictWriter(IWriter):
    """Dictionary writer class with write method
    which get data as string and write it to a dictionary,
    minutes as keys and text as values"""

    def __init__(self):
        self.dct = {}

    def get_dict(self) -> dict:
        """reset the object dictionary and return the last dictionary"""
        current_dict = self.dct.copy()
        self.dct = {}
        return current_dict

    @staticmethod
    def cur_min():
        """return the current minute"""
        return datetime.now().strftime("%d/%m/%Y, %H:%M")

    def write(self, data: str) -> None:
        if self.cur_min() not in self.dct:
            self.dct[self.cur_min()] = data
        else:
            self.dct[self.cur_min()] += data


class FileWriter(IWriter):
    """File writer class with write method
    which get data as string and write it to a text file."""
    def __init__(self, path :str = "C:/Users/User/OneDrive/GitProjects/KeyloggerFile/keylogger.txt"):
        self.file_path = path

    def write(self, data: str) -> None:
        with open(self.file_path, "a") as file:
            file.write(data+"\n")