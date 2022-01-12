class Node(object):
    def __init__(self, key, val, prev=None, nex=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nex = nex

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.head = self.tail = None
        self.dict = dict()
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """

        if key not in self.dict:
            return -1

        else:
            node = self.dict[key]

            if node.prev is None:
                return node.val
            elif node.nex is None:
                self.tail = node.prev
                self.tail.nex = None
                node.nex, node.prev, self.head.prev, self.head = self.head, None ,node, node
                return node.val
            else:
                node.prev.nex, node.nex.prev = node.nex, node.prev
                node.nex, node.prev, self.head.prev, self.head = self.head, None ,node, node
                return node.val

        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        

        if self.head is None and self.tail is None:
            self.tail = self.head = Node(key, value)
            self.dict[key] = self.head
            self.capacity -= 1
            return
        
        if key in self.dict:
            self.get(key)
            self.head.val = value
        else:
            if self.capacity == 0:

                node = Node(key, value)
                self.dict[key] = node
                self.head.prev, self.head, node.nex = node, node, self.head
                self.tail, tail_val = self.tail.prev, self.tail.key
                del self.dict[tail_val]
                self.tail.nex = None
            else:
                node = Node(key, value)
                self.dict[key] = node
                self.head.prev, self.head, node.nex = node, node, self.head
                self.capacity -= 1


        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)