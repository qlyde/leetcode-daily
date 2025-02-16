# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive
        # if not root:
        #     return root
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root

        # Iterative DFS (Pre-order)
        if not root:
            return root

        stack = [root]
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return root
