class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        odd = dict()
        even = dict()
        for i in arr:
            
        