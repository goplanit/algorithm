total_number = set(range(1, 10001))
target_number = set()

for i in range(1, 10001):
  for j in str(i):
    i += int(j)
  target_number.add(i)

self_number = sorted(total_number - target_number)

for k in self_number:
  print(k)


