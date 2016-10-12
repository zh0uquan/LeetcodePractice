# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # d = collections.defaultdict(list)
        # d[0] = [None]
        # d[1] = [ListNode(1)]

        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        def trees(first, last):
            if first > last:
                return [None]
            res = []
            for n in range(first, last+1):
                for left in trees(first, n-1):
                    for right in trees(n+1, last):
                        res.append(node(n, left, right))
            return res

        return trees(1, n) if n > 0 else []

if __name__ == '__main__':
    pass