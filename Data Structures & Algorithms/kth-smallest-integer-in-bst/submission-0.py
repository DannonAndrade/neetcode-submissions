# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []
        def in_order(node):
            if not node: return 

            in_order(node.left)
            res.append(node)
            in_order(node.right)

        in_order(root)
        node = res[k - 1]
        return node.val

        
        