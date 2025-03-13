# Task 1: Library Management System with Custom Exceptions

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not member:
            raise ValueError(f"Member {member_name} not found.")
        if not book:
            raise BookNotFoundException(f"Book {book_title} not found.")
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not member:
            raise ValueError(f"Member {member_name} not found.")
        if not book:
            raise BookNotFoundException(f"Book {book_title} not found.")
        member.return_book(book)

# Test the program
library = Library()

# Add books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Add members
member1 = Member("Alice")
member2 = Member("Bob")
library.add_member(member1)
library.add_member(member2)

# Borrow and return books
try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "1984")  
except Exception as e:
    print(e)

try:
    library.borrow_book("Bob", "1984")  
except Exception as e:
    print(e)

try:
    library.borrow_book("Alice", "A Book That Doesn't Exist")  
except Exception as e:
    print(e)

try:
    library.borrow_book("Alice", "1984")  
except Exception as e:
    print(e)

library.return_book("Alice", "1984")
library.borrow_book("Bob", "1984")

# Task 2: Student Grades Management

import csv

# Read data from grades.csv
grades = []
try:
    with open('grades.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append(row)
except FileNotFoundError:
    print("grades.csv file not found.")
    grades = [
        {"Name": "Alice", "Subject": "Math", "Grade": "85"},
        {"Name": "Bob", "Subject": "Science", "Grade": "78"},
        {"Name": "Carol", "Subject": "Math", "Grade": "92"},
        {"Name": "Dave", "Subject": "History", "Grade": "74"}
    ]

# Calculate the average grade for each subject
subject_grades = {}
for grade in grades:
    subject = grade['Subject']
    grade_value = int(grade['Grade'])
    if subject not in subject_grades:
        subject_grades[subject] = []
    subject_grades[subject].append(grade_value)

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

# Write the average grades to average_grades.csv
with open('average_grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average Grade'])
    for subject, average in average_grades.items():
        writer.writerow([subject, average])

# Task 3: JSON Handling

import json
import csv

# Load tasks from tasks.json
try:
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    print("tasks.json file not found.")
    tasks = [
        {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
        {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
        {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
    ]

# Display all tasks
for task in tasks:
    print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

# Save changes back to tasks.json
def save_tasks(tasks):
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")

# Calculate task completion stats
def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks
    return total_tasks, completed_tasks, pending_tasks, average_priority

total_tasks, completed_tasks, pending_tasks, average_priority = calculate_stats(tasks)
print(f"Total tasks: {total_tasks}")
print(f"Completed tasks: {completed_tasks}")
print(f"Pending tasks: {pending_tasks}")
print(f"Average priority: {average_priority:.2f}")

# Convert JSON data to CSV
with open('tasks.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Task', 'Completed', 'Priority'])
    for task in tasks:
        writer.writerow([task['id'], task['task'], task['completed'], task['priority']])