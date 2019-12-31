class Stack():
    """docstring for ClassName"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()

for c in "Hello":
    stack.push(c)

reverse = ""

for i in range(len(stack.items)):
    reverse += stack.pop()

stack.push(1)
item = stack.pop()

print(item)

print(reverse)
print(stack.is_empty())
print(stack.size())



class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a_queue = Queue()
print(a_queue.is_empty())

for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())


for i in range(5):
    print(a_queue.dequeue())

print(a_queue.size())

class Test():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

test1 = Test()
reverse = ""

for i in "yesterday":
    test1.push(i)

for i in range(len(test1.items)):
    reverse += test1.pop()

print(reverse)

test2 = Test()
list1 = []
for i in [1, 2, 3, 4, 5]:
    test2.push(i)

for i in range(len(test2.items)):
    list1.append(test2.pop())

print(list1)
