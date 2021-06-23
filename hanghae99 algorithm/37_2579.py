#규칙 
# 1. 계단은 한번에 한계단 또는 두계단씩 오를 수 있다.
# 2. 한계단을 밟으면서 다음계단 또는 2계단으로 오를 수 있다.
# 3. 연속된 세계의 계단을 밟을 수 없다(시작점 제외)
# 4. 첫째, 마지막 계단은 반드시 밟아야 한다.

# 규칙 풀이
# 1번째 계단은 무조건 올라가므로 1번째 계단의 합을 구한다.
# 문제의 조건에서 3칸을 연속해서 올라갈 수 없으므로,
# 자신의 위치(계단) 점수 + 1칸 밑의 점수 + 3칸 밑의 점수의 합과, 
# 자신의 위치 점수 + 2칸 밑의 점수 중 높은 것을 택하여 리스트에 저장한다
# 1번째 계단, 2번째 계단, 3번째 계단을 미리 구한 후, for문을 통해 마지막계단까지 구한다.


N = int(input())
dp = [0 for _ in range(N+3)]   #다이나믹 프로그래밍 약자로 dp 사용
arr = [0 for _ in range(N+3)]  # N + 3은 최대 3칸 이동을 하므로 +3으로 배열구성

for k in range(1,N+1):
  arr[k] = int(input())

  dp [1] = arr[1]
  dp [2] = arr[1] + arr[2]
  dp [3] = max(arr[1] + arr[3] ,arr[2] + arr[3])


  for i in range(4, N+1):
      dp[i] = max( dp[i-3] + arr[i-1] + arr[i] ,  dp[i-2] + arr[i] ) 

print(dp[N]) 