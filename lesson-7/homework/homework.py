# Task 1
import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of the same dimension")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operation")

    def __rmul__(self, other):
        return self.__mul__(other)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[a / mag for a in self.components])


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)          
v3 = v1 + v2
print(v3)          
v4 = v2 - v1
print(v4)         
dot_product = v1 * v2
print(dot_product)
v5 = 3 * v1
print(v5)         
print(v1.magnitude())  
v_unit = v1.normalize()
print(v_unit)      

# Task 2
import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        with open(self.file_path, 'a') as file:
            file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                for line in file:
                    print(line.strip())
        else:
            print("No records found.")

    def search_employee(self, emp_id):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                for line in file:
                    if line.startswith(emp_id):
                        print(line.strip())
                        return
            print("Employee not found.")
        else:
            print("No records found.")

    def update_employee(self, emp_id):
        if os.path.exists(self.file_path):
            lines = []
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            with open(self.file_path, 'w') as file:
                for line in lines:
                    if line.startswith(emp_id):
                        name = input("Enter new Name: ")
                        position = input("Enter new Position: ")
                        salary = input("Enter new Salary: ")
                        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    else:
                        file.write(line)
            print("Employee updated successfully!")
        else:
            print("No records found.")

    def delete_employee(self, emp_id):
        if os.path.exists(self.file_path):
            lines = []
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            with open(self.file_path, 'w') as file:
                for line in lines:
                    if not line.startswith(emp_id):
                        file.write(line)
            print("Employee deleted successfully!")
        else:
            print("No records found.")

    def menu(self):
        while True:
            print("\nMenu Options:")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_all_employees()
            elif choice == '3':
                emp_id = input("Enter Employee ID to search: ")
                self.search_employee(emp_id)
            elif choice == '4':
                emp_id = input("Enter Employee ID to update: ")
                self.update_employee(emp_id)
            elif choice == '5':
                emp_id = input("Enter Employee ID to delete: ")
                self.delete_employee(emp_id)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")


# Task 3
import json
import csv

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class ToDoManager:
    def __init__(self, file_path, file_format="json"):
        self.file_path = file_path
        self.file_format = file_format
        self.tasks = []

    def add_task(self):
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD): ")
        status = input("Enter Status (Pending/In Progress/Completed): ")
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ")
                task.description = input("Enter new Description: ")
                task.due_date = input("Enter new Due Date (YYYY-MM-DD): ")
                task.status = input("Enter new Status (Pending/In Progress/Completed): ")
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ")
        for task in self.tasks:
            if task.status == status:
                print(task)

    def save_tasks(self):
        if self.file_format == "json":
            with open(self.file_path, 'w') as file:
                json.dump([task.__dict__ for task in self.tasks], file)
        elif self.file_format == "csv":
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["task_id", "title", "description", "due_date", "status"])
                for task in self.tasks:
                    writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
        print("Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(self.file_path):
            if self.file_format == "json":
                with open(self.file_path, 'r') as file:
                    self.tasks = [Task(**task) for task in json.load(file)]
            elif self.file_format == "csv":
                with open(self.file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    self.tasks = [Task(**row) for row in reader]
            print("Tasks loaded successfully!")
        else:
            print("No saved tasks found.")

    def menu(self):
        while True:
            print("\nMenu Options:")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.filter_tasks()
            elif choice == '6':
                self.save_tasks()
            elif choice == '7':
                self.load_tasks()
            elif choice == '8':
                break
            else:
                print("Invalid choice. Please try again.")

test_V1 = ToDoManager("tasks.json")
print(test_V1.__str__())

test2 = ToDoManager("home")
test2.add_task()