class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0]
        for i in range(1, n+1):
            results.append(results[i & (i-1)] + 1)
        
        return results
        