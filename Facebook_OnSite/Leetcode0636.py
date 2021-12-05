class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
        current_time = 0
        current_id = 0
        call_stack = []
        id_time = {i:0 for i in range(n)}

        for l in logs:
             
            l = l.split(":")
            if l[1] == "start":
                if call_stack:
                    id_time[call_stack[-1]] += int(l[2]) - current_time
                if int(l[0]) not in call_stack:
                    call_stack.append(int(l[0]))
                current_time = int(l[2])
            else:
                id = call_stack.pop()
                id_time[id] += int(l[2]) + 1 - current_time
                current_time = int(l[2]) + 1

        return [id_time[i] for i in range(n)]
                
