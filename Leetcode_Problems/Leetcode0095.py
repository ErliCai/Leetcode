# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        self.d = {0:[None]}
        for i in range(n):
            self.d[i+1] = self.generateTrees_helper(i, self.d)

        return self.d[n]


    def generateTrees_helper(self, n, prev):
        
        trees = []
        for i in range(1, 2 + n):
            first_part = list(range(1, i))
            second_part = list(range(i+1, n+2))

            for left in prev[len(first_part)]:
                for right in prev[len(second_part)]:

                    left_copy = self.copy_tree(left)
                    right_copy = self.copy_tree(right)
                    self.traversal(left_copy, first_part)
                    self.traversal(right_copy, second_part)
                    trees.append(TreeNode(i, left_copy, right_copy))
        #print(n, trees)

        return trees

    def traversal(self, root, vals):
        if root:
        
            root.val = vals[root.val - 1]
            self.traversal(root.left, vals)
            self.traversal(root.right, vals)

    def copy_tree(self, root):

        if root:
            #print(root)

            new_root = TreeNode(root.val, self.copy_tree(root.left), self.copy_tree(root.right))
            return new_root



class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        return self.treesFromList(range(1,n+1))

    def treesFromList(self, lst):

        if not lst:
            return [[]]
        else:
            ans = []
            for i in range(len(lst)):
                for l in self.treesFromList(lst[:i]):
                    for r in self.treesFromList(lst[i+1:]):
                        ans.append(TreeNode(lst[i], l, r))

        return ans


print(not None)