from collections import deque
from collections import OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain_capacity = capacity
        self.key_to_freq = {}
        self.freq_to_key = {0:OrderedDict()}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("1", self.freq_to_key, self.key_to_freq)

        if key not in self.key_to_freq:
            return -1
        
        f = self.key_to_freq[key]
        self.key_to_freq[key] += 1
        # print(self.freq_to_key, self.key_to_freq)
        val = self.freq_to_key[f][key]
        del self.freq_to_key[f][key]
        if f + 1 not in self.freq_to_key:
            self.freq_to_key[f+1] = OrderedDict()
        self.freq_to_key[f+1][key] = val
        self.freq_to_key[f+1].move_to_end(key, last = False)
        
        # print("2", self.freq_to_key, self.key_to_freq)

        return val

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print("put")

        if self.remain_capacity > 0:
            if key not in self.key_to_freq:
                self.freq_to_key[0][key] = value
                self.key_to_freq[key] = 0
                self.remain_capacity -= 1
            else:
                f = self.key_to_freq[key]
                self.freq_to_key[f][key] = value                
            self.get(key)
        else:
            if key in self.key_to_freq:
                f = self.key_to_freq[key]
                self.freq_to_key[f][key] = value
                self.get(key)
            else:
                # for f in self.freq_to_key:
                for f in range(len(self.freq_to_key)):
                    # print("f", f)
                    if self.freq_to_key[f]:
                        k, v = self.freq_to_key[f].popitem()
                        del self.key_to_freq[k]
                        self.remain_capacity += 1
                        #print("got here")
                        self.put(key, value)
                        break
        
            
        #print(self.freq_to_key, self.key_to_freq)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)