# # 파이썬은 collections모듈의 deque(double-ended queue)을 통해 큐 자료구조 구현
# # 큐는 선입선출 방식이지만 덱은 양방향에서 삽입과 삭제 가능
# # 그럼 그냥 리스트를 쓰면 되지?
#   -> 리스트는 배열의 형태이기 때문에 index 의 앞 부분에서 삽입과 삭제가 일어나면
#       삭제된 곳을 채우기 위해 그 뒤 엘리먼트들이 앞으로 모두 움직이면서 시간복잡도가 O(n)
#       시간복잡도 참고  https://wiki.python.org/moin/TimeComplexity
#       Deque 메소드 참고  https://docs.python.org/3/library/collections.html#collections.deque
#   -> 덱은 데이터 추가 삭제 시 O(1)
# # import 해서 사용

 

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # 큐의 크기 n과 뽑아내려고 하는 수의 개수 m을 입력값으로 받기
position = list(map(int, input().split()))  # 뽑아내려는 수의 위치를 입력값으로 받기
dq = deque([i for i in range(1, n+1)])  # deque([1, 2, 3,...,n])
# dq = deque()
# for i in range(1, n+1):
#     dq.append(i)

count = 0   # 2, 3번 수행하면 카운트 올리기
for i in position:  # 뽑아내려는 수의 위치 하나씩 반복문 돌리기
    while True:     # 뽑을 때까지 계속 돌리기
        if dq[0] == i:  # dq의 첫인덱스가 뽑아내려는 수의 위치와 같다면 1번 수행
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:  # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을때는 왼쪽으로 움직여야 최소
                while dq[0] != i:   # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    dq.append(dq.popleft())  # 파이썬 첨부자료 확인
                    count += 1
            else:   # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 클때는 오른쪽으로 움직여야 최소
                while dq[0] != i:
                    dq.appendleft(dq.pop())  # 파이썬 첨부자료 확인
                    count += 1
print(count)