# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search_rec(atual, alvo):
    if atual == None:
        return None
    if atual.val == alvo:
        return atual
    if alvo < atual.val:
        return search_rec(atual.left, alvo)
    else:
        return search_rec(atual.right, alvo)

class Solution(object):
    def searchBST(self, root, val):
        return search_rec(root, val)
        
        