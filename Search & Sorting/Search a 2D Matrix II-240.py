class Solution:
    def searchMatrix(self,matrix,target):
                
        if not len(matrix) or not len(matrix[0]):
			# Quick response for empty matrix
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        # Start adaptive search from bottom left corner
        y, x = h-1, 0
        
        while True:
            
            if y < 0 or x >= w:
                break
            
            current = matrix[y][x]
            
            if target < current:
                # target is smaller, then go up
                y -= 1
            
            elif target > current:
                # target is larger, then go right
                x += 1
            
            else:
                # hit target
                return True
            
        return False
            
#         if len(arr)==0:
#             return False
#         mid = len(arr)//2
#         if arr[mid]==target:
#             return True
#         elif arr[mid]>target:
#             return self.binarySearch(arr[:mid],target)
#         else:
#             return self.binarySearch(arr[mid+1:],target)
    
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for arr in matrix:
#             value = self.binarySearch(arr,target)
#             if value:
#                 return True
#         return False