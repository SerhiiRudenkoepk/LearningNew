# list (it can be changed)
from abc import abstractmethod

a = []
a.append(1) # add 1 to the list
a.append("abc")
a.append(True)
a.clear() # clean list

# tuples (it can't be changed/edited)
b = (2, "abc")
# only .count and .index can be used for tuple
# You can't use append etc.

# dictionary
{"key1": True, "key2": 10}
person = {"name": "Artem"}
>>> person["name"]
'Artem'

# We can't add new vars to the person dictionary through .append. But we can add it like this:
person["happy"] = True;
# we added new one to the dict. (through the python console)
# We can also change it to something else with the same method:
person["happy"] = False;

# How to copy from one dict to another
new_person = person.copy()


# set - unorganised list of elements without index. It includes only unique elements.
# it can be changed.
# ONCE AGAIN: SET DOESN'T HAVE INDEX
my_fruits = {'apple', 'banana', 'cherry'}
posts_ids = {123, 321, 312}
user_inputs = {True, 1, 'hi'} # in set there's only a set of elements to compare to other.
# but most of the time no one does a set of different elements.


'''
ZIP
ZIP function let us combine 2 lists into one
'''

fruits = ['apple', 'banana', 'cherry']
quantities = [1, 2, 3]

fr_qt_zip = zip(fruits, quantities)
print(fr_qt_zip)
>>> [('apple', 1), ('banana', 2), ('cherry', 3)]
# FYI: that if the len of one list will be higher than another, zip will not add elements what will not have a pair.
# zip can also be converted to dict. But it should only have 2 sequ. (e.g, fruits and quantities (but nothing more than that))
fr_qt_dict = dict(fr_qt_zip)

'''
about for in cycle.
We can use a short version of it.
'''
all_nums = [1, -3, 2]
absol_nums = []

for i in all_nums:
    absol_nums.append(abs(i))

# But we can do it shorter like this:
abs_num = [abs(i) for i in all_nums]
# in the beginning we're using what we want to do, and then write the main part of for in
# OR
abs_num = [i for i in all_nums if i > 0]
# we're adding every number what is higher than 0

'''
Now we will learn about normal super() and __init__()
'''
class User():
    def __init__(self, email, username):
        self.email = email
        self.username = username

class Admin(User):
    def __init__(self, email, username):
        super().__init__(email, username) # with this we're automatically calling out our super (parent class User).


# OOP - Encapsulation
# Encapsulation - hiding details, exposing only what's necessary
'''
Encapsulation - means hiding internal data and logic of an object and exposing only
what's needed through methods

" You don't need to know how a car engine works - you just press "Start" to run it "


'''
# example 1

class Car:
    def __init__(self):
        self.__engine_on = False  # ' __ ' - makes it private.

    def start(self):
        self.__engine_on = True
        print("Engine started")

my_car = Car()

'''
When we will try to print it via ' print(my_car.__engine_on) - it will not print it.
But if we will write:
print(my_car._Car__engine_on) - it will print True.
Variable didn't disappear, python hid it under another name.

_one_underscore - internal variable (but not secured)
__two_underscores - makes variable private 
'''


# example 2
class Email:
    def __init__(self, sender, recipient, subject, body):
        self.sender = sender
        self.recipient = recipient # self. - saying that this one is part of this object, not a whole program.
        self.subject = subject
        self.body = body

    def send_email(self):
        # Logic related to sending an email
        pass

    def read_email(self):
        # Logic related to reading an email
        pass

# OOP - Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        # Code to start a Vehicle
        pass

    def stop(self):
        # Code to stop the vehicle
        pass

class Car(Vehicle):  # Inheritance of everything what class Vehicle has.
    def __init__(self, make, model, doors_qty):
        super().__init__(make, model) # we're calling a constructor from parent Vehicle with super.
        # Basically, we're taking all what does Vehicle and adding it to our actions
        self.doors_qty = doors_qty

    def lock_doors(self):
        # Logic to lock doors
        pass

    def open_doors(self):
        # Logic to open doors
        pass


# Polymorphism
'''
Polymorphism - means "many forms". From Greek "poly" - many, "morph" - shape.
It allows different objects to respond to the same method in different ways.

'''
# Example 1
class Animal:
    def speak(self):
        print("Some sounds")

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Wow")

animal = [Dog(), Cat(), Animal()]

for a in animal:
    a.speak() # Woof! / Meow! / Some sounds

'''
Every object understands speak(), but does it ITS OWN way
Analogy:
You say "Say hello" ->
- French person says "Bonjour"
- German "Hallo"
- Ukrainian "Привіт" 

same command -> different behavior
'''


# Abstraction
'''
Abstraction - defining a general concept (the IDEA of something) without worrying about
HOW exactly it's done
'''
# example
from abc import ABC, abstractmethod #to make abstractmethod work we need this.

class Shape(ABC): # abstract class/
    @abstractmethod # special decorator - says this method is mandatory for everyone, but it's not realised yet.
    def area(self):
        pass # we "promise" that this method should be there

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): # realisation of the method
        return 3.14 * (self.radius ** 2)

my_cricle = Circle(5)
print(my_cricle.area())

'''
 "Shape" defines the IDEA ("every shape must have an area")
 Circle decides HOW to calculate it
 
 Analogy:
 All vehicles can "move",
 but how they move (wheels, wings, tracks) is different
'''


