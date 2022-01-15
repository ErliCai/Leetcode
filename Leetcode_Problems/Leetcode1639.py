from collections import defaultdict

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        
        n = len(words[0])
        d = {i:defaultdict(int) for i in range(n)}
        for w in words:
            for i in range(n):
                d[i][w[i]] += 1
                
        
        l = [1] + [0] * len(target)
        
        for i in range(n):
            new_l = l[::]
            
            for j in range(len(target)):
                
                if target[j] in d[i]:

                    new_l[j+1] += l[j] * d[i][target[j]]
            l = new_l
            print(l)

        return l[-1] % (10 **9 + 7)

words = ["acca","bbbb","caca"]
target = "aba"
S = Solution()
print(S.numWays(words, target))