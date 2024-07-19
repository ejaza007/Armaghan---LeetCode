# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def is_leaf(node):
            return node is not None and node.left is None and node.right is None
        
        sum_left_leaves = 0
        
        if root.left:
            if is_leaf(root.left):
                sum_left_leaves += root.left.val
            else:
                sum_left_leaves += self.sumOfLeftLeaves(root.left)
        
        if root.right:
            sum_left_leaves += self.sumOfLeftLeaves(root.right)
        
        return sum_left_leaves

        