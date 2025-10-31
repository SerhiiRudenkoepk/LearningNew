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


