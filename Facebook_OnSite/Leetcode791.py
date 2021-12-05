class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i 


        not_in_order = ""
        order_freq = {o: 0 for o in order}
        for c in s:
            if c in order_dict:
                order_freq[c] += 1
            else:
                not_in_order = not_in_order + c

        # rebuild the string
        in_order = ""
        for o in order:
            in_order += o * order_freq[o]

        return in_order + not_in_order