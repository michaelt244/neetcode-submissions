class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []


        for i in range(2):
            for num in nums:
                new_list.append(num)

        return new_list
        