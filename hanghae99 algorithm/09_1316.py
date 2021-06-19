N = int(input())

count = N

for i in range(0, N):
  input_data = input()

  for k in range(0, len(input_data)-1):
    if input_data[k] ==  input_data[k+1]:
      pass
    elif input_data[k] in input_data[k+1:]:
      count -= 1
      break
    
print(count)