# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # only one loop with the help of the father
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [root]
        strList = ['']
        res = []
        while stack:
            node = stack.pop()
            string = strList.pop() + str(node.val)
            if not node.left and not node.right:
                res.append(string)
            if node.left:
                strList.append(string)
                stack.append(node.left)
            if node.right:
                strList.append(string)
                stack.append(node.right)

        return sum((int(n) for n in res))

    # two loop with stack, usally with dictionary WRONG!
