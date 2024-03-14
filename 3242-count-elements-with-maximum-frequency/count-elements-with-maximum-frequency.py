class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_frequency = 0
        sum_frequency = 0
        if len(nums) == set(nums):
            return len(nums)
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        for num in frequency_dict.values():
            if num > max_frequency:
                max_frequency = num
        for num in frequency_dict.values():
            if num == max_frequency:
                sum_frequency += max_frequency
        return sum_frequency
     