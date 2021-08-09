# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.n = 0
        def backtrack(root, temp):
            if not root.left and not root.right:
                #print(self.pathToInt(temp + [root.val]))
                self.n += self.pathToInt(temp + [root.val])
            else:
                temp += [root.val]
                if root.left:
                    backtrack(root.left, temp)
                if root.right:
                    backtrack(root.right, temp)
                temp.pop()
        
        backtrack(root, [])
        return self.n


    def pathToInt(self, l):
        v = 0
        for i in l:
            v *= 10
            v += i
        return v