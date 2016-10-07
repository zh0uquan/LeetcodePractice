# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = []
        ans = cnt = 0

        while stack or root:
            if cnt == k:
                break
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                ans = tmpNode.val
                root = tmpNode.right

        return ans
