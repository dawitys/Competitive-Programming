def big_int_multiplication(a,b):
    a_str = str(a)
    b_str = str(b)

    final_result =0
    pos = 0
    for i in range(len(b_str)-1,-1,-1):
        temp = multiply_by_single_digit(a,int(b_str[i]))
        result = str(temp) + (pos*'0')
        final_result += int(result)
        pos += 1
        print(final_result)
    
    return final_result    

def multiply_by_single_digit(num, c):
    result = 0
    for i in range(c):
        result = big_int_addition(result,num)
    return result

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

big_int_multiplication(123,1001)