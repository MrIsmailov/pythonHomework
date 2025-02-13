# String Questions

# 1. 
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
age = 2025 - year_of_birth
print(f"Hello {name}, you are {age} years old.")

# 2. 
txt = 'LMaasleitbtui'
print(txt[::2])

# 3. 
user_string = input("Enter string: ")
print("Length:", len(user_string))
print("Uppercase:", user_string.upper())
print("Lowercase:", user_string.lower())

# 4. 
palindrome_string = input("Enter string: ")
print("Palindrome" if palindrome_string == palindrome_string[::-1] else "Not a palindrome")

# 5.
string_input = input("Enter string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string_input if char in vowels)
consonant_count = len([char for char in string_input if char.isalpha() and char not in vowels])
print("Vowel:", vowel_count, "Consonant:", consonant_count)

# 6.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Contains" if str2 in str1 else "Does not contain")

# 7. 
sentence = input("Enter sentence: ")
replace_word = input("Word : ")
new_word = input("New word: ")
print(sentence.replace(replace_word, new_word))

# 8. 
string = input("Enter string: ")
print("First:", string[0], "Last:", string[-1])

# 9.
print(input("Enter string: ")[::-1])

# 10. 
print("Word count:", len(input("Enter sentence: ").split()))

# 11. 
print("Contains digit" if any(char.isdigit() for char in input("Enter string: ")) else "No digits")

# 12.
words = input("Enter words separated by space: ").split()
char = input("Enter separator character: ")
print(char.join(words))

# 13. 
print(input("Enter string: ").replace(" ", ""))

# 14.
print("Equal" if input("Enter first string: ") == input("Enter second string: ") else "Not equal")

# 15.
print("".join(word[0].upper() for word in input("Enter a sentence: ").split()))

# 16. 
string = input("Enter string: ")
char_to_remove = input("Enter character to remove: ")
print(string.replace(char_to_remove, ""))

# 17.
print("".join('*' if char.lower() in 'aeiou' else char for char in input("Enter a string: ")))

# 18. 
string = input("Enter a sentence: ")
start = input("Enter starting word: ")
end = input("Enter ending word: ")
print("Matches" if string.startswith(start) and string.endswith(end) else "Does not match")
