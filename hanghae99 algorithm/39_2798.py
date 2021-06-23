# 문제 접근
# 순서와 상관 없고, 중복 없이 3개의 숫자를 합하여 M보다 작거나 같은 결과를 출력해야 한다.
# 브루트포스 방식으로 한다. (5+6+7), (5+6+8), (5+6+9), (5+7+8), (5+7+9) ...등 모든 경우의 수를 탐색해서 M에 가장 가까운 경우를 출력하면 된다.

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
answer = 0
for i in range(len(numlist)):
    for j in range(i + 1, len(numlist)):
        for k in range(j + 1, len(numlist)):
            sum = numlist[i] + numlist[j] + numlist[k]
            if sum <= m:
                answer = max(answer, sum)
print(answer)