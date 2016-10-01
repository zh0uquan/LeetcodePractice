# Definition for singly-linked list.
import random

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        https://en.wikipedia.org/wiki/Reservoir_sampling
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        curr = self.head
        j = 1
        selected = curr.val
        while curr:
            r = random.randint(1, j)
            if r == 1:
                selected = curr.val
            curr = curr.next
            j += 1
        return selected


# Your Solution object will be instantiated and called as such:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(8)

d = {}
for i in range(100000):
    obj = Solution(head)
    param_1 = obj.getRandom()
    d[param_1] = d.setdefault(param_1, 0) + 1
print(d)
print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)
