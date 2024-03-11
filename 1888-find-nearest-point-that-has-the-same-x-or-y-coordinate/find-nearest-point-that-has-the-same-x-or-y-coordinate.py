class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mPoints = 10000
        mPointsIndex = 10000
        for i in range(len(points)):
            if x == points[i][0] or y == points[i][1]:
                tempMPoints = abs(x - points[i][0]) + abs(y - points[i][1])
                tempMPointsIndex = i
                if(tempMPoints < mPoints):
                    mPoints = tempMPoints
                    mPointsIndex = tempMPointsIndex
        if(mPoints == 10000):
            return -1
        else:
            return mPointsIndex