from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        val = self.top.value
        self.top = self.top.next
        self.size -= 1
        return val

    def is_empty(self):
        return self.top is None

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.stacks = defaultdict(Stack)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        self.stacks[f].push(val)

    def pop(self) -> int:
        val = self.stacks[self.max_freq].pop()
        self.freq[val] -= 1
        if self.stacks[self.max_freq].is_empty():
            self.max_freq -= 1
        return val
