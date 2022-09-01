class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dt = defaultdict(list)
        
        def sumOfDigit(val):
            total = 0
            
            while val:
                total+=val%10
                val = val//10
            return total
            
        for num in nums:
            dt[sumOfDigit(num)].append(num)
            
        maximum = -1
        
        for key in dt:
            dt[key].sort()
            if len(dt[key])>=2:
                maximum = max(maximum,dt[key][-1]+dt[key][-2])
        return maximum
        