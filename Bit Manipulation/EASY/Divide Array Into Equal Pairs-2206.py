class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dt = defaultdict(int)
        
        for num in nums:
            dt[num]+=1
            
        for key in dt:
            if dt[key]%2:
                return False
        return True