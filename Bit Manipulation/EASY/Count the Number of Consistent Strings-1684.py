class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        reference = [0]*26
        count = 0
        for ch in allowed:
            reference[ord(ch)-97] = 1
            
        for word in words:
            found = True
            for ch in word:
                if not reference[ord(ch)-97]:
                    found = False
                    break
            if found:
                count+=1
        return count