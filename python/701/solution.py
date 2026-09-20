# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def insertIntoBST_rec(atual, valor):
    if valor < atual.val:
        if atual.left == None:
            novo_no = TreeNode(valor, None, None)
            atual.left = novo_no
        else:
            insertIntoBST_rec(atual.left, valor)
    elif valor > atual.val:
        if atual.right == None:
            novo_no = TreeNode(valor, None, None)
            atual.right = novo_no
        else:
            insertIntoBST_rec(atual.right, valor)

class Solution(object):
    def insertIntoBST(self, root, val):
        if root == None:
            return TreeNode(val, None, None)
        insertIntoBST_rec(root, val)
        return root


        
        