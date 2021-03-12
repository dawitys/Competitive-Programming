class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        s = []
        count = 0
        visited = set()
        
        for stone in stones:
            if (stone[0],stone[1]) not in visited:
                s.append((stone[0],stone[1]))
                visited.add((stone[0],stone[1]))
            
                while(s):
                    curr = s.pop()
                    for neighbour_candidate in stones:
                        if ((neighbour_candidate[0],neighbour_candidate[1]) not in visited and (neighbour_candidate[0] == curr[0] or neighbour_candidate[1] == curr[1])):
                            s.append((neighbour_candidate[0],neighbour_candidate[1]))
                            visited.add((neighbour_candidate[0],neighbour_candidate[1]))
                count += 1           
        return len(stones) - count
