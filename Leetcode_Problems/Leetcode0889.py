# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        
        i = post.index(pre[1])
        left_child = self.constructFromPrePost(pre[:2+i], post[:i+1])
        right_child = self.constructFromPrePost(pre[2+i], post[i+1:-1])
        return TreeNode(pre[0], left_child, right_child)