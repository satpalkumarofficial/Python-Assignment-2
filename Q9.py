"""
Q9. Write a Python program to create a class named Calculator with methods for basic
    arithmetic operations like add, subtract, multiply, and divide. Also, implement operator
    overloading by defining special methods like add, sub, mul and truediv for the
    Calculator class."""

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"


    def __add__(self, a):
        return self.add(self, a)

    def __sub__(self, a):
        return self.subtract(self, a)

    def __mul__(self, a):
        return self.multiply(self, a)

    def __truediv__(self, a):
        return self.divide(self, a)


calc = Calculator()


print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.subtract(10, 4))
print("Multiplication:", calc.multiply(6, 2))
print("Division:", calc.divide(12, 4))


print("Operator Overloading - Addition:", calc + 7)
print("Operator Overloading - Subtraction:", calc - 3)
print("Operator Overloading - Multiplication:", calc * 4)
print("Operator Overloading - Division:", calc / 2)
