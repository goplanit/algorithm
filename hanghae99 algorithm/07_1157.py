word = input().upper()
word_list = list(set(word))

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])


#  -------------------



  words = input().upper()
overlap_words = list(set(words))

cnt_list = []

for i in overlap_words:
  cnt = words.count(i)
  cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
  print("?")
else:
  max_index = cnt_list.index(max(cnt_list))
  print(overlap_words[max_index])
