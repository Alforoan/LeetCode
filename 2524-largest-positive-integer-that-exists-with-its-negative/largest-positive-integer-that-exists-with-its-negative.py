class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if -nums[i] in nums:
                return nums[i]
        return -1