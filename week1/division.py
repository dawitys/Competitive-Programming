def division(n, d):

    is_negative = False
    if n < 0 and d < 0:
        n, d = abs(n), abs(d)
    elif n < 0 or d < 0:
        n, d = abs(n), abs(d)
        is_negative = True

    n, d = str(n), str(d)
    result = ""

    
    i = 0
    temp = int(n[i])
    while(temp < int(d)):
        temp = (temp * 10 + int(n[i+1]))
        i += 1
    i += 1

    while((len(n)) > i):
        result += str(int(temp // int(d)))
        temp = ((temp % int(d)) * 10 + int(n[i]))
        i += 1

    result += str(int(temp // int(d)))

    if (len(result) == 0):
        return "0"
    if is_negative:
        return 0 - result
    return result