'''
Descripttion: 完全二叉树的节点个数
version: 1
Author: Jason
Date: 2020-11-24 16:15:05
LastEditors: Jason
LastEditTime: 2020-11-24 16:15:22
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
