# Define the Parent class
class Parent:
    # Method to greet, which is specific to the Parent class
    def greet(self):
        print("Hello from Parent")  # This method prints a greeting message from the Parent

# Define the Child class that inherits from Parent
class Child(Parent):
    # Method to greet, which overrides the Parent's greet method
    def greet(self):
        # Call the greet method from the Parent class using super()
        super().greet()  # This calls the Parent's greet method, so it will print "Hello from Parent"
        # Add additional behavior specific to the Child class
        print("Hello from Child")  # This prints a greeting message from the Child

# Create an instance of the Child class
c = Child()  # 'c' is an instance of the Child class

# Call the greet method on the Child instance
c.greet()  # This will first call the Parent's greet method and then the Child's greet method
