class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        resultList = []
        for i in range(len(nums)):
            if i % 2 != 0:
                continue
            else:
                for x in range(nums[i]):
                    resultList.append(nums[i+1])
        return resultList