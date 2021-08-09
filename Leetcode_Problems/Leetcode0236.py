# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def find(root, v, temp):
            
            if root:
                # print(root.val, v.val)

                if root.val == v.val:
                    return temp + [root]
                else:
                    return find(root.left, v, temp + [root]) or find(root.right, v, temp + [root]) 

        l1 = find(root, p, [])
        l2 = find(root, q, [])
        # print(l1)
        # print()
        # print(l2)

        #while l1 and l2 and (l1[0] == l2[0] or l1[0] == p or l1[0] == q or l2[0] == p or l2[0] == q):
        v = None
        while l1 and l2 and l1[0] == l2[0]:
            v = l1.pop(0)
            l2.pop(0)
            
        #print(v)

        return v


class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root or root == p or root == q:
            return root
        l, r = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(r.right, p, q)
        if l and r:
            return root
        else:
            return l or r
        