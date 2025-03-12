"""
Implementation of a circular queue:

Requirement 1:
The circular queue should provide the following methods:
    • enqueue adds an item to the queue and prints “enqueue <element>” to terminal
    • dequeue removes and returns the front-most item in the queue and prints “dequeue
    <element>” to terminal
    • peek just returns the front-most item in the queue without removing it and prints
    “peek <element>” to terminal

• Requirement 2: 
The queue should print “dequeue None” or “peek None” if
you try to dequeue or peek from an empty queue.

• Requirement 4: The queue should print “enqueue None” if you try to to
enqueue into a full queue
--------------------------------------------------------------------------------------------------

1. Implement such a queue based on a fixed-size Python array [0.4 pts]
2. Implement the queue again, this time using a circular linked list [0.4 pts]
3. Generate a list of 40 operations, together with expected output, that can
be used to test correctness of implementation. [0.2 pts]
    • The list must include multiple peek, enqueue, dequeue operations. It should test
    regular operations and all corner cases (enqueue into full queue, peek into empty
    queue, push into empty queue)
    • The list can be implemented directly as Python code, e.g.:
    Mylist.enqueue(1)
    Mylist.dequeue()
    ...
"""