class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 0
        tempCount = 0
        for i in range(len(nums)):
            prev = nums[i-1]
            cur = nums[i]
            if(i != 0 and cur > prev):
                print('something')
                tempCount += 1
                if(tempCount > count):
                    count = tempCount
            else:
                tempCount = 0
        return count + 1