# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pre = self.preorderTravesrsal(root)
        freq = {}
        for num in pre:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        for i in range(len(pre)):
            freq[pre[i]] -= 1
            pre[i] = [pre[i], freq[pre[i]]]


        pre_node = self.preorderTravesrsal(root, True)

        for i in range(len(pre_node)):
            pre_node[i].val = pre[i]
            
        #pre = self.preorderTravesrsal(root)
        inorder = self.inorderTraversal(root)
        
        print(pre, inorder)

        pre = [self.toBinaryString(i) for i in pre]
        inorder = [self.toBinaryString(i) for i in inorder]       
        
        #print(pre, inorder)

        return "".join(pre) + "".join(inorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        #print(data)
        n = len(data) // 2
        pre = data[:n]
        str_len = 32

        pre = [self.binaryStringToInt(pre[str_len*i:str_len*(i+1)]) for i in range(int(len(pre)/str_len))]
        inorder = data[n:]
        inorder = [self.binaryStringToInt(inorder[str_len*i:str_len*(i+1)]) for i in range(int(len(inorder)/str_len))]
        
        print(pre, inorder)

        return self.buildTreeFromPreAndInorder(pre, inorder)

    def buildTreeFromPreAndInorder(self, pre, inorder):

        if len(pre) == 1:
            return TreeNode(pre[0][0])
        if len(pre) == 0:
            return None

        i = inorder.index(pre[0])
        
        left_child = self.buildTreeFromPreAndInorder(pre[1:i+1], inorder[:i])
        right_child = self.buildTreeFromPreAndInorder(pre[i+1:], inorder[i+1:])
        root = TreeNode(pre[0][0])
        root.left = left_child
        root.right = right_child
        return root


    def toBinaryString(self, n):
        n, dup = n
        dup = str(bin(dup))[2:]
        prefix_zero = 5 + 16 - len(dup)
        dup = "0" * prefix_zero + dup
        
        if n >= 0:
            n = str(bin(n))[2:]
            prefix_zero = 11 - len(n)
            n = "0" * prefix_zero + n + dup

            return n
        else:
            n = str(bin(n))[3:]
            prefix_zero = 10 - len(n)
            n = "1" + "0" * prefix_zero + n + dup

            return n            
        
    def binaryStringToInt(self, n):
        sign, n, dup = n[0], n[1:11], n[11:] 
        if sign == "1":
            sign = -1
        else:
            sign = 1
        v = 0
        for i in n:
            v *= 2
            if i == "0":
                v += 0
            else:
                v += 1
        d = 0
        for i in dup:
            d *= 2
            if i == "0":
                d += 0
            else:
                d += 1
        return v * sign, d

    def preorderTravesrsal(self, root, getNodes = False):
        if not getNodes:

            if not root:
                return []
            
            l = []
            if root.left:
                l = self.preorderTravesrsal(root.left)

            r = []
            if root.right:
                r = self.preorderTravesrsal(root.right)

            return [root.val] + l + r

        else:
            if not root:
                return []
            
            l = []
            if root.left:
                l = self.preorderTravesrsal(root.left, True)

            r = []
            if root.right:
                r = self.preorderTravesrsal(root.right, True)

            return [root] + l + r           

    def inorderTraversal(self, root):

        if not root:
            return []

        l = []
        if root.left:
            l = self.inorderTraversal(root.left)

        r = []
        if root.right:
            r = self.inorderTraversal(root.right)

        return l + [root.val] + r


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# C = Codec()
# print(C.toBinaryString(2))
# node = TreeNode(2)
# simple_tree = TreeNode(1)
# simple_tree.left = node
# print(C.preorderTravesrsal(simple_tree))
# #print(C.inorderTraval(simple_tree))
# print(C.serialize(simple_tree))
# print(len(C.serialize(simple_tree)))
# print(C.deserialize(C.serialize(simple_tree)))


# print(C.binaryStringToInt("1011"))
# print(C.buildTreeFromPreAndInorder([1,2],[2,1]).val)



print(0.8 % 1 * 10)