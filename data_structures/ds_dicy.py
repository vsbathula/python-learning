"""
Hashmaps (Dictionaries)
A hashmap (or dictionary in Python) is a collection of key-value pairs.
It provides fast lookup, insertion, and deletion by using a hash function to compute an index into an array of buckets or slots.

Key Operations:
Insert: Add a key-value pair.
Lookup: Find a value by key.
Delete: Remove a key-value pair.
Update: Modify an existing value.
"""
import json


my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(f'Dict : {json.dumps(my_dict, indent=4)}')

# Inserting a new key-value pair
my_dict['date'] = 4
print(f'Inserted new key value pair : {json.dumps(my_dict, indent=4)}')

# Lookup
print(my_dict['banana'])  # Output: 2

# Updating a value
my_dict['banana'] = 5
print(my_dict['banana'])  # Output: 5

# Deleting a key-value pair
del my_dict['apple']
print(my_dict)
