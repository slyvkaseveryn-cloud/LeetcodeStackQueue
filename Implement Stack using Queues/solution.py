class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size

class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)
        for _ in range(len(self.queue) - 1):
            self.queue.push(self.queue.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.is_empty()
