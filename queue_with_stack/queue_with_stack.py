"""
Queue implementation through stacks.
"""

class Node:
    """
    Base class for an instance of node.
    """
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    """
    A class for instances of a stack structure.
    """
    def __init__(self):
        self.top_node = None

    def empty(self):
        """
        Empty top node declaration.
        """
        return self.top_node is None

    def push(self, item):
        """
        Add an element to the stack.
        """
        new_node = Node(item)
        if not self.empty():
            new_node.next = self.top_node

        self.top_node = new_node

    def pop(self):
        """
        Delete an element out of stack.
        """
        if self.empty():
            raise Exception("Stack is empty")

        current_top = self.top_node
        item = current_top.item
        self.top_node = self.top_node.next
        del current_top
        return item

    def top(self):
        """
        Return the top node.
        """
        if self.empty():
            raise Exception("Stack is empty")
        return self.top_node.item


class MyQueue(object):
    """
    A class for queues with the help of stacks.
    """
    def __init__(self):
        self.s = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        s_compl = Stack()
        while not self.s.empty():
            s_compl.push(self.s.pop())
        s_compl.push(x)
        while not s_compl.empty():
            self.s.push(s_compl.pop())

    def pop(self):
        """
        :rtype: int
        """
        if self.s.empty():
            raise Exeption("Queue is empty")
        return self.s.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.s.empty():
            raise Exception("Queue is empty")
        return self.s.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.s.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
