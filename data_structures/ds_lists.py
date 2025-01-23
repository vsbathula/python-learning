"""
Lists
In Python, lists are the most commonly used data structure. Lists are ordered, mutable, and can store elements of any type.

Key Operations:
Indexing: Accessing elements by position.
Appending: Adding elements at the end.
Popping: Removing elements from the end.
Slicing: Accessing a subset of the list.
Insertion: Inserting an element at a specific position.
Length: Getting the number of elements.
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing the list
print(f'Sliced list: {numbers[1:4]}')

# Appending an element
numbers.append(10)
print(f'Appended list: {numbers}')

# Popping an element
numbers.pop()
print(f'Popped list: {numbers}')

# Insert element based on index
numbers.insert(10, 10)
print(f'Insert element based on index: {numbers}')

# Remove element based on index
numbers.remove(10)
print(f'Remove element based on index: {numbers}')

# Get every other element
print(f'Every other element in list: {numbers[::3]}')

# Reverse the list
print(f'Reversed list: {numbers[::-1]}')

# Sorting in Ascending Order
numbers.sort()
print(f'Sort in Ascending Order: {numbers}')

# Sorting in Descending Order
numbers.sort(reverse=True)
print(f'Sort in Descending Order: {numbers}')

# Reverse the list
numbers.reverse()
print(f'Reversed list: {numbers}')

a = ["apple", "banana", "kiwi", "cherry"]

# The key=len tells the sort() method to use length of each string during sorting
a.sort(key=len)
print(f'The key=len tells the sort() method to use length of each string during sorting: {a}')

# The key=str.lower tells the sort() to perform a case insensitive sort
a.sort(key=str.lower)
print(f'The key=str.lower tells the sort() to perform a case insensitive sort: {a}')
