from abc import ABC,abstractmethod

class KeyLogger:
    pass

class Writer(ABC):
    @abstractmethod
    def write(buffer) -> dict:
        pass

class Manager:
    pass
