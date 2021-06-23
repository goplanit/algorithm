# 문제 해석
# ==(입력값) 첫재줄에 N과 K가 주어진다.
# ==(풀이) 이항계수 (N K)를 구한다. 즉, nCk를 구하면 된다.
# 공식 = n! / k! * (n-k)!


import sys
import math
n,k = map(int, sys.stdin.readline().split())
answer = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(answer)



## 재귀함수를 이용한 문제 풀이 / 런타임에러뜸
# import sys
# def make_fac(num):
#     return num * make_fac(num-1) if num != 1 else 1
# n,k = map(int, sys.stdin.readline().split())
# answer = make_fac(n) // (make_fac(k)*make_fac(n-k))
# print(answer)
