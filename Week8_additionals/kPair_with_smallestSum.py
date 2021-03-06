class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if len(nums1) * len(nums2) <= 0:
            return []
        
        import heapq
        ret = []
        queue = [(nums1[0] + nums2[0], (0, 0))]
        visited = {}
        while len(ret) < k and queue:
            _, (i, j) = heapq.heappop(queue)
            ret.append((nums1[i], nums2[j]))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                    heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                    visited[(i, j + 1)] = 1
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                    heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                    visited[(i + 1, j)] = 1
        return ret
