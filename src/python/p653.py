#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by fhqplzj on 2017/10/27 下午9:12
class Solution(object):
    def findTarget1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def dfs(node, nums):
            if node is None:
                return False
            if k - node.val in nums:
                return True
            nums.add(node.val)
            return dfs(node.left, nums) or dfs(node.right, nums)

        return dfs(root, set())

    def findTarget2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        nums = []

        def inorder(node):
            if node is not None:
                inorder(node.left)
                nums.append(node.val)
                inorder(node.right)

        inorder(root)
        i, j = 0, len(nums) - 1
        while i < j:
            cur_sum = nums[i] + nums[j]
            if cur_sum == k:
                return True
            elif cur_sum < k:
                i += 1
            else:
                j -= 1
        return False
