class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue: 

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
            self.tail.next, self.tail = t, t
        return self

    def pop(self):
        if self.head == None:
            return None
        node, self.head = self.head, self.head.next
        return node

queue = Queue()
queue.push(0)
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop().value)
print(queue.pop().value)

print(queue)