#M이상 N이하의 소수를 모두 출력하는 프로그램 작성

import math

def check(num):
    if num == 1:
        return False

    else:
        for i in range(2, int(math.sqrt(num)+1)):
            if num%i == 0:
              return False       
        
        return True

a, b = map(int, input().split(" "))

for i in range(a, b+1):
    if check(i):
        print(i)

