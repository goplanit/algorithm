# 입력값에 따른 출력값
# 1 2 3 4 + + + +  4까지 쌓임
# 1 2 (3 4) - -    4, 3 순으로 빠진다
# 1 2 5 6 + +      5, 6이 추가됨
# 1 2 5 (6) -      6이 빠짐
# 1 2 5 7 8 + +    7, 8이 추가됨
# 1 2 5 7 (8) -    8이 빠짐
# 1 2 5 (7) -      7이 빠짐
# (1 2 5) - - -    5, 2, 1 순으로 빠짐

# <문제해결>
#스택에 넣었다가 뽑아 늘어 놓는다 == pop으로 뽑아낸 순서가 입력값 순이다.
#push 하는 순서는 오름차순으로 1=>8로 진행된다.
#스택을 이용해 해당 수열을 만들 수 없을 경우 NO를 입력한다.

# 1. 첫번째 입력값을 받아 for 문을 통해 반복할 수 있게 만든다.
# 2. count를 담을 수 있는 변수와 +, - 를 담을 수 있는 빈 배열과 스택의 빈배열과 불린값을 받는 메세지를 만든다.
# 3. for문과 입력값을 받는 변수를 지정한다.

num = int(input())
count = 0
result = []
stack = []
no_message = True

for i in range(num):
  input_data = int(input())
   
  while count < input_data:
    count += 1
    stack.append(count)
    result.append("+")
    
  if stack[-1] == input_data:
    stack.pop()
    result.append("-")
  else:
    no_message = False
    break
  
if no_message == False:
  print("NO")
else:
  print("\n".join(result))
