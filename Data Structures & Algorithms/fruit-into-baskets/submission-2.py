class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        res = 0
        tail = 0
        
        for i in range(len(fruits)):
            basket[fruits[i]] = 1 + basket.get(fruits[i], 0)
            while(len(basket) > 2):
                basket[fruits[tail]] -= 1
                if basket[fruits[tail]] == 0:
                    del basket[fruits[tail]]
                tail += 1
            res = max(res,i-tail+1)
        return res
                
            

            