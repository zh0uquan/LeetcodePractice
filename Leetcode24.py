# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next:
        #     return head
        #
        # init = ListNode(0)
        # init.next = head
        # curr = init
        #
        # while curr.next and curr.next.next:
        #     tmp = curr.next.next
        #     curr.next.next = curr.next
        #     curr.next = tmp
        #     curr = tmp.next

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            tmp = curr.next.next
            curr.next.next = tmp.next
            tmp.next = curr.next
            curr.next = tmp
            curr = curr.next.next

        return dummy.next
