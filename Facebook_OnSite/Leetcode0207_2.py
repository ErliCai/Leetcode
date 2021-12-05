class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        n = len(prerequisites)
        pre_nex = dict()
        nex_pre = dict()
        nodes = set()
        for p in prerequisites:
            if p[0] not in pre_nex:
                pre_nex[p[0]] = set()
            if p[1] not in nex_pre:
                nex_pre[p[1]] = set()
            pre_nex[p[0]].add(p[1])
            nex_pre[p[1]].add(p[0])
            nodes.add(p[0])
            nodes.add(p[1])


        nodes_no_pre = nodes - set(nex_pre.keys())

        print(nodes_no_pre, nex_pre)

        while nodes_no_pre:
            node = nodes_no_pre.pop()
            nodes.remove(node)
            if node in pre_nex:
                for node2 in pre_nex[node]:
                    nex_pre[node2].remove(node)
                    if not nex_pre[node2]:
                        nodes_no_pre.add(node2)

        print(nodes)

        return len(nodes) == 0

num = 2
pre = [[1,0], [0,1]]
S = Solution()
print(S.canFinish(num, pre))