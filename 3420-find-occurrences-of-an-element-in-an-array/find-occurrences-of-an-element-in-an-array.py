class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        #for each number in queries, figure out the index of the quries[i]th occurrence
        #of x is at
        #if there is no such occurrence, return -1

        #for each quries elements, iterate through nums and
        #keep a counter for x in nums
        #increase the counter until the queries[i] is equal to the counter
        #append the index number into the list that i should create

        x_indices = [i for i, num in enumerate(nums) if num == x]
        
        result = []
        
        for query_num in queries:
            if query_num <= len(x_indices):
                result.append(x_indices[query_num - 1])
            else:
                result.append(-1)
        
        return result