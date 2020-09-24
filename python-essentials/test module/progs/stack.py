class Stack:
    def __init__(self):
        self.__stk = []

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

    def push(self, val):
        self.__stk.append(val)

class AddingStack:
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def getSum(self):
        return self.__sum

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
        
stack = AddingStack()
for i in range(5):
    stack.push(i)
print(stack.getSum())
print(stack.__dict__)
for i in range(5):
    print(stack.pop())
