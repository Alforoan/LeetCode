class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = 0
        decreasing = 0
        for i in range(len(nums)):
            if i != len(nums)-1:
                cur = nums[i]
                next = nums[i+1]
                if(next > cur):
                    increasing += 1
                if(next < cur):
                    decreasing += 1
        if increasing > 0 and decreasing > 0:
            return False
        else:
            return True