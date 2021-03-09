class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        d =  []
        for i in range(len(s)):
            if d and d[-1][0] == s[i]:
                if d[-1][1] == k-1:
                    d.pop()
                else:
                    d[-1][1] += 1
            else:
                d.append([s[i],1])

        return "".join(c * count for c, count in d)