# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.inorder(root)
        self.index = 0
    
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)
        self.nodes.append(root)
        if root.right:
            self.inorder(root.right)
        

    def next(self):
        """
        :rtype: int
        """
        i = self.index
        self.index += 1
        return self.nodes[i]

        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index <= len(self.nodes):
            return True
        else:
            return False
        

