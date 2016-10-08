# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # # depth = math.log(len(nums),2)
        # if not nums:
        #     return
        #
        # mid = len(nums) / 2
        # root = TreeNode(nums[mid])
        #
        # level = [nums[:mid], nums[mid+1:]]
        # nodes = [root, root]
        #
        # while level:
        #     uppernode = nodes.pop()
        #     lv = level.pop()
        #     if lv:
        #         mid = len(lv)/2
        #         midNode = TreeNode(lv[mid])
        #         if uppernode.val > lv[mid]:
        #             uppernode.left = midNode
        #         else:
        #             uppernode.right = midNode
        #
        #         if lv[:mid]:
        #             level.append(lv[:mid])
        #             nodes.append(mid)
        #         if lv[mid+1:]:
        #             level.append(lv[mid+1:])
        #             nodes.append(mid)
        #
        # return root

        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
