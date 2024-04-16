"""
Stack implemented through queue.
"""

class Node:
    """
    Base class for an instance of node.
    """
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue(object):
    """
    A class for instances of a queue structure.
    """
    def __init__(self):
        self.front = None
        self.back = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        new_node = Node(x)
        if self.empty():
            self.front = new_node
        else:
            self.back.next = new_node

        self.back = new_node

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            raise Exeption("Queue is empty")
        current_front = self.front
        item = current_front.item
        self.front = self.front.next
        del current_front

        if self.front is None:
            self.back = None
        return item

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            raise Exception("Queue is empty")
        return self.front.item

    def empty(self):
        """
        :rtype: bool
        """
        return self.front is None and self.back is None

class MyStack(object):
    """
    A class for stacks with the help of queues.
    """
    def __init__(self):
        self.q = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        q_compl = Queue()
        q_compl.push(x)
        while not self.q.empty():
            q_compl.push(self.q.pop())

        while not q_compl.empty():
            self.q.push(q_compl.pop())

    def pop(self):
        """
        :rtype: int
        """
        if self.empty():
            raise Exception("Stack is empty")

        return self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.empty():
            raise Exception("Stack is empty")
        return self.q.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
