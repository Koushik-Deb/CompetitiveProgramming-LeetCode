class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dtS = collections.Counter(s)
        
        for ch in t:
            if ch not in dtS:
                return False
            dtS[ch]-=1
            if dtS[ch]<=0:
                del dtS[ch]
        
        return len(dtS)==0
        