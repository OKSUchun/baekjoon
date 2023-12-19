n = int(input())  # 들어오는 단어의 갯수
count = 0
word_list = []
for _ in range(n):
    word_list.append(input())

# 이미 등장한 alphabet을 모아놓는 list
for word in word_list:
    factor = list(word)
    already = []
    continuous_yn = n
    for i, _ in enumerate(factor):

        if i == 0:
            already.append(factor[i])
        else:
            if factor[i - 1] == factor[i]:
                pass
            else:
                if factor[i] not in already:
                    already.append(factor[i])
                else:
                    continuous_yn = 'n'
                    break
    if continuous_yn == 'n':
        pass
    else:
        count += 1

print(count)
    # 연속이다. 앞의 알파벳과 동일하다. ok
    # 새로운 알파벳이면서 연속이 아니다.ok
    # 앞의 알파벳과 다르면서, 새로운 알파벳이 아니다. x
