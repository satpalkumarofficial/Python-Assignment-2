"""
Q6. Write a Python program to create a class named Car with attributes model,
    color and price. Implement methods to start, stop, and accelerate the car.
    Also, implement a static method to count the number of cars created."""

class Car:
    total_cars = 0

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        self.is_running = False
        Car.total_cars += 1

    def start(self):
        if not self.is_running:
            self.is_running = True
            return f"{self.color} {self.model} car has started."

    def stop(self):
        if self.is_running:
            self.is_running = False
            return f"{self.color} {self.model} car has stopped."

    def accelerate(self, speed):
        if self.is_running:
            return f"{self.color} {self.model} car is accelerating at {speed} mph."
        else:
            return "Car is not running. Start the car to accelerate."

    @staticmethod
    def count_cars():
        return f"Total number of cars created: {Car.total_cars}"


car1 = Car("Toyota", "Blue", 25000)
car2 = Car("Honda", "Red", 28000)

print(car1.start())
print(car2.accelerate(60))
print(car1.stop())

print(Car.count_cars())
