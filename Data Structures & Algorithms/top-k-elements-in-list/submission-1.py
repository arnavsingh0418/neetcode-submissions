class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nCount = Counter(nums)
        # nSort = 
        nRev = list(reversed(sorted(nCount.keys(),key=nCount.get)))
        output = []
        return nRev[:k]

        