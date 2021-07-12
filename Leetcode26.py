def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    i = 0
    while i < len(nums)-1:
        print(len(nums)-1)
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i +=1
    return len(nums) 

nums = [1,1,2]
removeDuplicates(nums)

nums = [1,1,1,2,2,3,3,4,5,5]
removeDuplicates(nums)