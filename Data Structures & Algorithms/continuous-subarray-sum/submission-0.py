class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        summed = 0
        for l in range(len(nums)):
            summed = nums[l]
            for r in range(l+1,len(nums)):
                summed += nums[r]
                if(summed % k == 0):
                    return True
        return False