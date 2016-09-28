# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        tmp = 0
        if root.left:
            if not root.left.left and not root.left.right:
                tmp = root.left.val
        return tmp + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
