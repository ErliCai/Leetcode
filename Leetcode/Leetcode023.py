def mergeKLists(self, lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    nums = []
    for l in lists:
        while l:
            nums.append(l.val)
            l = l.next
    print(nums)
    if nums == []:
        return None
    else:
        nums.sort()
        l = ListNode(nums[-1])
        nums.pop()
        while nums:
            l = ListNode(nums[-1], l)
            nums.pop()
        return l