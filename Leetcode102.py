class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # level, res = [root] if root else [], []
        # while level:
        #     res += [map(lambda node: node.val, level)]
        #     for node in level:
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #     level = next_level
        # return res

        level, res = [root] if root else [], []
        while level:
            res += [map(lambda node: node.val, level)]
            level = filter(lambda node: node, [i for node in level if node for i in [node.left, node.right]])
        return res
