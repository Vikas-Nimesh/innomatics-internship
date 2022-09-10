class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            len_str = str(i)
            if (len(len_str) % 2) == 0:
                count+=1
        return count
        