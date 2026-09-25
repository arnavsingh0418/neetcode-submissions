class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0]=1
        summed = 0
        res = 0

        for n in nums:
            summed += n
            diff = summed - k
            res += count[diff]
            count[summed] += 1 

        return res

        