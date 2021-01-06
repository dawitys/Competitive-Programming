def repeatedString(s, n):
    count = 0
    additional = 0
    iter = 0
    for i in s:
        if i == 'a':
            count += 1

    while(count*len(s) < n):
        iter += 1
        val = len(s)
        if(n- len(s) < len(s)):
            val = n % len(s)
            for i in s[0:val]:
                if i == 'a':
                    count += 1
                    break
    return count * iter + additional

print(repeatedString("a",736778906400))