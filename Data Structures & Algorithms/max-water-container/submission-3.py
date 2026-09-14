class Solution:
    def maxArea(self, h: List[int]) -> int:
        left = 0
        right = len(h)-1
        maxA = 0

        while left<right:
            currA = min(h[left],h[right])*(right-left)
            if(currA > maxA):
                maxA = currA
            if(h[left]>h[right]):
                right -= 1
            else:
                left += 1
            
        return maxA
