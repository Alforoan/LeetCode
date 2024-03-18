class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        firstIndex = 0
        secondIndex = 0
        for num in nums1:
            if num in nums2:
                firstIndex += 1
        for num in nums2:
            if num in nums1:
                secondIndex += 1
        return [firstIndex, secondIndex]