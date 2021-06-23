# 최소공배수 구하기  /  런타임 에러 났음

num = int(input())

for i in range(num):
  x, y = map(int, input().split(" "))

  for j in range(y, (x*y)+1):   # 최소공배수 for문으로 구하기
    if j%x == 0 and j%y == 0:
      print(j)
      break
    
# 유클리드 호제법으로 구하기

def gcd(x, y):  #최대공약수 구하기
  if y == 0:
    return x
  else:
    return gcd(y, x%y)
  
def lcm(x, y):  ## 최대공약수 구하기
  result = (x*y) // gcd(x,y)
  return result

num = int(input())

for i in range(num):
  x, y = map(int, input().split(" "))
  print(lcm(x, y))

