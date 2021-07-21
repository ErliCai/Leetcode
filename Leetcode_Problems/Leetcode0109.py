# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        l = []
        while head:
            l.append[head.val]
            head = head.next

        def BST(l):
            n = len(l) // 2
            if len(l) == 1:
                return TreeNode(l[0])
            if len(l) == 0:
                return None

            return TreeNode(l[n], l[:n], l[n+1:])

        return BST(l)