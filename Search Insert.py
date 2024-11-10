def searchInsert(nums, target) :
    for k in range(len(nums)):
        if nums[k]==target:
            return k
        elif nums[k]< target and k+1<len(nums):
            if nums[k+1]== target:
                return k+1
            elif nums[k+1]> target:
                return k+1
        elif nums[k]< target and k+1==len(nums):
            return k+1
    return 0
