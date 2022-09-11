class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            if nums.count(i) == 1 :
                result.append(i)

        return result
        
        