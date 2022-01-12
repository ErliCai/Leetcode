class FreqStack(object):

    def __init__(self):
        
        self.freq = {}
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        self.stack.append(val)

    def pop(self):
        """
        :rtype: int
        """
        def maxFreq():
            return max([(i,j) for i, j in self.freq.items()], key = lambda x: x[1])
        
        n = 0
        
        max_freq = maxFreq()[1]
        for i in range(len(self.stack)):
            if self.freq[self.stack[-1-i]] == max_freq:
                n = self.stack.pop(-1-i)
                break
                
        self.freq[n] -= 1
        return n
            


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()






class FreqStack(object):

    def __init__(self):
        
        self.freq = {}
        self.stacks = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        if self.freq[val] <= len(self.stacks):
            self.stacks[self.freq[val]].append(val)
        else:
            self.stacks.append([val])


    def pop(self):
        """
        :rtype: int
        """
        n = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        self.freq[n] -= 1

        return n