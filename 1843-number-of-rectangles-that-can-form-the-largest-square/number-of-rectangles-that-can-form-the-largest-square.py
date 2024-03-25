class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        #as you iterate through the array, find a lower value
        #append that lower value to the list
        #find the maximum value from the list
        #iterate through the list that contains the lower values and increase the counter
        #every time the element is equal to the maximum value
        lower_values = []
        max_value_counter = 0
        for rectangle in rectangles:
            length = rectangle[0]
            width = rectangle[1]
            min_value = min(length, width)
            lower_values.append(min_value)
        max_value = max(lower_values)
        for value in lower_values:
            if value == max_value:
                max_value_counter += 1
        return max_value_counter
