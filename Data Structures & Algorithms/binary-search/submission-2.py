class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1

        for index, n in enumerate(nums):
            if n == target:
                ans = index
                break
        return ans
