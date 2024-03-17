class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = sum(nums)
        total2 = 0
        for num in nums:
            for x in str(num):
                total2 += int(x)
        return abs(total - total2)