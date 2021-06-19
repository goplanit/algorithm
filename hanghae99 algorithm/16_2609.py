#최대공약수와 최소공배수
#첫째줄에는 두개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며, 사이에 한칸의 공백이 주어진다
#첫째줄에는 두 수의 최대공약수를, 둘째줄에는 두 수의 최소 공배수를 출력

#최대공약수란? 동시에 그들 모두의 약수인 정수로 약수 중에 제일 큰 수를 말한다.
#최소공배수란? 최소공배수는 양의 공배수 가운데 가장 작은 하나

#유클리드 호제법:
#유클리드 호제법은 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘의 하나이다.
#호제법이란 말은 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
#2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), 
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
# 이 성질에 따라, b를 r로 나눈 나머지 r’를 구하고, 
# 다시 r을 r’로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 
# 나누는 수가 a와 b의 최대공약수이다. 

#a, b, r / a>b
#입력값 : 24 18

num = map(int, input().split(" "))

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    result = (x, y) // gcd(x, y)
    return result

print(gcd(num))
print(lcm(num))


a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
        
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))

    # 최대공약수 GCD(Greatest Common Divisor)
    # 최소공배수 LCM(Least Common Multiple)
