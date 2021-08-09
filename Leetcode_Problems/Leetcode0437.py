# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.count = 0

        def val_freq(root):
            possible_val_frequency = dict()
            if not root:
                return possible_val_frequency
            else:
                vf1 = val_freq(root.left)
                vf2 = val_freq(root.right)
                
                for k in vf1:
                    if k not in possible_val_frequency:
                        possible_val_frequency[k + root.val] = 0
                    possible_val_frequency[k + root.val] += vf1[k]
                for k in vf2:
                    if k not in possible_val_frequency:
                        possible_val_frequency[k + root.val] = 0
                    possible_val_frequency[k + root.val] += vf2[k] 
                    
                if root.val not in possible_val_frequency:
                    possible_val_frequency[root.val] = 0
                possible_val_frequency[root.val] += 1
                    
            print(possible_val_frequency)

            if targetSum in possible_val_frequency:
                self.count += possible_val_frequency[targetSum]
            return possible_val_frequency
        
        val_freq(root)

        return self.count