# 문제 해석
# 재원이가 강 서쪽에서 강 동쪽으로 이어지는 다리를 놓으려고 한다.
# ==(조건#1. 서쪽에서 동쪽으로만 잇는다.)
# 다리를 짓기에 적합한 곳을 '사이트'라고 한다.
# 강 서쪽의 사이트는 강 동쪽의 사이트보다 같거나 적다.
# ==(조건#2. N <= M)
# 헌 사이트에는 최대 한 개의 다리만 연결될 수 있다.
# 다리는 겹칠 수 없다.
# 다리의 수는 서쪽의 사이트 개수(N)만큼 짓는다.
# 다리를 지을 수 있는 경우의 수는?


# 문제 접근
# 1. 첫 줄에 테스트 케이스의 개수 T가 주어지고, 둘째 줄부터 T만큼의 테스트 케이스(n, m)를 입력할 수 있다. == 반복문, map함수 활용
# 2. 조합 공식 이용한다. 서쪽 사이트 N개에서 순서에 상관 없이 동쪽 사이트 M에 연결할 수 있는 경우의 수를 구해야 하는데, 다리는 서로 겹칠 수 없다고 했으므로 조합 공식을 이용한다.



import sys
import math
num = int(sys.stdin.readline().rstrip())
for i in range(0,num):
    n, m = map(int, sys.stdin.readline().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(bridge)