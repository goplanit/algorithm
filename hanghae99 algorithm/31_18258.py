# 파이썬은 collections모듈의 deque(double-ended queue)을 통해 큐 자료구조 구현
# 보통 큐는 엘리먼트 삽입 · 삭제 방향이 한방향으로 정해져 있지만 덱은 양쪽에서 삽입 · 삭제 가능.
# 양 끝 엘리먼트에 접근하여 삽입 · 삭제할 경우, 일반적인 리스트가 O(n)이 소요되는데 반해, 덱은 O(1) 소요.
# 임포트(import) 해서 사용.

import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()   # 빈 큐 만들기

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        que.append(command[-1])     # print(que) -> deque(['1'])
    elif command[0] == 'pop':   # 큐는 선입선출이므로 popleft() 메소드사용
        if not que:
            print(-1)
        else:
            print(que.popleft())    
    elif command[0] == 'size':
        print(len(que))
    elif command[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':  # 큐의 가장 앞 인덱스는 0
        if not que:
            print(-1)
        else:
            print(que[0])
    elif command[0] == 'back':  # 큐의 가장 마지막 인덱스는 -1
        if not que:
            print(-1)
        else:
            print(que[-1])