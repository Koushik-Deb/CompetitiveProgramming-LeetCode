class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums,target)
        r = bisect.bisect(nums,target)
        return [-1, -1] if l == r else [l, r - 1]
        