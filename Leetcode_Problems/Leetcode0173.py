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
        self.inorder = self.inorderTraversal(root)
        self.i = 0
        
    def inorderTraversal(self, root):
        
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 

    def next(self):
        """
        :rtype: int
        """
        r = self.inorder[self.i]
        self.i += 1
        return r
        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.inorder)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()