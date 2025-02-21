# Task 1: 
def convert_cel_to_far(celsius):
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

fahrenheit = float(input("Enter a temperature in degrees F: "))
celsius = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit} degrees F = {celsius} degrees C")


celsius = float(input("Enter a temperature in degrees C: "))
fahrenheit = convert_cel_to_far(celsius)
print(f"{celsius} degrees C = {fahrenheit} degrees F")

# Task 2: 
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of return (as a decimal): "))
years = int(input("Enter the number of years: "))
invest(principal, rate, years)

# Task 3:
def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

number = int(input("Enter a positive integer: "))
factors(number)

# Task 4: 
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    sorted_values = sorted(values)
    mid = len(values) // 2
    if len(values) % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]

enrollments, tuitions = enrollment_stats(universities)
total_students = sum(enrollments)
total_tuition = sum(tuitions)
student_mean = mean(enrollments)
student_median = median(enrollments)
tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("******************************")

# Task 5: 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number to check if it is prime: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")