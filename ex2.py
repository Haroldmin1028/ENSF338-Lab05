import sys, timeit, numpy as np
sys.setrecursionlimit(20000)
 
class PQueue_Mergesort:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1
    def get_size(self):
        if self.head == -1:
            return 0
        elif self.tail >= self.head:
            return self.tail - self.head + 1
        else:
            return self.capacity - self.head + self.tail + 1
    def enqueue(self, element):
        if (self.tail + 1) % self.capacity == self.head:
            return
        elif self.head == -1:
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = element
        self.mergesort(self.queue,  0, self.get_size() - 1)
    def dequeue(self):
        if self.head == -1:
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return item
    def mergesort(self, arr, low, high):
        if low < high:
            mid = int((low + high)/2)
            self.mergesort(arr, low, mid)
            self.mergesort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)

    def merge(self, arr, low, mid, high):
        leftarr = [arr[i] for i in range(low, mid + 1)]
        rightarr = [arr[i] for i in range(mid + 1, high + 1)]
    
        i = 0     
        j = 0     
        k = low    

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] <= rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1

        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1
        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1

class PQueue_Insert:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    def get_size(self):
        return len(self.queue)
    def enqueue(self, element):
        if self.get_size() == self.capacity:
            return
        for i in range(self.get_size()):
            if element < self.queue[i]:
                self.queue.insert(i, element)
                return
        self.queue.append(element)
    def dequeue(self):
        if self.get_size() == 0:
            return None
        return self.queue.pop(0)

def randomlist():
    return ['enqueue' if np.random.randint(1, 10) > 3 else 'dequeue' for x in range(1000)]

def queue(pqueue, tasks):
    for task in tasks:
        if task == 'enqueue':
            pqueue.enqueue(np.random.randint(1, 800))
        else:
            pqueue.dequeue()

def main():
    queuemerge = queueinsert = 0
    priorityqueue1 = PQueue_Mergesort(7000)
    priorityqueue2 = PQueue_Insert(7000)

    for i in range(1, 11):
        if i % 10 == 0:
            print(f"Performing tasks for {i}th time...")
        queuemerge += timeit.timeit(lambda: queue(priorityqueue1, randomlist()), number = 1)
        queueinsert += timeit.timeit(lambda: queue(priorityqueue2, randomlist()), number = 1)
    print(f"Priority queue with mergesort: {queuemerge}s\nPriority queue with insert: {queueinsert}s")

if __name__ == "__main__":
    main()

"""
5.  Priority queue with insert is much faster than with mergesort. For the mergesort implementation, every enqueue runs a costly O(n log n) mergesort, whereas the insert implementation only does a O(n) linear search to find the correct position to insert. The mergesort also has a larger amount of time it is guaranteed to spend with the split and merge than the linear search which has a decrease in time spent when the element to enqueue is a small number.
"""
