class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_number = min(nums)
        max_number = max(nums)
        gcf = 0
        for i in range(1, min_number + 1):
            if min_number % i == 0 and max_number % i == 0:
                gcf = i
        return gcf