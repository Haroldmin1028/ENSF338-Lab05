import sys, timeit, numpy as np
sys.setrecursionlimit(20000)

class PQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = -1
        self.tail = -1
    def dequeue(self):
        if self.head == -1:
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return item

class PQueue_Mergesort(PQueue):
    def enqueue(self, element):
        if (self.tail + 1) % self.capacity == self.head:
            return
        elif self.head == -1:
            self.head = self.tail = 0

    def mergesort(arr, low, high):
        if low < high:
            mid = (low + high)/2
            PQueue_Mergesort.mergesort(arr, low, mid)
            PQueue_Mergesort.mergesort(arr, mid + 1, high)
            PQueue_Mergesort.merge(arr, low, mid, high)

    def merge(arr, low, mid, high):
        leftarr = []
        rightarr = []

        for i in range(low, mid-low+1):
            leftarr[i] = arr[low + i]
        for j in range(mid + 1, high + 1):
            rightarr[j] = arr[mid + 1 + j]
    
        i = 0     
        j = 0     
        k = low    

        while i < (mid - low + 1) and j < (mid + 1 + j):
            if leftarr[i] <= rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1
        while i < (mid - low + 1):
            arr[k] = leftarr[i]
            i += 1
            k += 1
        while j < (mid + 1 + j):
            arr[k] = rightarr[j]
            j += 1
            k += 1

class PQueue_Insert(PQueue):
    def enqueue(self, element):
        pass

    

def randomlist():
    return ['enqueue' if np.random.randint(1, 10) > 3 else 'dequeue' for x in range(1000)]

def queue(pqueue, tasks):
    for task in tasks:
        if task == 'enqueue':
            pqueue.enqueue()
        else:
            pqueue.dequeue()

def main():
    queuemerge, queueinsert = 0
    priorityqueue1 = PQueue_Mergesort(1200)
    priorityqueue2 = PQueue_Insert(1200)

    for i in range(100):
        if i % 20 == 0:
            print(f"Performing tasks for {i}th time...")
        queuemerge += timeit.timeit(lambda: queue(priorityqueue1, randomlist()))
        queueinsert += timeit.timeit(lambda: queue(priorityqueue2, randomlist()))
    print(f"Priority queue with mergesort: {queuemerge}s\nPriority queue with insert: {queueinsert}s")

if __name__ == "__main__":
    main()

"""
5.  
"""
