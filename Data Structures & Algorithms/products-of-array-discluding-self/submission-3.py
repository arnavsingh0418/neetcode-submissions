class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1]*len(nums)
        #right to left
        for r in range(len(nums)):
            if(r>0):
                ans[r] = ans[r-1]*nums[r-1]
            

        #left (last) to right
        postfix = 1
        for l in range(len(nums)-1,-1,-1):
            ans[l] *= postfix
            postfix *= nums[l]
            
            
        return ans


