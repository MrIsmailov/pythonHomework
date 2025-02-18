my_list = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5]

# 1. 
element = 2
count = my_list.count(element)
print("Count Occurrences:", count)

# 2. 
total = sum(my_list)
print("Sum of Elements:", total)

# 3.
maximum = max(my_list)
print("Max Element:", maximum)

# 4. 
minimum = min(my_list)
print("Min Element:", minimum)

# 5. 
exists = 3 in my_list
print("Check Element:", exists)

# 6. 
first = my_list[0] if my_list else None
print("First Element:", first)

# 7. 
last = my_list[-1] if my_list else None
print("Last Element:", last)

# 8. 
sliced = my_list[:3]
print("Slice List (First 3):", sliced)

# 9.
reversed_list = my_list[::-1]
print("Reverse List:", reversed_list)

# 10. 
sorted_list = sorted(my_list)
print("Sort List:", sorted_list)

# 11. 
unique_list = list(dict.fromkeys(my_list))
print("Remove Duplicates:", unique_list)

# 12. 
my_list.insert(2, 99)
print("Insert Element at index 2:", my_list)

# 13. 
index = my_list.index(3) if 3 in my_list else -1
print("Index of Element 3:", index)

# 14.
is_empty = len(my_list) == 0
print("Check for Empty List:", is_empty)

# 15. 
even_count = sum(1 for x in my_list if x % 2 == 0)
print("Count Even Numbers:", even_count)

# 16.
odd_count = sum(1 for x in my_list if x % 2 != 0)
print("Count Odd Numbers:", odd_count)

# 17. 
list2 = [6, 7, 8]
concatenated = my_list + list2
print("Concatenate Lists:", concatenated)

# 18. 
sublist = [2, 3]
found_sublist = str(sublist) in str([my_list[i:i+len(sublist)] for i in range(len(my_list)-len(sublist)+1)])
print("Find Sublist:", found_sublist)

# 19. 
old_element, new_element = 3, 30
if old_element in my_list:
    my_list[my_list.index(old_element)] = new_element
print("Replace Element:", my_list)

# 20. 
second_largest = sorted(set(my_list))[-2] if len(set(my_list)) > 1 else None
print("Find Second Largest:", second_largest)

# 21.
second_smallest = sorted(set(my_list))[1] if len(set(my_list)) > 1 else None
print("Find Second Smallest:", second_smallest)

# 22. 
even_numbers = [x for x in my_list if x % 2 == 0]
print("Filter Even Numbers:", even_numbers)

# 23.
odd_numbers = [x for x in my_list if x % 2 != 0]
print("Filter Odd Numbers:", odd_numbers)

# 24.
length = len(my_list)
print("List Length:", length)

# 25. 
copy_list = my_list[:]
print("Create a Copy:", copy_list)

# 26.
mid = len(my_list) // 2
middle_element = my_list[mid] if len(my_list) % 2 != 0 else my_list[mid-1:mid+1]
print("Get Middle Element:", middle_element)

# 27.
start, end = 2, 5
max_sublist = max(my_list[start:end+1]) if start < len(my_list) and end < len(my_list) else None
print("Find Maximum of Sublist:", max_sublist)

# 28.
min_sublist = min(my_list[start:end+1]) if start < len(my_list) and end < len(my_list) else None
print("Find Minimum of Sublist:", min_sublist)

# 29. 
index_to_remove = 3
if 0 <= index_to_remove < len(my_list):
    my_list.pop(index_to_remove)
print("Remove Element by Index:", my_list)

# 30. 
is_sorted = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
print("Check if List is Sorted:", is_sorted)

# 31.
repeat_count = 2
repeated_list = [x for x in my_list for _ in range(repeat_count)]
print("Repeat Elements:", repeated_list)

# 32.
merged_sorted = sorted(my_list + list2)
print("Merge and Sort:", merged_sorted)

# 33. 
element_to_find = 2
all_indices = [i for i, x in enumerate(my_list) if x == element_to_find]
print("Find All Indices:", all_indices)

# 34. 
rotate_by = 2
rotated_list = my_list[-rotate_by:] + my_list[:-rotate_by]
print("Rotate List:", rotated_list)

# 35. 
range_list = list(range(1, 11))
print("Create Range List:", range_list)

# 36.
sum_positive = sum(x for x in my_list if x > 0)
print("Sum of Positive Numbers:", sum_positive)

# 37. 
sum_negative = sum(x for x in my_list if x < 0)
print("Sum of Negative Numbers:", sum_negative)

# 38. 
is_palindrome = my_list == my_list[::-1]
print("Check Palindrome:", is_palindrome)

# 39. 
chunk_size = 3
nested_list = [my_list[i:i+chunk_size] for i in range(0, len(my_list), chunk_size)]
print("Create Nested List:", nested_list)

# 40.
unique_ordered = []
for x in my_list:
    if x not in unique_ordered:
        unique_ordered.append(x)
print("Get Unique Elements in Order:", unique_ordered)
