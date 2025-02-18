# Task 1
list1 = [1, 1, 2]
list2 = [2, 3, 4]
uncommon_elements = list1 + list2
for element in set(list1).intersection(set(list2)):
    uncommon_elements = [x for x in uncommon_elements if x != element]
print("Uncommon elements:", uncommon_elements)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
uncommon_elements = list1 + list2
for element in set(list1).intersection(set(list2)):
    uncommon_elements = [x for x in uncommon_elements if x != element]
print("Uncommon elements:", uncommon_elements)

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
uncommon_elements = list1 + list2
for element in set(list1).intersection(set(list2)):
    uncommon_elements = [x for x in uncommon_elements if x != element]
print("Uncommon elements:", uncommon_elements)

# Task 2: 
n = 5
for i in range(1, n):
    print(i * i)

# Task 3: 
txt = "hello"
result = []
vowels = "aeiou"
for i, char in enumerate(txt):
    result.append(char)
    if (i + 1) % 3 == 0 or char in vowels:
        result.append('_')
print("".join(result).rstrip('_'))

txt = "assalom"
result = []
for i, char in enumerate(txt):
    result.append(char)
    if (i + 1) % 3 == 0 or char in vowels:
        result.append('_')
print("".join(result).rstrip('_'))

txt = "abcabcdabcdeabcdefabcdefg"
result = []
for i, char in enumerate(txt):
    result.append(char)
    if (i + 1) % 3 == 0 or char in vowels:
        result.append('_')
print("".join(result).rstrip('_'))

# Task 4: 
import random

def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 10
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("You guessed it right!")
            return
        attempts -= 1
    print("You lost. Want to play again?")
    play_again = input().lower()
    if play_again in ['y', 'yes', 'ok']:
        number_guessing_game()

number_guessing_game()

# Task 5: 
password = input("Enter a password: ")
if len(password) < 8:
    print("Password is too short.")
elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")

# Task 6: 
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)