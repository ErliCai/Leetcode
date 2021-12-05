# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.result = None
        self.helper(root, p, q)
        
        return self.result

    def helper(self, root, p, q):
        print(root.val)
        if self.result is not None:
            pass
        else:
            left_p = left_q = right_p = right_q = False
            if root.left:
                left_p, left_q = self.helper(root.left, p, q)
            if root.right:
                right_p, right_q = self.helper(root.right, p, q)

            this_p = this_q = False
            if root.val == p:
                this_p = True
            elif root.val == q:
                this_q = True

            p_found = (this_p or left_p or right_p)
            q_found = (this_q and left_q and right_q)

            print(root.val, p_found, q_found)
            if p_found and q_found:
                self.result = root
            else:
                return p_found, q_found


