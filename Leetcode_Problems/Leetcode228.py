def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    head = None
    curr = None
    output = []

    for i in nums:
        if head is None:
            head = i
            curr = i
        else:
            if i == curr + 1:
                curr += 1
            else:
                if head != curr:
                    output.append(str(head)+ "->"+ str(curr))
                else:
                    output.append(str(head))

                head = curr = i

    if head != curr:
        output.append(str(head) + "->" + str(curr))
    else:
        output.append(str(head))
        
    return output

print(summaryRanges([0,1,2,4,5,7]))