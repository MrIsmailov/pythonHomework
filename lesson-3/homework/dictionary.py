# DICTIONARY
# 1
dictionary = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
value = dictionary.get(key, 'Key not found')
print("Value:", value)

# 2
key = 'a'
is_key_present = key in dictionary
print("Is Key Present:", is_key_present)

# 3
key_count = len(dictionary)
print("Number of Keys:", key_count)

# 4
keys_list = list(dictionary.keys())
print("All Keys:", keys_list)

# 5
values_list = list(dictionary.values())
print("All Values:", values_list)

# 6
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)

# 7
key_to_remove = 'b'
if key_to_remove in dictionary:
    del dictionary[key_to_remove]
print("Dictionary after removing key:", dictionary)

# 8
dictionary.clear()
print("Cleared Dictionary:", dictionary)

# 9
is_empty = len(dictionary) == 0
print("Is Dictionary Empty:", is_empty)

# 10
dictionary = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
key_value_pair = (key, dictionary[key]) if key in dictionary else 'Key not found'
print("Key-Value Pair:", key_value_pair)

# 11
dictionary['a'] = 10
print("Updated Dictionary:", dictionary)

# 12
value_to_count = 2
value_occurrences = list(dictionary.values()).count(value_to_count)
print("Value Occurrences:", value_occurrences)

# 13
inverted_dict = {v: k for k, v in dictionary.items()}
print("Inverted Dictionary:", inverted_dict)

# 14
value_to_find = 3
keys_with_value = [k for k, v in dictionary.items() if v == value_to_find]
print("Keys with Value:", keys_with_value)

# 15
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))
print("Dictionary from Lists:", dict_from_lists)

# 16
has_nested_dict = any(isinstance(v, dict) for v in dictionary.values())
print("Has Nested Dictionary:", has_nested_dict)

# 17
nested_dict = {'a': {'nested_key': 'nested_value'}}
nested_value = nested_dict['a'].get('nested_key', 'Key not found')
print("Nested Value:", nested_value)

# 18
from collections import defaultdict
default_dict = defaultdict(lambda: 'default_value')
default_dict['a'] = 1
print("Default Dictionary:", default_dict['b'])

# 19
unique_values_count = len(set(dictionary.values()))
print("Count of Unique Values:", unique_values_count)

# 20
sorted_by_key = dict(sorted(dictionary.items()))
print("Sorted by Key:", sorted_by_key)

# 21
sorted_by_value = dict(sorted(dictionary.items(), key=lambda item: item[1]))
print("Sorted by Value:", sorted_by_value)

# 22
filtered_dict = {k: v for k, v in dictionary.items() if v > 1}
print("Filtered Dictionary:", filtered_dict)

# 23
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
common_keys = set(dict1.keys()).intersection(dict2.keys())
print("Common Keys:", common_keys)

# 24
tuple_of_pairs = (('a', 1), ('b', 2))
dict_from_tuple = dict(tuple_of_pairs)
print("Dictionary from Tuple:", dict_from_tuple)

# 25
first_key_value_pair = next(iter(dictionary.items()))
print("First Key-Value Pair:", first_key_value_pair)