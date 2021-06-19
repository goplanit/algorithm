# H = 층
# W = 방갯수
# N = 몇번째 손님
# 총 방갯수 = W * H
# YXX = 방번호

#입력값 : T = 테스트 데이터 / 첫째줄 / H, W, N의 데이터 입력됨


T = int(input())

for i in range(T):
    h, w, n = map(int, input().split( ))

    floor = n % h
    room_line = (n // h) + 1
    if floor == 0:
        floor = h
        room_line -= 1
    
    print(floor * 100 + room_line)
