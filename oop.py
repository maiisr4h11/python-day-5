#Defining a class
class person:
    #Class attributes
    name = "John"
    occupation = "Programmer"
    networth = 5000
    #Method to print information about the person
    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is {self.networth}")

p = person()
p.name = "mike"
p.occupation = "singer"
p.networth = 1000
p.info()

