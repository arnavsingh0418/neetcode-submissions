class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        post = [1] * n

        # 1. Prefix: elements to the left
        for r in range(1, n):
            pref[r] = pref[r - 1] * nums[r - 1]

        # 2. Suffix: elements to the right (loop backwards)
        for l in range(n - 2, -1, -1):
            post[l] = post[l + 1] * nums[l + 1]

        # 3. Combine both
        ans = [1] * n
        for i in range(n):
            ans[i] = pref[i] * post[i]

        return ans