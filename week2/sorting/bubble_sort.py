def bubbleSort(array):
    n = len(arr) 
    for j in range(n-1):
        for i in range(0, n-j-1)):
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    return array