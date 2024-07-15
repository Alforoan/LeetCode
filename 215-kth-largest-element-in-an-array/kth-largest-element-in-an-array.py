class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_set = (sorted(nums, reverse=True))
        return new_set[k-1]