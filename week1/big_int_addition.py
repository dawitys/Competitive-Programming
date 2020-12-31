def big_int_addition(a,b):
    a_str= str(a)
    b_str= str(b)
    final = ""

    if len(a_str) < len(b_str):
        while(len(a_str) < len(b_str)):
            a_str = '0'+ a_str
    elif len(a_str) > len(b_str):
        while(len(a_str) > len(b_str)):
            b_str = '0'+ b_str
    
    for i in range (len(a_str)):
        result = int(a_str) + int(b_str)
        final += str(result)

    return int(result)

print(big_int_addition(111111111111111111111111111111111111111111111111111111111111111111111111111,111111111111111111111111111111111111111111111111111111111111111111111111111))