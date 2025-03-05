class MyArrayStack:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
        # Note that in Python "not <list>" evaluates to True if the list is empty
        if not self._storage:
            return None
        else:
            return self._storage.pop()
    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]

def calculate(user_input):
    length = len(user_input)
    new_array = MyArrayStack()

    for i in range (0, length):
        if (user_input[i] == '('):
            calculate(user_input)
        else:
            continue

    return 0

def main():
    '''
    An S-expression is of the form (o e1 e2) where o is the operand and e1 and e2 are 
    S-expressions.
    The arithmetic expression "2+3*5" would be written as an S-expression like this:
    (+ 2 (* 3 5)) where + is the operand, 2 and (* 3 5) are the S-expressions. 
    For (* 3 5), * is the operand and 3 and 5 are the S-expressions.

    Maybe do some recursion since we can have nested S-expressions?
    Can we assume that the inputs will be in correct format? As in we don't have to put 
    out a message for the cases where the user does not provide an input in the correct format.
    '''

    print('\nAn S-expression is of the form (o e1 e2) where o is the operand (+,-,*,/), and e1 and e2 are S-expressions.\n')
    user_input = input('Please enter an S-expression: ')
    MyArrayStack.push(user_input)
    print('stuff')

    calculate(user_input)

    return 0

if __name__ == '__main__':
    main()