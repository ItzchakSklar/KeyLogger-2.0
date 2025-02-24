from abc import ABC, abstractmethod

class IEncryptor(ABC):
    """Abstract class for Interface Encryptor with encryption method."""
    @abstractmethod
    def encrypt(self, data: dict) -> str:
        pass

class XorEncryptor(IEncryptor):
    """XOR Encryptor class with methods to encrypt data using XOR encryption."""

    def __init__(self):
        self.key = "Y"

    def encrypt(self, data):
        """Encrypt the given data using XOR encryption."""
        encrypted_string = ""
        convert_to_string = str(data)
        arr = list(convert_to_string)

        for i in arr:
            char = ord(i)
            char = char ^ ord(self.key)
            encrypted_char = chr(char)
            encrypted_string += str(encrypted_char)

        return encrypted_string


"""
# Example usage:
xor = XorEncryptor()
print(xor.encrypt({"abcd": "efg", 123: "hig"}))
# print(xor.decrypt(xor.encrypt({"abcd": "efg", 123: "hig"})))
"""

