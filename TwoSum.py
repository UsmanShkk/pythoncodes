class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for u in range(len(nums)):
            if (target-nums[u]) in m:
                return(m[target-nums[u]],u)
            else:
                m[nums[u]]=u
