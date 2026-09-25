class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        tail = 0
        ds = set()

        for i in range(len(s)):
            while(s[i] in ds):
                ds.remove(s[tail])
                tail += 1
            ds.add(s[i])
            longest = max(longest,i-tail+1)
        return longest