import math

class ArrayQueue:
    def __init__(self, capacity):
        if capacity<=0:
            capacity = 4
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def __str__(self):
        return "%s" % self.queue

    def push(self, item):
        if self.count + 1 >= self.capacity:
            self._resize()
        self.queue[self.tail] = item
        self.tail = (self.tail+1) % self.capacity
        self.count += 1
    
    def pop(self):
        if self.head == self.tail:
            return None
        res = self.queue[self.head] 
        self.queue[self.head] = None
        self.head = (self.head + 1 ) % self.capacity
        self.count -= 1
        return res

    def _resize(self):
        newCapacity = math.floor(self.capacity*1.5)
        tmpQueue = [None]*newCapacity
        i = 0
        if self.head < self.tail:
            for x in range(self.head, self.tail):
                tmpQueue[i], i = self.queue[x], i+1
        else:
            for x in range(self.head, self.capacity):
                tmpQueue[i], i = self.queue[x], i + 1
            for x in range(0, self.tail):
                tmpQueue[i], i = self.queue[x], i + 1

        self.head = 0
        self.tail = i
        self.queue = tmpQueue
        self.capacity = newCapacity

arrayQueue = ArrayQueue(3)
arrayQueue.push(1)
arrayQueue.push(2)
arrayQueue.push(3)
print("popped")
print(arrayQueue.pop())
print(arrayQueue.pop())
arrayQueue.push(5)
arrayQueue.push(6)
arrayQueue.push(7)
print(arrayQueue.pop())
print(arrayQueue.pop())
arrayQueue.push(8)
arrayQueue.push(9)

print(arrayQueue)