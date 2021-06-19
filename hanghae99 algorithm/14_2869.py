import math

day_move, night_move, tree_height = map(int, input().split(' '))

count = (tree_height - day_move) / (day_move - night_move) + 1

print(math.ceil(count))


# 문제 접근
# 1. 주어지는 값 : A(낮 이동 거리), B(밤 미끄러지는 거리), V(목표 높이)
# 2. 소요일 계산 ... 총 소요일 X = 우리가 찾는 정답
# ==1일 이동 가능한 거리 : 목표 높이에 도달하는 마지막 날을 제외한 (X-1)일 동안에는 (A-B)씩 이동한다. 마지막 날만 A만큼 이동한다.
# ==❗❗❗즉, (X-1)(A-B)+A = V
# ==이를 X에 대해 정리하면, (X-1)(A-B) = V-A 👉 (X-1) = (V-A)/(A-B) 👉 X = (V-A)/(A-B)+1
# ==소요일은 즉 (V-A)/(A-B)+1

# 필요한 함수
# ①map(A함수, B집합)
# ==(개념) 파이썬의 내장함수로서, map 이하의 B집합(리스트, 문자열)에 A함수를 적용하는 것이다. A과 B 둘 다 반드시 채워져야 한다.
# ==(예시) map(int, input()) 👉 콘솔창에 input한 값에 int 함수를 적용한다. input의 경우 기본적으로 str이기 때문에, 수를 입력해서 연산하려면 int를 적용해야 한다.
# ② math
# ==(개념) 파이썬 수학 모듈함수, 반드시 import math를 해야한다. 올림, 루트, 최댓값, 절대값 등 수학 기능에 이용된다.
# ==(문법) math.method(변수) 👉 method에는 ceil, abs, max, min 등이 있다. 기본적으로 연산을 하는 함수이므로 변수는 int 속성이어야 한다.
# ==(예시) math.ceil(3.2) 👉 올림처리를 하므로 4
# ③ sys
# ==(개념) 빠른 입력! input()과 겉보기에 똑같은 역할을 하지만, 시간초과가 나는 경우 빠른입력 사용하면 효율 상승한다. 다만 input()과는 다르게 str문 입력 시 '사용자가 입력한 문자열 + 개행 문자(\n)'가 저장되기 때문에 에서는 sys.stdin.readline.split('\n') 이용하면 좋다.
# ==(문법) import sys, sys.stdin.readline(). math처럼 모듈함수이므로 import를 해야한다.