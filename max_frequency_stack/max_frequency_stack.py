"""
Maximum frequency stack.
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


class FreqStack(object):
    """
    Class for a special stack-like structure.
    """
    def __init__(self):
        self.dict_freq = {}
        self.dict_vals = {}
        self.freq_max = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.dict_freq:
            self.dict_freq[val] = 0

        self.dict_freq[val] += 1
        current_freq = self.dict_freq[val]

        if current_freq > self.freq_max:
            self.freq_max = current_freq

        if current_freq not in self.dict_vals:
            self.dict_vals[current_freq] = Stack()

        self.dict_vals[current_freq].push(val)

    def pop(self):
        """
        :rtype: int
        """
        r_value = self.dict_vals[self.freq_max].top()
        self.dict_vals[self.freq_max].pop()

        self.dict_freq[r_value] -= 1

        if self.dict_vals[self.freq_max].empty():
            self.freq_max -= 1

        return r_value
