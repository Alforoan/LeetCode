class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            result.append(abs(left_sum - right_sum))
        return result       