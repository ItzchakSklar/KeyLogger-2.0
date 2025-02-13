from abc import ABC, abstractmethod

# מחלקה מופשטת של מצפין
class IEncryptor(ABC):

    @abstractmethod
    def encrypt(data):
        pass