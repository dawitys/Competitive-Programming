def big_int_addition(a,b):
    final = ""
    a_str, b_str= str(a), str(b)
 
    if len(a_str) < len(b_str):
        while(len(a_str) < len(b_str)):
            a_str = '0'+ a_str
    elif len(a_str) > len(b_str):
        while(len(a_str) > len(b_str)):
            b_str = '0'+ b_str
    
    carry = 0
    for i in range (len(a_str)-1,-1,-1):    
        temp = int(b_str[i]) + int(a_str[i])
        if carry > 0:
            temp += carry
            carry = 0
        if(temp >=10):
            carry += 1
        final = str(temp % 10) + final

    return int(final)