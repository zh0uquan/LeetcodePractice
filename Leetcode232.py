class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.q.pop(0)


    def peek(self):
        """
        :rtype: int
        """
        if self.q:
            return q[0]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.q

q = Queue()
q.push(1)
q.peek()
print q.empty()
