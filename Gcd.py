import random
# -*- coding: UTF-8 -*-

"这是一个生成两个随机数然后再求两者最大公约数的程序，程序返回值是两者的最大公约数"
def gcd(A,B):
    while(A != B):
        if(A > B): A = A - B
        if(B > A): B = B - A
    print("最大公约数是： %d" % A)
    return A

e = random.randint(1,50)
m = random.randint(1,50)
print(e,m)
gcd(e,m)
