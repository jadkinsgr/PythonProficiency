# Python Proficiency 🐍

Welcome to the Python Proficiency Document! This document showcases proficiency in Python programming, offering insights into various Python concepts and best practices. Let's dive in! 💻

## Table of Contents 📑

- [Introduction](#introduction)
- [Basic Syntax](#basic-syntax)
- [Data Structures](#data-structures)
- [Control Flow](#control-flow)
- [Functions and Modules](#functions-and-modules)
- [Object-Oriented Programming](#object-oriented-programming)
- [File Handling](#file-handling)
- [Error Handling](#error-handling)
- [Libraries and Frameworks](#libraries-and-frameworks)
- [Testing and Debugging](#testing-and-debugging)
- [Bonus Tips](#bonus-tips)
- [Resources](#resources)

## Introduction 🌐

Python is a versatile, high-level programming language known for its readability and ease of use. Whether you're automating tasks, analyzing data, or developing web applications, Python has the tools and libraries to get the job done.

## Basic Syntax 📝

### Hello World
```python
print("Hello, World!")
```

## Variables and Data Types
```python
name = "Alice"
age = 30
height = 5.5
```
## Data Structures
### Lists
```python
fruits = ["apple", "banana", "cherry"]
```
### Dictionaries
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
```
### Tuples
```python
coordinates = (40.7128, 74.0060)
```
### Sets
```python
unique_numbers = {1, 2, 3, 4, 5}
```
## Control Flow
### If Statements
```python
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```
### Loops
```python
for fruit in fruits:
    print(fruit)
##
while age < 35:
    age += 1
```
## Functions and Modules🔧
### Defining Functions
```python
def greet(name):
    return f"Hello, {name}!"
```
### Importing Modules
```python
import math
result = math.sqrt(16)
```
## Object Oriented Programming 🧱
### Classes and objects
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", "Golden Retriever")
```

## File Handling 🗂️
### Reading Files
```python
with open('file.txt', 'r') as file:
    content = file.read()
```
### Writing Files
```python
with open('file.txt', 'w') as file:
    file.write("Hello, World!")
```
## Popular Libraries 📚
- NumPy: Numerical computing
- Pandas: Data manipulation
- Requests: HTTP requests
- Flask: Web development

### Requests Example
```python
import requests

response = requests.get("https://api.github.com")
print(response.json())
```

## Testing and Debugging 🧪
### Unit Testing
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
```

### Debugging with pdb
```python
import pdb; pdb.set_trace()
```
## Bonus Tips  💡
- Use list comprehensions for concise and efficient looping.
- Leverage generators to handle large datasets without consuming too much memory.
- Familiarize yourself with virtual environments to manage dependencies.

## Resources 📚
- [Python Documentation](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
