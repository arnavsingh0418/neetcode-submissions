class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n1, n2 = len(s1), len(s2)
        if(n1>n2):
            return False
        s1_count = Counter(s1)
        window = Counter(s2[:n1])
        if(s1_count == window):
                return True

        for i in range(n1,n2):
            window[s2[i]] += 1
            left = s2[i-n1]
            window[left] -= 1
            if(window[left] == 0):
                del window[left]

            if(s1_count == window):
                return True
        return False