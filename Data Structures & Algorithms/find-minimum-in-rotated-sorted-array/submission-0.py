class Solution:
    def findMin(self, nums: List[int]) -> int:
        minV = nums[0]
        for n in nums:
            if n < minV:
                minV = min(minV,n)
        return minV