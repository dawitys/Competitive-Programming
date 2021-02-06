def countingSort(arr):
    highest = max(arr) + 1
    counter_arr = [0]*highest
    n = len(arr)
    new_arr = [0]*n
    
    for i in range(len(arr)):
        counter_arr[arr[i]] += 1
    for i in range(1,highest):
        counter_arr[i]+= counter_arr[i-1]
    
    i = n - 1
    while i >= 0:
        new_arr[counter_arr[arr[i]] - 1] = arr[i]
        counter_arr[arr[i]] -= 1
        i -= 1
