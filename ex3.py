"""
1. Implement a stack which internally uses Python arrays. push() must append an element at the tail,
and pop must remove an element from the end of the tail.

2. Implement a stack which internally uses a singly-linked list. push() must add an element at the head,
and pop() must remove the head element.

3. Write a function which generates random list of 10,000 stack operations. Either push with a 0.7 probability or pop with a 0.3 probability

4. Measure the performance time for each implementation to process 100 list (each with 10,000 elements) operations

5. Plot the distribution of times (distributions for each implementation
should be overlayed in the same plot; make sure to use consistent
ranges) and discuss the results.
"""
import timeit
import array
import random
import matplotlib.pyplot as plt

class InternalPythonArray: # Implementation for 1
    def __init__(self, typecode="i"):
        self._storage = array.array(typecode)

    def push(self, value):
        self._storage.append(value)

    def pop(self):
        if not self._storage:
            return None
        else:
            return self._storage.pop()

    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]


class ListNode: # Implementation for 2
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

class InternalSinglyLinkedList: # Implementation for 2
    def __init__(self):
        self.head = None
    def push(self, value):
        new_node = ListNode(value)
        new_node.setNext(self.head)
        self.head = new_node
    def pop(self):
        if self.head is None:
            return None
        popped_value = self.head.getData()
        self.head = self.head.getNext()
        return popped_value



def tasks_list(size=10000): # Implementation for 3
    tasks = []
    for i in range(size):
        if random.random() < 0.7:
            tasks.append(("push", random.randint(1, 100))) # Note we append tuples
        else:
            tasks.append(("pop",)) # extra comma is to make sure the last added tuple gets removed. It has to be a tuple
    return tasks

def execution(stack, task_list): # Implementation for 4
    for task in task_list:
        if task[0] == "push":
            stack.push(task[1])
        elif task[0] == "pop":
            stack.pop()

task_lists = [tasks_list() for i in range(100)]

array_time = timeit.timeit( # implementation for 4
    lambda: [execution(InternalPythonArray(), task_list) for task_list in task_lists], number=1

)

linked_list_time = timeit.timeit( # implementation for 4
    lambda: [execution(InternalSinglyLinkedList(), task_list) for task_list in task_lists], number=1
)

print(f"Array Stack Time: {array_time} seconds")
print(f"Linked-List stack Time: {linked_list_time} seconds")


    
# implementation for 5 starts here

num_runs = 10

array_stack_plot_times = [
    timeit.timeit(
        lambda: [execution(InternalPythonArray(), task_list) for task_list in task_lists], 
        number=1
    )
    for i in range(num_runs)
]

linked_list_stack_plot_times = [
    timeit.timeit(
        lambda: [execution(InternalSinglyLinkedList(), task_list) for task_list in task_lists], 
        number=1
    )
    for i in range(num_runs)
]

plt.figure(figsize=(10,6))
plt.hist(array_stack_plot_times, bins=8, alpha=0.6, color='blue', edgecolor='black', label="Array Stack")
plt.hist(linked_list_stack_plot_times, bins=8, alpha=0.6, color='red', edgecolor='black', label="Linked-List Stack")

plt.xlabel("Execution Time (seconds)", fontsize=12)
plt.ylabel("Frequency (Number of Runs)", fontsize=12)
plt.title("Execution Time Distribution: Array Stack vs Linked List Stack", fontsize=14)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()



