import sys

input = sys.stdin.readline
N=int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

#1 산술 평균 (소수점 첫 번째 자리에서 반올림)
print(round(sum(arr)/N))

#2 중앙값
arr.sort()
print(arr[N//2])

#3 최빈값
from collections import Counter
k=Counter(arr).most_common()


if len(arr) > 1:  #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:
        print(k[1][0]) 
    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
    else:
        print(k[0][0]) 
else:
    print(arr[0]) 

#4 범위
print(arr[-1] -  arr[0])



#  사사오입 방식의 반올림 구현하는 방법


# 파이썬에서 round 함수로 0.5를 반올림할 때, 정수 부분이 짝수면 반내림이 되고, 홀수면 반올림이 된다.
# 그 이유는 파이썬에서 사용하고 있는 round 내장 함수는 round_half_up 방식이 아니라 round_half_even 방식을 채택하고 있기 때문.



#  ex)즉 3.5의 경우에는 반올림이 되서 4가 되고, 4.5의 경우에는 반내림이 되어서 4가 되는 것.

# 이를 해결하기 위해, 반올림 오차가 없는 고정소수점을 사용하려면 decimal 모듈의 Decimal을 사용하면 된다. Decimal은 숫자를 10진수로 처리하여
#  정확한 소수점 자릿수를 표현해준다.




