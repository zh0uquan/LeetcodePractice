# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class BSTIterator(object):
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.tree = self.inorder_tree(root, [])
#         self.it = iter(self.tree)
#         self.next_int = None
#
#     def inorder_tree(self, node, res):
#         if node:
#             self.inorder_tree(node.left, res)
#             res.append(node.val)
#             self.inorder_tree(node.right, res)
#         return res
#
#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         try:
#             self.next_int = next(self.it)
#         except StopIteration:
#             self.next_int= None
#             return False
#         return True
#
#     def next(self):
#         """
#         :rtype: int
#         """
#         if self.next:
#             tmp = self.next_int
#             self.next_int = None
#             return tmp
#         return next(self.it)
#
#
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.visit = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.visit is not None and self.stack != []

    def next(self):
        """
        :rtype: int
        """
        while self.visit:
            self.stack.append(self.visit)
            self.visit = self.visit.left
        else:
            nextNode = self.stack.pop()
            self.visit = nextNode.right
            return nextNode.val
