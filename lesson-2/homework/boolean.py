# Boolean Data Type Questions

# 1.
username = input("Enter username: ")
password = input("Enter password: ")
print("Valid" if username and password else "Invalid")

# 2. 
print("Equal" if int(input("Enter first number: ")) == int(input("Enter second number: ")) else "Not equal")

# 3.
num = int(input("Enter a number: "))
print("Positive and even" if num > 0 and num % 2 == 0 else "Not positive or not even")

# 4. 
num1, num2, num3 = map(int, input("Enter three numbers: ").split())
print("All different" if len({num1, num2, num3}) == 3 else "Not all different")

# 5. 
print("Same length" if len(input("Enter first string: ")) == len(input("Enter second string: ")) else "Different length")

# 6.
num = int(input("Enter number: "))
print("Divisible by both" if num % 3 == 0 and num % 5 == 0 else "Not divisible by both")

# 7. 
print("Greater than 50" if (int(input("Enter first number: ")) + int(input("Enter second number: "))) > 50 else "Not greater than 50")

# 8.
num = int(input("Enter a number: "))
print("Within range" if 10 <= num <= 20 else "Out of range")

