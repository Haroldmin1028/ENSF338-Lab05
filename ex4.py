import timeit, numpy as np, matplotlib.pyplot as plt

class Queue_Array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    def get_size(self):
        return len(self.queue)
    def enqueue(self, element):
        if self.get_size() == self.capacity:
            return
        self.queue.insert(0, element)
    def dequeue(self):
        if self.get_size() == 0:
            return None
        return self.queue.pop()

class Node:
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

class Queue_LL:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self, node):
        if self.head is not None:
            node.setNext(self.head)
        elif self.head is None:
            self.tail = node
        self.head = node
    def dequeue(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            element = self.tail.getData()
            self.head = self.tail = None
            return element
        else:
            current = self.head
            while current.getNext() != self.tail:
                current = current.getNext()
            element = self.tail.getData()
            self.tail = current
            self.tail.setNext(None)
            return element        

def randomlist():
    return ['enqueue' if np.random.randint(1, 10) > 3 else 'dequeue' for x in range(10000)]

def queue(queue, tasks):
    for task in tasks:
        if task == 'enqueue':
            queue.enqueue(Node(np.random.randint(10000)))
        else:
            queue.dequeue()

def main():
    arraytimelist, lltimelist, arraytime, lltime = [], [], 0, 0
    arrayqueue = Queue_Array(70000)
    llqueue = Queue_LL()

    for i in range(1, 101):
        if i % 10 == 0:
            print(f"Performing tasks for {i}th time...")
        arraytimeone = timeit.timeit(lambda: queue(arrayqueue, randomlist()), number = 1)
        arraytime += arraytimeone
        arraytimelist.append(arraytimeone)
        lltimeone = timeit.timeit(lambda: queue(llqueue, randomlist()), number = 1)
        lltime += lltimeone
        lltimelist.append(lltimeone)
    print(f"Queue using array: {arraytime}s\nQueue using singly linked list: {lltime}s")

    plt.subplot(1, 2, 1)
    plt.xlabel("Times")
    plt.ylabel("Frequency")
    plt.title("Queue Array Performance")   
    plt.hist(arraytimelist, bins = 20)
    plt.subplot(1, 2, 2)
    plt.xlabel("Times")
    plt.ylabel("Frequency")
    plt.title("Queue Linked List Performance")   
    plt.hist(lltimelist, bins = 20)
    plt.show()

if __name__ == "__main__":
    main()

"""
This exercise was completed before the edit in the assignment, and implements the queue as a singly linked list with a tail pointer.
5.  The array implementation of the queue performed better than the linked list implementation. The linked list implementation had a fatal flaw in the dequeuing process, where it was needed to traverse through the whole list each time to find the penultimate node, costing O(n). The tail pointer did not improve the performance of the linked list because it was a singly linked list. The enqueuing and dequeuing processes of the array implementation were both O(1).
"""