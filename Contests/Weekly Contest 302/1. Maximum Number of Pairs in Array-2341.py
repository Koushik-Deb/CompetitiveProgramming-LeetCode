class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dt = defaultdict(int)
        count = 0
        for num in nums:
            dt[num]+=1
            if dt[num]%2==0:
                del dt[num]
                count+=1
        
        return [count, len(dt)]