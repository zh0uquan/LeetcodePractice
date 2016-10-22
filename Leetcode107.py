# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # if not root:
        #     return []
        #
        # level, res = [root], []
        # while level:
        #     next_level = []
        #     res = level + res
        #     for node in level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     level = next_level
        # return res

        res, nodes = [], [root] if root else []
        while nodes:
            res.append(list(node.val for node in nodes))
            nodes = [x for node in nodes for x in (node.left, node.right) if x]
        res.reverse()
        return res
