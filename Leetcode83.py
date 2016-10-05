class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head
        :rtype: ListNode
        """
        if not head:
            return head

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
                curr = curr
            else:
                curr = curr.next

            if not curr:
                break

        return head
