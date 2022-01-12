from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.d.move_to_end(key, False)
            return self.d[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if len(self.d) == self.capacity:
            if key not in self.d:
                self.d.popitem(last=True)
        self.d[key] = value
        self.d.move_to_end(key, last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)