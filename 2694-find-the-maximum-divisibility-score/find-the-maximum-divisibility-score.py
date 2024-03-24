class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        count = []

        for divisor in divisors:
            tempCount = 0
            for num2 in nums:
                if num2 % divisor == 0:
                    tempCount += 1      
            count.append(tempCount)
            print(f"Divisor: {divisor}, Temp Count: {tempCount}")
  
        print(count)
        maxCount = max(count)
        maxDivisors = [divisor for divisor, c in zip(divisors, count) if c == maxCount]

        return min(maxDivisors)