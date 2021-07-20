
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        D = {}
        for c in t:
            if c in D:
                D[c] += 1
            else:
                D[c] = 1

        low = high = 0
        s = s + " "
        Dcopy = dict(D)
        rlow = rhigh = None

        while high < len(s) - 1:
            if max(Dcopy.values()) > 0:
                if s[high] in t:
                    Dcopy[s[high]] -= 1
                high += 1
            else:
                if rlow is None or high - low < rhigh - rlow:
                    rlow, rhigh = low, high
                if s[low] in t and Dcopy[s[low]] < D[s[low]]:
                    Dcopy[s[low]] += 1
                low += 1


        tailSolution = False
        while max(Dcopy.values()) <= 0:
            tailSolution = True
            if s[low] in t and Dcopy[s[low]] < D[s[low]]:
                Dcopy[s[low]] += 1
            low += 1

        if tailSolution and (rlow is None or high - low + 1 < rhigh - rlow):
            rlow, rhigh = low - 1, high

        if rlow == None:
            return ""
        else:
            return s[rlow:rhigh]


S = Solution()
s = "a"
t = "aa"
r = S.minWindow(s=s,t=t)
print(r)


# A = {1:2, 3: 4, 6:0}
# print(max(A.values()))



# print(ord("a"))
# print(chr(97))
# print(ord("A"))
# print(chr(65+25))

# print("123" + "4")
# print(ord(" "))