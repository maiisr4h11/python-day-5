# Define the Parent class
class Parent:
    # The constructor method (__init__) initializes the 'name' attribute
    def __init__(self, name):
        self.name = name  # Assign the 'name' parameter to the instance attribute 'name'

    # Method to greet, using the 'name' attribute
    def greet(self):
        print(f"Hello, my name is {self.name}.")  # Print a greeting message that includes the person's name

# Define the Child class that inherits from Parent
class Child(Parent):
    # The constructor method (__init__) initializes both 'name' and 'age' attributes
    def __init__(self, name, age):
        # Call the parent class's __init__ method to initialize the 'name' attribute
        super().__init__(name)  # 'super()' allows us to call the Parent class's methods
        self.age = age  # Assign the 'age' parameter to the instance attribute 'age'
 # Method to display the child's age
    def display_age(self):
        print(f"I am {self.age} years old.")  # Print a message displaying the child's age

# Creating an instance of the Child class
c = Child("Alice", 10)  # 'c' is an instance of the Child class with 'name' as "Alice" and 'age' as 10

# Call the inherited greet method from the Parent class
c.greet()  # This will output: "Hello, my name is Alice."

# Call the display_age method defined in the Child class
c.display_age()  # This will output: "I am 10 years old."

