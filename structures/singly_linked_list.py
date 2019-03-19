class SinglyLinkedList: 

    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, next):
        self.next = next
        return next

    @staticmethod
    def forEach(head, predicate):
        cur = head
        while cur:
            predicate(cur)
            cur = cur.next

head = SinglyLinkedList(1)
head.append(SinglyLinkedList(2)).append(SinglyLinkedList(3))

def multiply(node):
    node.value *= 2

def printNode(node):
    print(node.value)

SinglyLinkedList.forEach(head, multiply)
SinglyLinkedList.forEach(head, printNode)