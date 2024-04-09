class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds_count = 0
        for num in arr:
            if num % 2 != 0:
                odds_count += 1
                if(odds_count == 3):
                    return True
            else:
                odds_count = 0
        return False