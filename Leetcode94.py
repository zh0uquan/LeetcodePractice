# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # def helper(node, result):
        #     if node:
        #         helper(node.left, result)
        #         result.append(node.val)
        #         helper(node.right, result)
        #
        # res = []
        # helper(root, res)
        #
        # return res

        res = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                res.append(tmpNode.val)
                root = tmpNode.right

        return res
