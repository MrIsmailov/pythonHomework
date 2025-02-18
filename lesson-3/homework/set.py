#  Sets
# 1
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

# 2
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# 3
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# 4
is_subset = set1.issubset(set2)
print("Is Subset:", is_subset)

# 5
element = 3
is_element_in_set = element in set1
print("Element in Set:", is_element_in_set)

# 6
set_length = len(set1)
print("Set Length:", set_length)

# 7
lst = [1, 2, 2, 3, 4]
converted_set = set(lst)
print("Converted Set:", converted_set)

# 8
set1.discard(2)
print("Set after removing element:", set1)

# 9
set1.clear()
print("Cleared Set:", set1)

# 10
is_empty = len(set1) == 0
print("Is Set Empty:", is_empty)

# 11
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# 12
set1.add(6)
print("Set after adding element:", set1)

# 13
popped_element = set1.pop()
print("Popped Element:", popped_element)

# 14
set_of_numbers = {1, 2, 3, 4, 5}
max_element = max(set_of_numbers)
print("Maximum Element:", max_element)

# 15
min_element = min(set_of_numbers)
print("Minimum Element:", min_element)

# 16
even_numbers_set = {x for x in set_of_numbers if x % 2 == 0}
print("Even Numbers Set:", even_numbers_set)

# 17
odd_numbers_set = {x for x in set_of_numbers if x % 2 != 0}
print("Odd Numbers Set:", odd_numbers_set)

# 18
range_set = set(range(1, 11))
print("Range Set:", range_set)

# 19
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged_set = set(list1).union(list2)
print("Merged and Deduplicated Set:", merged_set)

# 20
set1 = {1, 2, 3}
set2 = {4, 5, 6}
are_disjoint = set1.isdisjoint(set2)
print("Are Disjoint Sets:", are_disjoint)

# 21
lst_with_duplicates = [1, 2, 2, 3, 4]
unique_list = list(set(lst_with_duplicates))
print("List without Duplicates:", unique_list)

# 22
unique_count = len(set(lst_with_duplicates))
print("Count of Unique Elements:", unique_count)

# 23
import random
random_set = {random.randint(1, 100) for _ in range(10)}
print("Random Set:", random_set)