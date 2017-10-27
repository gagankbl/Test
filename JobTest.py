def solution(A):
    # write your code in Python 2.7
    a = []
    sum1 = 0
    sum2 = 0
    for i in range(len(A)-1):
        print(i)
        for z in range(0,i):
            print("Z",z, A[z])
            sum1 += A[z]
        for x in range(i+1, len(A)):
            print("X", x, A[x])
            sum2 += A[x]
            print("sum2", sum2)
        print("BREAK")
        print("SUM",sum1, sum2)
        if (sum1 == sum2):
            a.append(A[i])
        sum1 = 0
        sum2 = 0
    
    if (len(a) > 0):
        return a[0]
    else:
        return -1

print(solution([-1, 3, -4, 5, 1, -6, 2, 1] ))