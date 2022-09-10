class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        count = 0
        output = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j :
                    count+=1
            output.append(count)
        
        return output
        