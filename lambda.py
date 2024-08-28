# Lambda is a function without a name
# add = lambda x, y: x + y
# result = add(10, 20)

# print(result)

# # Define a list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Use map() to square each number 
# squared_numbers = list(map(lambda x: x*2, numbers))

# #print the result
# print(squared_numbers)

# # Converting the strinf to list
# words = ["apple", "banana", "cherry"]
# uppercase_words = list(map(lambda x: x.upper(), words))
# print(uppercase_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)