# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# [1, 2, 3, 4]

head = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)

head.next = h2
h2.next = h3
h3.next = h4

# 0 6 1 5 2 4 3
#
# 0 4 1 3 2
# 0 3 1 2
class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        it = head
        linked_list = [head.val]
        while it.next:
            linked_list.append(it.next.val)
            it = it.next

        middle = len(linked_list) / 2
        left = linked_list[:middle+1]
        right = linked_list[middle+1:][::-1]

        print(left, right)



Solution().reorderList(head)
