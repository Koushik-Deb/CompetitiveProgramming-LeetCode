class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        s = set()
        result = []
        
        for word in words:
            dt = {}
            isMatch = True
            for ind,ch in enumerate(word):
                if ch in dt:
                    if dt[ch]!=pattern[ind]:
                        isMatch = False
                        break
                    continue
                elif pattern[ind] in s:
                    isMatch = False
                    break
                else:
                    dt[ch] = pattern[ind]
                    s.add(pattern[ind])
            s.clear()
            if isMatch: result.append(word)
        return result