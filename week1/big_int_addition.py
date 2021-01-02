def big_int_addition(a,b):
    negative_num = 0
    final = ""

    if a<0 and b>=0:
        negative_num = 1
    elif b<=0 and a>0:
        negative_num = 2
    elif b<0 and a<0:
        negative_num = -1

    a, b = abs(a), abs(b)
    a_str, b_str= str(a), str(b)
 
    if len(a_str) < len(b_str):
        while(len(a_str) < len(b_str)):
            a_str = '0'+ a_str
    elif len(a_str) > len(b_str):
        while(len(a_str) > len(b_str)):
            b_str = '0'+ b_str
    
    carry = 0
    for i in range (len(a_str)-1,-1,-1):
        if(negative_num == 1):
            digit1 = int(b_str[i])
            if carry == -1:
                digit1 -= 1
                carry = 0
            if digit1 < int(a_str[i]):
                carry = -1
                digit1 = (10 + digit1)
            temp = digit1 - int(a_str[i])
            final = str(temp) + final
        elif(negative_num == 2):
            digit1 = int(a_str[i])
            if carry == -1:
                digit1 -= 1
                carry = 0
            if digit1 < int(b_str[i]):
                carry = -1
                digit1 = (10 + digit1)
            temp = digit1 - int(b_str[i])
            final = str(temp) + final
        else:
            temp = int(b_str[i]) + int(a_str[i])
            if carry > 0:
                temp += carry
                carry = 0
            if(temp >=10):
                carry += 1
            final = str(temp % 10) + final
    print(carry)

    if negative_num == -1:
        return 0-int(final)

    return int(final)

print(big_int_addition(19, -82))