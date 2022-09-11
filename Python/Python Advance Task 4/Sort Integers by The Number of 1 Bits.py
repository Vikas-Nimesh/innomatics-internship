class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d=[]
        for i in sorted(arr):
            d.append((i,bin(i).count('1')))
        sd = sorted(d, key=lambda i: i[1])
        ans=[]
        for i in sd:
            ans.append(i[0])
        return ans
        