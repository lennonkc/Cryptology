import random

def gcd(A, B):
    while (A != B):
        if (A > B): A = A - B
        if (B > A): B = B - A
    return A

def ExtGCD(a, b):
    "a*s + b*t = gcd(a,b),扩展欧几里德算法"
    if b == 0:
        return 1, 0, a
    else:
        s, t, q = ExtGCD(b, a % b)  # q = gcd(a, b) = gcd(b, a%b)
        s, t = t, (s - (a // b) * t)
        return s, t, q

def isPrime(n):
    '改良的判断素数方法 费马检测 + 平方根二次检测, 返回False不是素数,返回True是素数'
    if(n <= 2):
        if(n == 2):return True
        else:return False
    if(n %2 == 0):return False
    u = n - 1
    while(u % 2 == 0):
        u = int(u / 2)
    for _ in range(10):
        '检测次数为 10次 ,费马检测出错概率为(1/4^10)'
        a = random.randint(2, n - 1)
        testu = u
        x = ModExp(a,u,n)
        while(testu < n):
            y = ModExp(x,2,n)      # 二次检测原理
            if (y == 1 and x != 1 and x != n - 1):
                return False       # 不满足二次探测
            x = y
            testu = testu * 2
        if ( x != 1):
            return False
    return True

def ModExp(b,n,m):
    '反复平方乘算法 计算b^n(mod m)'
    stringN = bin(n)               # 指数转换为二进制
    stringN = stringN[3:]          # 取第三位之后
    x = b
    for i in stringN:
        if(i == '0'):
            x = x**2
        else:
            x = b*(x**2)
    return x%m

def Phi(n):
    '计算欧拉函数'
    phi = 0
    for i in range(1,n):
        if(gcd(i,n) == 1):phi += 1
    return phi


if __name__ == '__main__':
    # print(ExtGCD(3, 2))
    # print(ModExp(8,5,11))
     print(isPrime(2**16+1))
     print(Phi(5))
