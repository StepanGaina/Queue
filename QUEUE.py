class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.first = self.last = None
        self.queuesize = 0

    def front(self):
        if self.queuesize == 0:
            return None
        else:
            return self.first.value

    def back(self):
        if self.queuesize == 0:
            return None
        else:
            return self.last.value

    def enqueue(self, value):
        newnode = Node(value)

        if self.queuesize == 0:
            self.first = self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
        self.queuesize = self.queuesize + 1

    def dequeue(self):

        if self.first is None:
            return None
        else:
            self.queuesize = self.queuesize - 1
            remnode = self.first
            self.first = self.first.next
            return remnode.value

    def size(self):
        return self.queuesize

    def clear(self):
        self.first = self.last = None
        self.queuesize = 0

