class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        
        for val in encoded:
            result.append(result[-1]^val)
            
        return result