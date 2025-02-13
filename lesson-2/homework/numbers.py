# Number Data Type Questions

# 1. 
num = float(input("Enter a float number: "))
print(round(num, 2))

# 2. 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("Largest:", max(num1, num2, num3))
print("Smallest:", min(num1, num2, num3))

# 3. 
km = float(input("Enter distance in kilometers: "))
print("Meters:", km * 1000)
print("Centimeters:", km * 100000)

# 4. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Quotient:", a // b)
print("Remainder:", a % b)

# 5. 
celsius = float(input("Enter temperature: "))
print("Fahrenheit:", (celsius * 9/5) + 32)

# 6. 
number = int(input("Enter number: "))
print("Last digit:", number % 10)

# 7. 
even_check = int(input("Enter number: "))
print("Even" if even_check % 2 == 0 else "Odd")

