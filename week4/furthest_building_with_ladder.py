#Link: https://leetcode.com/problems/furthest-building-you-can-reach/submissions/

import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        acc, n = 0, len(heights)
        pq = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                heapq.heappush(pq, -diff)
                acc += diff
                if acc > bricks:
                    if ladders > 0:
                        acc += heapq.heappop(pq)
                        ladders -= 1
                    else:
                        return i - 1
        return n - 1
