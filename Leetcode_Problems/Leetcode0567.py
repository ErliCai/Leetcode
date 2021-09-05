class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = {}
        for c in s2:
            if c not in count:
                count[c] = 0
        for c in s1:
            count[c] += 1

        for i in range(len(s1)):
            count[s2[i]] -= 1
        if max(count.values()) == min(count.values()) == 0:
            return True

        l = len(s1)
        for i in range(len(s2) - len(s1)):
            count[s2[i]] -= 1
            count[s2[i+l]] += 1
        if max(count.values()) == min(count.values()) == 0:
            return True           

        return False

print(ord("a"))
print(ord("A"))