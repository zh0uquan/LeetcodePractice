# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # curr = head
        # even = ListNode(0)
        # evenCurr = even
        #
        # while curr.next and curr.next.next:
        #     tmp = curr.next  # even
        #     curr.next = tmp.next
        #     curr = curr.next
        #
        #     evenCurr.next = tmp
        #     evenCurr = evenCurr.next
        #
        # if curr.next:
        #     evenCurr.next = curr.next
        # else:
        #     evenCurr.next = None
        #
        # curr.next = even.next
        #
        # return head

        # Recommand!!!

        if not head:
            return head

        odd = head
        even = evenHead = odd.next
        while even and even.next:
            odd.next = odd = even.next
            even.next = even = odd.next

        odd.next = evenHead

        return head
