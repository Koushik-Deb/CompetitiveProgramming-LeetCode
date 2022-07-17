# class Solution:
#     def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
#         gc = reduce(gcd, numsDivide)
#         nums.sort()
#         for ind,val in enumerate(nums):
#             if gc % val == 0:
#                 return ind
#             if val > gc:
#                 break
#         return -1
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        
        gc = numsDivide[0]
        for num in numsDivide:
            gc = gcd(gc,num)

        nums.sort()
        for ind,val in enumerate(nums):
            if gc % val == 0:
                return ind
            if val > gc:
                break
        return -1
