import sys

class MyArrayStack:
    def __init__(self):
        self._storage = []
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


def calculate(expression_array):
    stack = MyArrayStack()
    operands = ['+', '-', '*', '/']
    
    for element in reversed(expression_array):
        if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
            stack.push(int(element))
        elif element in operands:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if element == '+':
                stack.push(operand1 + operand2)
            elif element == '-':
                stack.push(operand1 - operand2)
            elif element == '*':
                stack.push(operand1 * operand2)
            elif element == '/':
                stack.push(operand1 // operand2)  
    
    return stack.pop()


def search(expression):
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    expression_array = expression.split()

    return calculate(expression_array)


def main():
    expression = sys.argv[1]
    result = search(expression)
    print(result)


if __name__ == "__main__":
    main()
