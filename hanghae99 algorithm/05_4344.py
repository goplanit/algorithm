n = int(input())

for i in range(n):
  input_score = list(map(int, input().split(' ')))

  avg = sum(input_score[1:])/input_score[0]
  cnt = 0
 
  for score in input_score[1:]:
    if score > avg:
      cnt += 1
  rate = cnt / input_score[0] * 100
  print(f'{rate:.3f}%')

