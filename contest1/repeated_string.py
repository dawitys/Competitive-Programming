def repeatedString(s, n):
    count = 0
    length = len(s)
    while(len(s) < n):
        val = length
        if n % len(s) != 0:
            val = n % length
        s += s[:val]
        print(s)
    for i in s:
        if i == 'a':
            count += 1   
    return count
