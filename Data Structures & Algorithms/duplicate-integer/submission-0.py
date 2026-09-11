from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # numsCount = Counter(nums)
        # for i in numsCount.values():
        #     if(i>1):
        #         return True
        # return False
        return len(nums) != len(set(nums))