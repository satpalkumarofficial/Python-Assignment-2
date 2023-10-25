"""
Q1. Write a Python program to create a class named
    Student with attributes name, age and grade. Implement 
    a method to display the student’s information in a formatted 
    string. """

class Students:
    def __init__(self, name, age, grade):
        self.name, self.age, self.grade = name, age, grade

    @classmethod
    def from_input(cls):
        print("Enter student's information:")
        name, age, grade = input("Name: "), input("Age: "), input("Grade: ")
        return cls(name, age, grade)

    def get_students_info(self):
        print(f"\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}\n")

student = Students.from_input()
student.get_students_info()
