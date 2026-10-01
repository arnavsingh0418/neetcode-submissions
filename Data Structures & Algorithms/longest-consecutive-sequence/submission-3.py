class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        long = 0
        for n in nums:
            streak = 0
            if n-1 not in num_s:
                while n+streak in num_s:
                    streak+=1
            long = max(streak,long)

        return long 