# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        
        def inorder(root):

            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)

        l = inorder(root)
        lval = [i.val for i in l]

        correc_ord = lval.sort()

        wrong_index = []
        for i in range(len(lval)):
            if correc_ord[i] != lval[i]:
                wrong_index.append(i)

        i, j = wrong_index
        l[i].val, l[j].val = l[j].val, l[i].val