//TO-DO
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        prev_max = arr[-1]
        for i in range(len(arr)-1,-1,-1):
            if arr[i] < prev_max:
                arr[: i].reverse()
                flips
            
