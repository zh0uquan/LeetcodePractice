# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # buff = [head.val]
        # nextNode = head.next
        # while nextNode:
        #     buff.append(nextNode.val)
        #     nextNode = nextNode.next
        #
        # return buff[::-1]
        rev = None
        while head:
            head.next, head, rev = rev, head.next, head
        rerurn rev

Solution().reverseList(head)
