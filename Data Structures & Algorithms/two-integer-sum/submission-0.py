class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, num in enumerate(nums):
            diff = target - num  #the number we need to look for
            if(diff in prev):
                return[prev[diff],i]
            prev[num] = i