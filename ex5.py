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

class CircularQueue: # implementation for 1
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        print("enqueue", item)

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        item = self.queue[self.head]
        print("dequeue", item)
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        print("peek", self.queue[self.head])
        return self.queue[self.head]

class Node: # Implementation for 2
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def toString(self):
        return str(self._value)

class CircularQueueLinkedList: # Implementation for 2
    def __init__(self, capacity):
        self.capacity = capacity
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.tail is None

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        new_node = Node(item)
        if self.is_empty():
            new_node.setNext(new_node)
            self.tail = new_node
        else:
            new_node.setNext(self.tail.getNext())
            self.tail.setNext(new_node)
            self.tail = new_node
        self.size += 1
        print("enqueue", item)

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        head = self.tail.getNext()
        print("dequeue", head.getData())
        if self.tail == head:
            self.tail = None
        else:
            self.tail.setNext(head.getNext())
        self.size -= 1
        return head.getData()

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        head = self.tail.getNext()
        print("peek", head.getData())
        return head.getData()

queue = CircularQueueLinkedList(6) # Implementation 3: You can test the linked-list version or CircularQueue version by changing the name

# 1. Peek, expected output: peek None
queue.peek()

# 2. Dequeue, expected output: dequeue None
queue.dequeue()

# 3. Enqueue 10, expected output: enqueue 10
queue.enqueue(10)

# 4. Peek, expected output: peek 10
queue.peek()

# 5. Enqueue 20, Expected output: enqueue 20
queue.enqueue(20)

# 6. Enqueue 30, expected output: enqueue 30
queue.enqueue(30)

# 7. Peek, expected output: peek 10
queue.peek()

# 8. Dequeue, expected output: dequeue 10
queue.dequeue()

# 9. Peek, Expected output: peek 20
queue.peek()

# 10. Enqueue 40, Expected output: enqueue 40
queue.enqueue(40)

# 11. Enqueue 50, Expected output: enqueue 50
queue.enqueue(50)

# 12. Enqueue 60, expected output: enqueue 60
queue.enqueue(60)

# 13. enqueue 70, Expected output: enqueue 70
queue.enqueue(70)

# 14. Peek, Expected output: peek 20
queue.peek()

# 15. Dequeue, Expected output: dequeue 20
queue.dequeue()

# 16. Enqueue 70, Expected output: enqueue 70
queue.enqueue(70)

# 17. Peek, Expected output: peek 30
queue.peek()

# 18. Dequeue, Expected output: dequeue 30
queue.dequeue()

# 19. Dequeue, expected output: dequeue 40
queue.dequeue()

# 20. Peek, Expected output: peek 50
queue.peek()

# 21. Enqueue 80, expected output: enqueue 80
queue.enqueue(80)

# 22. Enqueue 90, Expected output: enqueue 90
queue.enqueue(90)

# 23. enqueue 100, expected output: enqueue None
queue.enqueue(100)

# 24. Dequeue, Expected output: dequeue 50
queue.dequeue()

# 25. Peek, Expected output: peek 60
queue.peek()

# 26. Dequeue, Expected output: dequeue 60
queue.dequeue()

# 27. Dequeue, Expected output: dequeue 70
queue.dequeue()

# 28. Peek, Expected output: peek 70
queue.peek()

# 29. Dequeue, Expected output: dequeue 70
queue.dequeue()

# 30. Dequeue, Expected output: dequeue 80
queue.dequeue()

# 31. Peek, Expected output: peek 90
queue.peek()

# 32. Dequeue, Expected output: dequeue 90
queue.dequeue()

# 33. Enqueue 110, Expected output: enqueue 110
queue.enqueue(110)

# 34. Enqueue 120, Expected output: enqueue 120
queue.enqueue(120)

# 35. Peek, Expected output: peek 110
queue.peek()

# 36. Dequeue, Expected output: dequeue 110
queue.dequeue()

# 37. Dequeue, Expected output: dequeue 120
queue.dequeue()

# 38. Dequeue, Expected output: dequeue None
queue.dequeue()

# 39. Peek, Expected output: peek None
queue.peek()

# 40. Enqueue 130, Expected output: enqueue 130
queue.enqueue(130)
