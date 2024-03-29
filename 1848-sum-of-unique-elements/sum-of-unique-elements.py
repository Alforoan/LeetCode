class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and len(nums) != 1:
            return 0
        if len(set(nums)) == len(nums):
            return sum(nums)
        num_sum = 0
        unique_values = {}
        for num in nums:
            if num in unique_values:
                unique_values[num] += 1
            else:
                unique_values[num] = 1
        for (key, value) in unique_values.items():
           
            if value == 1: 
                num_sum += key

        return num_sum