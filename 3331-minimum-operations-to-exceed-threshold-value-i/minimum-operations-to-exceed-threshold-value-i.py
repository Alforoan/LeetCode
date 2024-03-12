class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        if min(nums) >= k:
            return 0
        for x in nums:
            if x < k:
                counter += 1
        return counter