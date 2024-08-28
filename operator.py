# Equality operator
a = 3
b = 3
print(a is b)  # Output: True
print( a == b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # Output: False : why false? - a and b are not the same object
print( a == b) # Output: True : why true? - a and b are the same object

c = a 
print(a is c) # Output: True : why true? - a and c are the same object