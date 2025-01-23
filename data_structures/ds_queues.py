"""
Queue
A queue is a FIFO (First In, First Out) data structure. The first element added to the queue is the first one to be removed.
You can implement a queue using a list or the collections.deque class for better performance.

Key Operations:
Enqueue: Add an element to the end of the queue.
Dequeue: Remove and return the front element from the queue.
Peek: View the front element without removing it.
is_empty: Check if the queue is empty.

Note: deque is more efficient than lists for queues, as removing elements from the front of a list takes O(n) time, while deque is O(1).
"""

from collections import deque

# Queue implementation using deque
queue = deque()

# Enqueueing elements
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeuing an element
print(queue.popleft())  # Output: 1

# Peek front element
print(queue[0])