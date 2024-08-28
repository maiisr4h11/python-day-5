#Getter and Setter
class Person:
    def __init__(self, name, age):
        self._name = name  #The underscore makes the attribute private
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age
    
    #Setter method for age
    def set_age(self, age):
        if age < 0:
            return ValueError("Age cannot be negative")
        self._age = age

p = Person("John", 30)
print(p.get_name())
p.set_age(40)
print(p.get_age())

    