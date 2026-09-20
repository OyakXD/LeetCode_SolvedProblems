# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth_rec(atual):
    if atual == None:
        return 0
    
    altura_esq = maxDepth_rec(atual.left)
    altura_dir = maxDepth_rec(atual.right)

    return max(altura_esq, altura_dir) + 1

class Solution(object):
    def maxDepth(self, root):
        return maxDepth_rec(root)

        