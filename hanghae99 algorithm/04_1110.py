input_num = int(input())
N = input_num
cnt = 0
num = N

while True:
  num_1 = num // 10
  num_2 = num % 10
  num_3 = (num_1 + num_2)%10
  num = (num_2*10) + num_3
  cnt += 1
  
  if num == N:
    print(cnt)
    break
