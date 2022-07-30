class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        val = start^goal
        count = 0
        
        while val:
            if val&1: 
                count+=1
            val >>= 1
        return count