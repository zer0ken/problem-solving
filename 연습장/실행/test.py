import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def eea(a, b):
    s1, s2, t1, t2 = 1, 0, 0, 1
    while b > 0:
        q = a // b
        a, b = b, a % b
        s1, s2 = s2, s1 - q*s2
        t1, t2 = t2, t1 - q*t2
    return s1, t1


input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    """ 1. CRT; Chinese Remainder Theorem
    
    다음을 만족하는 k를 구해야 한다.
        k === x (mod M)
        k === y (mod N)

    두 식을 변형하면 각각 다음의 식을 얻는다.
        k = M*k1 + x ... (1)
        k = N*k2 + y ... (2)
    
    즉, 다음과 같다.
        M*k1 - N*k2 = y - x
        
    g = gcd(M, N)이라고 했을 때 다음이 성립한다.
        M*k1 / g - N*k2 / g = (y - x) / g,
        k1 * M/g - k2 * N/g = (y - x)/g
    
    M/g와 N/g는 M, N을 최소공배수로 각각 나눈 것이기 때문에 서로소이다.

    여기서 (y - x)가 g로 나누어 떨어지지 않으면 문제를 풀 수 없다.
    """
    g = gcd(M, N)
    if (y - x) % g:
        sys.stdout.write('-1\n')
        continue
    
    """ 2. EEA; Extended Euclidean Algorithm
    
    주어진 a, b에 대해 a * s + b * t = gcd(a, b)일 때 s와 t의 값을 구할 수 있다.
    
    이전 단계에서 a = M/g, b = N/g이므로 gcd(a, b) = 1이고, 위의 식은 다음과 같이 변형된다.
    
    (M/g * k1 + N/g * k2) / ((y - x)/g) = 1
    """
    
    k1, k2 = eea(M // g, N // g)
    
    left = M//g * k1 + N//g * k2
    print(left, k1, k2)