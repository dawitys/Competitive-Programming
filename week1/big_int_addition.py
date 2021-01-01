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
    
    for i in range (len(a_str)):
        if(negative_num == 1):
            final += str(int(b_str) - int(a_str))
        elif(negative_num == 2):
            final += str(int(a_str) - int(b_str))
        else:
            final += str(int(b_str) + int(b_str))

    if negative_num == -1:
        return 0-int(result)

    return int(result)

print(big_int_addition(-365463458400,452486453515113516))