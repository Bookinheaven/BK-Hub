class MyOwn:
    pass

obj = MyOwn()

# Inheritance 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")
my_dog = Dog("Brick", 9)
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.bark()

class Cat(Dog):
    def purr(self):
        print("Purr!")
    
my_cat = Cat("Whiskers", 2)
print(f"{my_cat.name} is {my_cat.age} years old.")
my_cat.bark() 
my_cat.purr() 

# Encapsulation 
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    def set_radius(self, new_radius):
        if new_radius > 0:
            self.__radius = new_radius

my_circle = Circle(5)
print(f"Radius: {my_circle.get_radius()}")
my_circle.set_radius(7)
print(f"New Radius: {my_circle.get_radius()}")

# Polymorphism
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

def print_area(shape):
    print(f"Area: {shape.area()}")

my_square = Square(4)
print_area(my_square)