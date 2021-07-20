def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    numset = set(nums)
    print(numset)
    print(nums)

    return len(nums) != len(numset)

containsDuplicate([1,2,3,1])