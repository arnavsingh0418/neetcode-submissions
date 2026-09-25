class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while (numbers[right]+numbers[left] != target):
            diff = target - numbers[left] 
            if(diff < numbers[right]):
                right -= 1
            else:
                left += 1
        return [left+1,right+1]