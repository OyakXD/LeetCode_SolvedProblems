# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        resultado = []
        def inorder(no):
            if no:
                inorder(no.left)
                resultado.append(no.val)
                inorder(no.right)
        inorder(root)

        return resultado

        
        