from collections import Counter

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = Counter(A)
        visited = []

        increment = 0
        for x in range(100000):
            if count[x] >= 2:
                visited.extend([x] * (count[x] - 1))
            elif visited and count[x] == 0:
                increment += x - visited.pop()
        return increment
