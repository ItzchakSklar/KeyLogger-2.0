from abc import ABC, abstractmethod

class IEncryptor(ABC):

    @abstractmethod
    def encrypt(data):
        pass

class XorEncryption(IEncryptor):
    def __init__(self):
        self.key = "Y"

    def encrypt(self, data):
        encrypted_string = ""
        convert_to_string = str(data)
        arr = list(convert_to_string)
        for i in arr:
            char = ord(i)
            char = char ^ ord(self.key)
            encrypted_char = chr(char)
            encrypted_string += str(encrypted_char)
        return encrypted_string
    def decryption(self, data):
        decryption_string = ""
        password_number = input("Enter password: ")
        arr = list(data)
        for i in arr:
            char = ord(i)
            char = char ^ ord(password_number)
            decryption_char = chr(char)
            decryption_string += str(decryption_char)
        return decryption_string


xor = XorEncryption()
print(xor.encrypt({"abcd": "efg", 123: "hig"}))
print(xor.decryption(xor.encrypt({"abcd": "efg", 123: "hig"})))

