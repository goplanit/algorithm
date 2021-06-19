# 배열 리스트에 일치하는 조건이 있으면 먼저 삽입 후, pop을 통해 제거
# 배열이 0일 경우 YES, 0이 아닐경우 NO로 출력


while True:
  word = input()
  bracket = []

  if word[0] == ".":  # "."일때 break를 걸어 진행 방지
    break
  
  for i in word:
    if i == "(" or i == "[":   #"(, [" 이 있을 때, 배열에 삽입
      bracket.append(i)
    elif i == ")":
      if len(bracket) != 0 and bracket[-1] == "(":
        bracket.pop()
      else:
        bracket.append(")")
        break
    elif i == "]":
      if len(bracket) != 0 and bracket[-1] == "[":
        bracket.pop()
      else:
        bracket.append("]")
        break

  if len(bracket) == 0:
    print("yes")
  else:
    print("no")

