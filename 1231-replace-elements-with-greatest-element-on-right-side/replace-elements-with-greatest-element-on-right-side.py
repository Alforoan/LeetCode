class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        resultList = []
        maxValue = max(arr)
        for i in range(len(arr)):
            if i == len(arr) - 1:
                resultList.append(-1)
            elif arr[i] == maxValue:
                maxValue = max(arr[i + 1:], default=-1)
                resultList.append(maxValue)
            else:
                resultList.append(maxValue)
        return resultList