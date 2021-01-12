def findMedian(arr):
    arr.sort()
    mid = len(arr)//2
    return arr[mid]