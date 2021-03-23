from heapq import heappush as push
from heapq import heappop as pop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            push(heap, -stone)
        while len(heap) > 0:
            one = -pop(heap)
            if len(heap) > 0:
                two = -pop(heap)
            else:
                return one
            if one != two:
                if one > two:
                    one -= two
                    push(heap, -one)
                else:
                    two -= one
                    push(heap, -two)
        return 0
