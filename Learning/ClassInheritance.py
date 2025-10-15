

# We're creating a class inheritance all the info from the other class "Car"
'''
So, what is the point of OOP Class Inheritance?
It gives us an ability to build on top of other functions/classes without spamming everything
in one specific class. Makes it more readable and organized.
'''

class Car:
    def __init__(self):
        self.belts = True;
        self.wheels = 4;

    def move(self):
        print("Brrrrrrrr")


class Toyota(Car):
    def __init__(self):
        # super() - reference to the inh. super class (Car)
        # We're using super to activate this Car class in this function
        super().__init__()

    def move(self):
        # Calling out move() function from Car
        super().move()
        # Printing additional message after calling move() from a super class
        print("even damn faster than before")


# we're making Mazda connected to a "Car" class
Mazda = Toyota()
# We're calling a "move" function in it
Mazda.move()