# Decorator
def decoration_function(original_fn):
    def wrapper_function():
        result = original_fn()

        return result


def my_function():
    print("This is my function")

# Decorator - is a function that takes another function and adds NEW behavior to it,
# without changing its original code.
# Example 2 (Adding decorator BEFORE the main func)

#  we "WRAP" our donut with this decoration

def chocolate_glaze(func):
    def wrapper():
        print("Adding chocolate")
        func() //
        print("sprinkling nuts")
    return wrapper

# Then we "WRAP" our donut with this decoration
# Naturally our wrap will be above, because code is reading things from top to bottom. d
@chocolate_glaze
def donut():
    print("This is donut")


# Example 3 adding AFTER the main func

def say_hello():
    print("Hello")

def decorator(func):  # func here is a simple parameter, like 'x' or 'y' or 'name'. But we name it func
# because we expect that there will be a func
    def wrapper():
        print("Before function runs")
        func() # we're calling the main function "say_hello"
        print("After function runs")
    return wrapper

say_hello = decorator(say_hello) # applying decorator manually

say_hello()

# Example 4

def decorator_function(original_fn):
    def wrapper(*args, **kwargs): # we're making this wrapper unique
        # Some actions before executions of the original_fn
        # *args = “take all unnamed arguments and put them in a tuple”
        # **kwargs = “take all named arguments and put them in a dictionary”
        print("Before function runs")

        result = original_fn(*args, **kwargs) # we're calling my_function here
        print("After function runs")
        return result
    return wrapper

@decorator_function
def my_function(a, b):
    print("This is my function")
    return (a, b)




''' 
How to work with FILES in Python
There's 2 libs what ca be used: os and pathlib 
'''
# OS example
from os import path

print(path.abspath('.'))
# /User/username/Desktop/python

print(type(path))
# <class 'module'>

#pathlib example
from pathlib import Path

print(Path('.').absolute())
# /User/username/Desktop/python

print(type(path))
# <class 'type'>


# path to a current directory

from pathlib import Path

print(Path.cwd())
# /User/username/Desktop/python


# creating paths on Mac and Linux
print(Path('usr').joinpath('local').joinpath('bin')) # joinpath - creates a new path 
# usr/local/bin

print(Path('usr') / 'local' / 'bin')
# usr/local/bin


# Check if the file or directory is present

print(Path('main.py').exists())
# True

print(Path('/Users/usernamee/Desktop').exists())
# True

print(Path('other.py').exists()) # exists - checks if the file/directory exists
# False


# Check if it's a file or directory

print(Path('main.py').is_file()) # check if it's a file
print(Path('/Users/username/Desktop').is_dir()) # check if it's a directory

# List of items/dirs with a loop

for f in Path('.').iterdir():  # it will show everything what is in the folder
    print(f)


# HOW TO READ/WRITE FILES

# Read
# test.txt - the code with think that this file will be placed in the same directory as your code
with open('test.txt') as test_file:
    print(test_file.read()) # read - will read everything what is in the file
    # function 'open' is now connected to 'test_file'
    # OR we can use readlines and put everything in the List
    print(test_file.readlines())
    # ['This is a test file\n',
    #  'Another line in the test file'] '

# WRITE in file
with open('new_txt.txt', 'w') as new_file:
    new_file.write("This is the text what we will put in the new file\n")

with open('new_txt.txt') as new_file:
    print(new_file.read())
    # first line in the new file

with open('new_txt.txt', 'a') as new_file:
    new_file.write("Second new line in the new file\n")

with open('new_txt.txt') as new_file:
    print(new_file.read())
    #first line in the file
    #second line in the new file

# Deleting files
print(Path('new_txt.txt').exists()) # we're checking if the file is there
# True
Path('new_txt.txt').unlink() # unlink - removes the file


# How to create a ZIP archive
from zipfile import ZipFile
from pathlib import Path

Path('my_files').mkdir() # created a directory

with open("my_files/first.txt", "w") as my_file:  # we created a file
    my_file.write("This is the text what we will put in the new file\n")

with open("my_files/second.txt", "w") as my_file:  # we created a file
    my_file.write("This is the text what we will put in the second new file\n")

with ZipFile("my_files/my_file.zip", "w") as my_zip:
    print(my_zip)
    for file in Path('my_files').iterdir():
        my_zip.write(file) # adds every file to archive cuz of the for loop

# Unpacking ZIP

with ZipFile("my_files/my_file.zip", "r") as my_zip:
    my_zip.extractall('my_files_unzipped') # extract everything, we can also create a directory
    print(my_zip.infolist()) # info about the archive

# Work with CSV files

import csv

with open('test.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["user_id", "user_name", "comments_qty"]) # write a row.
    writer.writerow(["5132", "Artem", "3312"])

# Searching words in the code

import re

my_string = "My name is Luria."
res = re.search(r"Luria", my_string) # we're searching the word (pattern) in the my_string
# OR we can also search like this
res = re.search(r"L...a", my_string) # L...a - means that it will search for a word what starts with L and ends with a.
# "^L..a" - ^ searching at the beginning of the line
# "L...a$" - $ - searching at the end of the line
# "^M.*name' starts with M at the beginning of the line, has any symbols in between and ends on '-name'. . (dot) - any symbol
# "L...a\.$" - means we're searching for smth what starts L and ends with a and also ends with '.' (dot) in the end of the line.