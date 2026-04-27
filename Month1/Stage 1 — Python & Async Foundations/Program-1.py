# Python data types, loops, functions & classes

# Data types
my_string = "Hello, World!"
my_integer = 42
my_float = 3.14
my_double = 3.141592653589793
my_boolean = True

# Lists
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Adding an element to the list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])  # Output: 3

# Dictionaries
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict["name"])  # Output: "John"

# Loops
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Functions


def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result)  # Output: 7

# Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 25)
person1.greet()  # Output: "Hello, my name is Alice and I am 25 years old."
