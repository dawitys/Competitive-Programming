class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = {}
        for x in barcodes: freq[x] = 1 + freq.get(x, 0)
            
        ans, i = [None] * len(barcodes), 0
        for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True): 
            for _ in range(v): 
                ans[i] = k 
                i = i+2 if i+2 < len(ans) else 1
        return ans 