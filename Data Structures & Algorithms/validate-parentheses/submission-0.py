class Solution:
    def isValid(self, s: str) -> bool:
        
        if(len(s) & 1):
            return False
        
        temp = []
        key = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for p in s:
            if p in key:
                if temp and temp[-1] == key[p]:
                    temp.pop()
                else:
                    return False
            else:
                temp.append(p)
        return temp == []