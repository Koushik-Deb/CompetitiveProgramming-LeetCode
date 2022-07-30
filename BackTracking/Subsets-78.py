class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        def backTrack(index,arr):
            result.append(copy.copy(arr))

            for i in range(index,len(nums)):
                backTrack(i+1,arr+[nums[i]])
            
        
        
        result = []
        backTrack(0,[])
        
        return result