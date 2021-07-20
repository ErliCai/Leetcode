class Solution(object):

    def toDict(self,str):
        r = [0] * 26
        for c in str:
            r[ord(c)-97] += 1

        return r

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = []
        for str in strs:
            hashmap = self.toDict(str)
            alreadyIn = False
            for r in result:
                if r[0] == hashmap:
                    r.append(str)
                    alreadyIn = True
                    break
            if not alreadyIn:
                result.append([hashmap,str])

        result = [s[1:] for s in result]
        return result


class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_in_ord = ["".join(sorted(str)) for str in strs]
        strs_set = list(set(strs_in_ord))
        result = [[] for i in range(len(strs_set))]
        for i in range(len(strs)):
            result[strs_set.index(strs_in_ord[i])].append(strs[i])

        return result



s = Solution2()
strs = ["eat","tea","tan","ate","nat","bat"]
r = s.groupAnagrams(strs)
print(r)

