import sys, timeit, numpy as np
sys.setrecursionlimit(20000)

class PQueue:
    def dequeue(self):
        if self.head == -1:
            return None
        else:
            pass

class PQueue_Mergesort(PQueue):
    def __init__(self, capacity):
        self.capacity = capacity
    def enqueue(self, element):
        pass
    def mergesort(arr, low, high):
        if low < high:
            mid = (low + high)/2
            PQueue_Mergesort.mergesort(arr, low, mid)
            mergesort(arr, mid + 1, high)
            merge(arr, low, mid, high)
    def merge(arr, low, mid, high):
        leftarr = []
        rightarr = []
        for i in range(low, mid - low + 1):
            leftarr[i] = arr[low + i]
        for j in range(mid + 1, high + 1):
            rightarr[j] = arr[mid + 1 + j] 

class PQueue_Insert(PQueue):
    def __init__(self, capacity):
        self.capacity = capacity
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
    priorityqueue1 = PQueue_Mergesort(5)
    priorityqueue2 = PQueue_Insert(4)

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
