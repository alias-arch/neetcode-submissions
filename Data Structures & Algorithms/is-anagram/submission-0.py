class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
       
        return ls == lt