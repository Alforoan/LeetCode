class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for eachNumber in str(num):
                result.append(int(eachNumber))
        return result