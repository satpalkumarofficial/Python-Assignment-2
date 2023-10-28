"""
Q8. Write a Python program to create a class named Person with attributes name, age and
    gender. Implement methods to greet and introduce the person. Also, implement multiple
    inheritance by creating two subclasses named Student and Teacher that inherit from
    Person and have additional attributes like course and subject respectively."""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, I'm {self.name}!"

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old and I am {self.gender}."


class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.course = course

    def introduce(self):
        return f"{super().introduce()} I am a student studying {self.course}."


class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

    def introduce(self):
        return f"{super().introduce()} I am a teacher teaching {self.subject}."


# Example usage:
person = Person("Alice", 30, "Female")
print(person.greet())
print(person.introduce())

student = Student("Bob", 20, "Male", "Computer Science")
print(student.greet())
print(student.introduce())

teacher = Teacher("Charlie", 35, "Male", "Mathematics")
print(teacher.greet())
print(teacher.introduce())
