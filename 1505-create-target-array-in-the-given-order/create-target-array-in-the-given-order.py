class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        newList = []
        for i in range(len(nums)):
            newList.insert(index[i], nums[i])
        return newList