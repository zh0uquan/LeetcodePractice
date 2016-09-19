# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # use set to store the ListNode obj
        # buff = set()
        # while head:
        #     if head in buff:
        #         return True
        #     buff.add(head)
        #     head = head.next
        if not head:
            return False

        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
