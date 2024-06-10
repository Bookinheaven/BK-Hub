"""
Design a class to represent a rectangle with length and breadth as instance
attributes. Create two rectangle objects, r1 and r2. Initialize the attributes
using the constructor and do the following operations.

● r3 = r1 + r2, where r3 is an another Rectangle object
o r3’s length = r1’s length + r2’s length
o r3’s breadth = r1’s breadth + r2’s breadth
● Obtain a user-friendly string representation of the Rectangle
object as Length is 30 and Breadth is 11 by overriding
__str__( ).
o print(r3)
● Compare the dimensions of r1 and r2.
o r1 == r2
o r1 < r2
o r1 > r2
o r1 >= r2
o r1 <= r2
"""
class Rectangle():
    def __init__(self: object, length: int, breadth: int) -> None:
        self.length = length
        self.breadth = breadth
    def __str__(self: object) -> str:
        return f"Length: {self.length} Breadth: {self.breadth}"
    def __eq__(self, other: object) -> bool:
        return self.length == other.length, self.breadth == other.breadth
    def __add__(self:object, other: object) -> int:
        return Rectangle(self.length + other.length, self.breadth + other.breadth)
    def __lt__(self, other: object) -> bool:
        return self.length < other.length, self.breadth < other.breadth
    def __gt__(self, other: object) -> bool:
        return self.length > other.length, self.breadth > other.breadth
    def __ge__(self, other: object) -> bool:
        return self.length >= other.length, self.breadth >= other.breadth
    def __le__(self, other: object) -> bool:
        return self.length <= other.length, self.breadth <= other.breadth

r1 = Rectangle(length=20, breadth=6)
r2 = Rectangle(length=10, breadth=5)
r3 = r1 + r2
print(r3)
r3 = r1 == r2
print(f"Equal: {r3}")
r3 = r1 > r2
print(f"Greater than: {r3}")
r3 = r1 < r2
print(f"Less than: {r3}")
r3 = r1 >= r2
print(f"Greater than or equal: {r3}")
r3 = r1 <= r2
print(f"Less than or equal: {r3}")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")