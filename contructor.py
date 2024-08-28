class person:
    #Constructor for the class with default values
    def __init__(self, name, occupation, networth):
        #Initialize attributes
        self.name = name
        self.occupation = occupation
        self.networth = networth
    
    #Method to display information about the person
    def info(self):
        print(f"Name:{self.name}")
        print(f"Occupation:{self.occupation}")
        print(f"Networth:{self.networth}")
    
person1 = person("John", "Programmer", 5000)
person2 = person("Mike", "Singer", 1000)
person1.info()
person2.info()

