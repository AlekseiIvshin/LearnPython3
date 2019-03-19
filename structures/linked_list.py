class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, value):
        self.head = LinkedListNode(value)
        self.tail = self.head
    
    def addLast(self, value):
        next = LinkedListNode(value)
        next.prev = self.tail
        self.tail.next = next
        self.tail = next
        return self

    def popLast(self):
        last, self.tail = self.tail, self.tail.prev
        self.tail.next = None
        return last
    
    def addFirst(self, value):
        prev = LinkedListNode(value)
        self.head.prev = prev
        prev.next = self.head
        self.head = prev
        return self

    def popFirst(self):
        first, self.head = self.head, self.head.next
        self.head.prev = None
        return first

    def atIndex(self, index):
        cur = self.head
        i = 0
        while cur and i < index:
            cur = cur.next
            i += 1
        return cur

    @staticmethod
    def forEach(linked_list, predicate):
        cur = linked_list.head
        while cur:
            predicate(cur)
            cur = cur.next

    @staticmethod
    def printNode(node):
        print(node.value)

    @staticmethod 
    def print(linked_list):
        s = "["
        def appendValue(node):
            nonlocal s
            s+=" %s " % node.value
        LinkedList.forEach(linked_list, appendValue)
        s+="]"
        print(s)

head = LinkedList(1).addLast(2).addFirst(0).addFirst(-1).addLast(3)
LinkedList.printNode(head.popLast())
LinkedList.printNode(head.popFirst())
LinkedList.printNode(head.popLast())


LinkedList.print(head)

LinkedList.printNode(head.atIndex(1))