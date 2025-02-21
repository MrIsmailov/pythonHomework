#  Zero Check Decorator
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

print(div(6, 2))  
print(div(6, 0)) 

#  Employee Records Manager
import os

def add_employee(file_path):
    with open(file_path, 'a') as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")

def view_employees(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    else:
        print("No records found.")

def search_employee(file_path, emp_id):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith(emp_id):
                    print(line.strip())
                    return
        print("Employee not found.")
    else:
        print("No records found.")

def update_employee(file_path, emp_id):
    if os.path.exists(file_path):
        lines = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if line.startswith(emp_id):
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                else:
                    file.write(line)
    else:
        print("No records found.")

def delete_employee(file_path, emp_id):
    if os.path.exists(file_path):
        lines = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if not line.startswith(emp_id):
                    file.write(line)
    else:
        print("No records found.")

def employee_manager():
    file_path = "employees.txt"
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
            add_employee(file_path)
        elif choice == '2':
            view_employees(file_path)
        elif choice == '3':
            emp_id = input("Enter Employee ID to search: ")
            search_employee(file_path, emp_id)
        elif choice == '4':
            emp_id = input("Enter Employee ID to update: ")
            update_employee(file_path, emp_id)
        elif choice == '5':
            emp_id = input("Enter Employee ID to delete: ")
            delete_employee(file_path, emp_id)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

#  Word Frequency Counter
import string

def create_sample_file():
    with open("sample.txt", 'w') as file:
        file.write(input("Enter text to create sample.txt: "))

def count_word_frequency(file_path):
    if not os.path.exists(file_path):
        create_sample_file()
    
    with open(file_path, 'r') as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    total_words = len(words)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top_5_words = sorted_word_count[:5]
    
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word} - {count} times")
    
    with open("word_count_report.txt", 'w') as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_5_words:
            report.write(f"{word} - {count}\n")

