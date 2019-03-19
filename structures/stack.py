class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack: 

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur = self.head
        s = "["
        while cur:
            s+=" %s " % cur.value
            cur = cur.next
        s+="]"
        return s

    def push(self, value):
        t = Node(value)
        if self.head == None:
            self.head, self.tail = t,t
        else:
            t.next, self.head = self.head, t
        return self

    def pop(self):
        if self.head == None:
            return None
        node, self.head = self.head, self.head.next
        return node

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop().value)
print(stack.pop().value)

print(stack)