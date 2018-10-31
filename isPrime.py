import random
import math
# -*- coding: UTF-8 -*-

def gcd(A,B):
    while(A != B):
        if(A > B): A = A - B
        if(B > A): B = B - A
    return A

"这是一个分辨一个数是否是素数的程序，程序返回值1表示该数是素数，返回0表示不是"
def isPrime(n):
    i = 2
    while(i <= math.sqrt(n)):
        if(gcd(i,n) == 1):i += 1
        if(gcd(i,n) != 1):
            print("%d不是素数"%n)
            return 0
    print("%d是素数" % n)
    return 1



# n = random.randint(1,10000)    # 随机生成1～10000的一个整数
# f = math.sqrt(n)              # f 是sqrt(n)的值
# print(n,f)
print(isPrime(2**16+1))
