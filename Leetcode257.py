# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        path = []
        if not root:
            return path

        stack = [root]
        level = [[]]

        while stack:
            node = stack.pop()
            tmp = level.pop() + tmp

            if node.left:
                stack.append(node.left)
                level.append(tmp)

            if node.right:
                stack.append(node.right)
                level.append(tmp)

            if not node.left and not node.right:
                path.append('->'.join(str(i) for i in tmp))

        return path
