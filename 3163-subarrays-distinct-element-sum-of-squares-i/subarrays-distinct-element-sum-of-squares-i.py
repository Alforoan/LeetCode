class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j > i:
                    sum += len(set(nums[i:j+1]))** 2
        sum += len(nums)
        return sum