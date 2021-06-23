#문제
# 1. 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 2. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 3. 고른 수열은 오름차순이어야 한다.

# 입력값
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력값
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다. ==> combination 외장함수와 동일한 방식이다.
 

#풀이방법 1
# itertools 모듈을 Import하여 모듈내에 있는 외장함수 combinations를 적용한다.
# combinations는 배열에 있는 n개의 원소를 사용해서 순서의 관계없이 r개의 배열로 나타낼 수 있다.
# 조합 공식 : nCr = nPr/r!   // 순열공식 : npr = n!/(n-r)! - 순열공식은 순서를 정하여 r개의 배열로 나타내는 것
# 예) [1,2,3] 배열을 2개의 배열로 나타내면, [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)] 으로 총 6가지가 되는 것

from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

answer = list(combinations(arr, M))

for element in answer:
    for element2 in element:
        print(element2, end = " ")
    print()
    

# --------------------------
# 문제풀이 2
# 문제의도가 DFS 방식으로 백트래킹 기법을 이용하여 문제를 풀도록 하였다.
# DFS는 깊이 우선 탐색으로 한지점에서 간선을 타고 도착지점까지 계속 탐색한 후 다시 돌아와 다른지점에서 탐색하는 방식
# 백트래킹 기법은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기하고, 다시 왔던 길로 되돌아와 다른 선택지로 다시 탐색하는 것
# 백트래킹은 재귀로 보통 구현하며, 안되는 조건을 없애면서 탐색하기에 시간복잡도를 줄일 수 있다.

# 백트래킹을 위해 우선 가능성이 판단되는 유무를 확인하기 위해 True, False 값을 담아놓을 수 있는 배열을 만든다.
# 값의 비교를 통해 가능성 판단을 결정해야하므로 값을 저장해놓을 수 있는 배열을 만든다.
# 재귀함수를 통해 숫자를 +1씩 증가시키면서 Print 문의 조건을 충족시켜 출력되게 한다.
# for 문을 통해 반복하고, True, False값이 변경되었다면, 다시 변경된 부분을 초기화시켜야 한다.


N, M = map(int, input().split(" "))
lst = [i for i in range(1, N+1)]
check_list = [False]*N

arr = []
def dfs(cnt):
    if cnt == M:
        print(*arr)
        return
    
    for i in range(N):
        if check_list[i]:
            continue
        check_list[i] = True
        arr.append(lst[i])
        dfs(cnt+1)
        arr.pop()
        
        for j in range(i+1, N):
            check_list[j] = False

dfs(0)
