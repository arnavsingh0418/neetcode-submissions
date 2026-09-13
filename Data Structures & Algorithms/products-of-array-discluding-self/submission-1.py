class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        # 1. Left to right: ans[r] gets the product of all elements to the left of r
        for r in range(1, len(nums)):
            ans[r] = ans[r - 1] * nums[r - 1]

        # 2. Right to left: multiply into ans[l] the product of all elements to the right
        postfix = 1
        for l in range(len(nums) - 1, -1, -1):
            ans[l] *= postfix
            postfix *= nums[l]

        return ans