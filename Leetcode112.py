# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # if not root:
        #     return False
        #
        # stack = [root]
        # level = [root.val]
        # tmp = []
        # while stack:
        #     node = stack.pop()
        #     tmp = level.pop()
        #
        #     if node.left is not None:
        #         stack.append(node.left)
        #         level.append(node.left.val+tmp)
        #     if node.right is not None:
        #         stack.append(node.right)
        #         level.append(node.right.val+tmp)
        #
        #     if node.left is None and node.right is None:
        #         if sum == tmp:
        #             return True
        #
        # return False

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
