# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # if not root:
        #     return
        #
        # level = [root]
        # while level:
        #     next_level = []
        #     node = level.pop(0)
        #     while node:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #
        #         if not level:
        #             next_node = None
        #         else:
        #             next_node = level.pop(0)
        #
        #         node.next = next_node
        #         node = next_node
        #
        #     level = next_level

        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
