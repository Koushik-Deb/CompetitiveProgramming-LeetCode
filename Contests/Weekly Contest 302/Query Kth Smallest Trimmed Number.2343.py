class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        heap = []
        length = len(nums[0])
        result = []
        
        for query in queries:
            
            for ind,num in enumerate(nums):
                heap.append((int(num[length-query[1]:]),ind))
            
            heapq.heapify(heap)
            
            k = query[0]
            while(k):
                pop = heapq.heappop(heap)
                k-=1
            result.append(pop[1])
            heap = []
            
        return result