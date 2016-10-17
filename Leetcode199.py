# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iterative
        # if not root:
        #     return []
        # res = []
        # level = [root]
        #
        # while level:
        #     next_level = []
        #     for node in level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     res.append(level[-1].val)
        #     level = next_level
        #
        # return res

        # recursive
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.left, depth+1)
                collect(node.right, depth+1)
        view = []
        collect(root, 0)
        return view

if __name__ == '__main__':
    pass
