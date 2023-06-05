class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        str_set = dict()
        key = 0
        rst = []

        for s in str:
            if sorted(s) in str_set:
                index = str_set[sorted[s]]
                rst[index].append(s)

            else:
                str_set[sorted(s)] = key
                key += 1
                rst.append([s])

        return rst