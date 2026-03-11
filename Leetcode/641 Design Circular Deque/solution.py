class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.k = k
        self.capacity = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        newnode = Node(value)

        if self.isEmpty():
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

        self.capacity += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        newnode = Node(value)

        if self.isEmpty():
            self.head = self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

        self.capacity += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self.capacity -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self.capacity -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self) -> bool:
        return self.capacity == 0

    def isFull(self) -> bool:
        return self.capacity == self.k