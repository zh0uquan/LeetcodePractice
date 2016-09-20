class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if not p or not q:
        #     return p == q
        # return get_level(p) == get_level(q)
        #
        # def get_level(root):
        #     level = [root]
        #     stack = []
        #     while level:
        #         node = level.pop()
        #         if node.left:
        #             level.append(node.left)
        #         if node.right:
        #             level.append(node.right)
        #         stack += [node.left.val, node.right.val]
        #     return stack

        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        else:
            return self.isSameTree(q.left, p.left) and \
                   self.isSameTree(q.right, p.right)
