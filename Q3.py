"""
Q3. Write a Python program to create a class named Rectangle with 
    attributes length and width. Implement methods to calculate the area
    and perimeter of the rectangle. Also, implement a method to compare
    two rectangles based on their area."""


class Rectangle:
    def __init__(self, length, width):
        self.length, self.width = length, width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * self.length + self.width

    def compare_area(self, other):
        return "Rectangle 1 is larger than Rectangle 2" if self.calculate_area() > other.calculate_area() else "Rectangle 1 is smaller than Rectangle 2" if self.calculate_area() < other.calculate_area() else "Rectangle 1 is equal to Rectangle 2"


rect1 = Rectangle(20, 30)
rect2 = Rectangle(30, 20)
rect3 = Rectangle(10, 50)

print(f"Area of rectangle: {Rectangle.calculate_area(rect1)}")
print(f"Perimeter of rectangle: {Rectangle.calculate_perimeter(rect1)}")
print(
    f"Area comparision of rectangles: {Rectangle.compare_area(rect1, rect2)}")
print(
    f"Area comparision of rectangles: {Rectangle.compare_area(rect1, rect3)}")
