# Tuple Tasks 

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 1
element = 1
count = tup.count(element)
print("Count occurrences:", count)

# 2
max_element = max(tup)
print("Max element:", max_element)

# 3
min_element = min(tup)
print("Min element:", min_element)

# 4
check = 3 in tup
print("Element present:", check)

# 5
first = tup[0] if tup else None
print("First element:", first)

# 6
last = tup[-1] if tup else None
print("Last element:", last)

# 7
length = len(tup)
print("Tuple length:", length)

# 8
sliced = tup[:3]
print("Sliced tuple (first 3):", sliced)

# 9
tup2 = (6, 7, 8)
concatenated = tup + tup2
print("Concatenated tuple:", concatenated)

# 10
is_empty = len(tup) == 0
print("Is tuple empty?:", is_empty)

# 11
indices = [i for i, v in enumerate(tup) if v == element]
print("Indices of element:", indices)

# 12
second_largest = sorted(set(tup), reverse=True)[1] if len(set(tup)) > 1 else None
print("Second largest:", second_largest)

# 13
second_smallest = sorted(set(tup))[1] if len(set(tup)) > 1 else None
print("Second smallest:", second_smallest)

# 14
single_tuple = (element,)
print("Single element tuple:", single_tuple)

# 15
lst = [1, 2, 3]
tuple_from_list = tuple(lst)
print("Tuple from list:", tuple_from_list)

# 16
is_sorted = all(tup[i] <= tup[i + 1] for i in range(len(tup) - 1))
print("Is tuple sorted?:", is_sorted)

# 17
start, end = 1, 4
max_subtuple = max(tup[start:end])
print("Max of subtuple:", max_subtuple)

# 18
min_subtuple = min(tup[start:end])
print("Min of subtuple:", min_subtuple)

# 19
value_to_remove = 1
new_tuple = tuple(v for i, v in enumerate(tup) if i != tup.index(value_to_remove)) if value_to_remove in tup else tup
print("Tuple after removing element:", new_tuple)

# 20
nested_tuple = tuple((tup[i:i+2]) for i in range(0, len(tup), 2))
print("Nested tuple:", nested_tuple)

# 21
repeated = tuple(item for item in tup for _ in range(2))
print("Repeated elements tuple:", repeated)

# 22
range_tuple = tuple(range(1, 11))
print("Range tuple:", range_tuple)

# 23
reversed_tuple = tup[::-1]
print("Reversed tuple:", reversed_tuple)

# 24
is_palindrome = tup == tup[::-1]
print("Is tuple palindrome?:", is_palindrome)

# 25
unique_elements = tuple(dict.fromkeys(tup))
print("Unique elements in order:", unique_elements)
