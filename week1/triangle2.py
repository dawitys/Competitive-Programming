def print_triangle(a):
    n = a//2
    for i in range(a+1):
        if i % 2 == 1:
            print(' '*n , '*'*i)
            n -=1