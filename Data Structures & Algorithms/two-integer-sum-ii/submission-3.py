class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # step = 0
        # choose = numbers[step]

        # for n in numbers:
        #     if(target > choose):
        #         goal = target-choose
        #     else:
        #         step += 1
            
        #     if(n == goal):
        #         return [choose,n]

        right = len(numbers)-1
        left = 0

        while left<right:
            currSum = numbers[left]+numbers[right]
            if(currSum > target):
                right -= 1
            elif(currSum < target):
                left += 1
            else: return [left+1,right+1]
            
        # return []

        
