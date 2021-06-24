# 백준 2588번 문제

# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.


num1 = int(input())
num2 = int(input())

print(num1 * (num2%10))
print(num1 * ((num2%100)//10))
print(num1 * (num2//100))
print(num1 * num2)

#방법 2

num1 = int(input())
num2 = list(map(int, input()))

result = []

for i in range(len(num2), 0, -1):
  result.append(num1 * num2[i-1])

print(result[0], result[1], result[2], sep='\n')
print(result[0]+(result[1]*10)+result[2]*100)


# 방법 3

num1 = int(input())
num2 = input()

for i in range(len(num2), 0, -1):	# 3부터 1까지 -1씩 값을 바꿔 탐색한다.
    print(num1 * int(num2[i-1]))

print(num*int(num2))