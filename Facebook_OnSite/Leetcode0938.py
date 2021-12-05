class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        self.sum = 0
        self.low = low
        self.high = high

        self.pre_sort(root)
        return self.sum


        
    def pre_sort(self, root):

        if self.low <= root.val < self.high:
            self.sum += root.val
        elif self.low > root.val:
            if root.right:
                self.pre_sort(root.right)
        else:   
            if root.left:
                self.pre_sort(root.left)