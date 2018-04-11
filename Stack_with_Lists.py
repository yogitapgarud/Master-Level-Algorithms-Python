class Stack:
        def __init__(self):
                self.stack = []

        def push(self, x):
                self.stack.append(x)

        def pop(self):
                if len(self.stack) > 0:
                        x = self.stack.pop()
                        return x
                else:
                        return False

        def peek(self):
                if len(self.stack) > 0:
                        x = self.stack[-1]
                        return x
                else:
                        return False

        def isEmpty(self):
                if len(self.stack) > 0:
                        return False
                return True

        def size(self):
                return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(5)
print("stack peek: ", stack.peek())
stack.push(10)
print("stack peek: ", stack.peek())

while not stack.isEmpty():
        print("stack pop: ", stack.pop())

print("popping: ", stack.pop())
