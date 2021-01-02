def repeatedString(s, n):
    count = 0
    temp = s
    while(len(s) < n):
        val = len(temp)
        if n//len(temp) == 0:
            val = n % len(temp)
        s += s[:val]
        print(s)
    for i in s:
        if i == 'a':
            count += 1   
    return count

print(repeatedString('sbc',10))