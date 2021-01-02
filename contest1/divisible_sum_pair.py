def divisibleSumPairs(n, k, ar):
    res = 0
    for j in range(len(ar)):
        for i in range(0,j):
            if (ar[i]+ar[j]) % k == 0:
                res +=1
    return res