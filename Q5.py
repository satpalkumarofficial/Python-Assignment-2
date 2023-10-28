"""
Q5. Write a Python program to create a class named Employee with attributes
    name, id, and salary. Implement methods to get and set the salary of the 
    employee. Also, implement a class method to calculate the average salary 
    of all employees."""

class Employee:
    employees = []

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        Employee.employees.append(self)

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.salary = new_salary
            return f"Salary for {self.name} updated to ${self.salary}"
        else:
            return "Invalid salary amount."

    @classmethod
    def average_salary(cls):
        if cls.employees:
            total_salary = sum(emp.salary for emp in cls.employees)
            return total_salary / len(cls.employees)
        else:
            return "No employees available to calculate the average salary."


emp1 = Employee("Alice", 101, 50000)
emp2 = Employee("Bob", 102, 60000)
emp3 = Employee("Charlie", 103, 75000)

print(emp1.get_salary())
print(emp2.set_salary(65000))

print(Employee.average_salary())
