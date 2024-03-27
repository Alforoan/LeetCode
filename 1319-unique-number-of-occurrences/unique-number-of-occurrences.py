class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = {}
        my_list = []
        for num in arr:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        for val in my_dict.values():
            my_list.append(val)

        return len(my_list) == len(set(my_list))