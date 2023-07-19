from enum import Enum

class TaskPriority(Enum):

    HIGH = 0
    LOW = 1
    LOWEST = 2

    @classmethod
    def choices(cls):
        print(tuple((i.value, i.name) for i in cls))
        return tuple((i.value, i.name) for i in cls)
    

class TaskStatus(Enum):

    STATUS_0 = 0
    STATUS_1 = 1
    STATUS_2 = 2

    @classmethod
    def choices(cls):
        print(tuple((i.value, i.name) for i in cls))
        return tuple((i.value, i.name) for i in cls)