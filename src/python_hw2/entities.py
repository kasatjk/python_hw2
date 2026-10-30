from dataclasses import dataclass

@dataclass(init=False)
class guinea_pig():
    name: str
    age: int
    is_swiss: bool
    has_friend: bool

    def __init__(self, name: str, age: int, is_swiss: bool, has_friend: bool):
        self.name = name
        self.age = age
        self.is_swiss = is_swiss
        self.has_friend = has_friend
    
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 15:
            raise ValueError("Age must be between 0 and 15")
        self._age = value
    
    def eat(self):
        print(f"{self.name} eats.")
    
    def spend_time(self):
        if self.has_friend:
            print(f"{self.name} is happy :)")
        else:
            print(f"{self.name} is sad :(")

@dataclass
class swiss_government():
    corruption: bool = False
    is_angry: bool = False

    def check_guinea_pig(self, pet):
        if pet.is_swiss and not pet.has_friend:
            self.is_angry = True
            print(f"{pet.name} is alone! Pay a fine! >:(")
        elif pet.is_swiss and pet.has_friend:
            self.is_angry = False
            print(f"{pet.name} is happy! Have a nice day! :)")
        else:
            print(f"{pet.name} is not swiss. We don't care!")