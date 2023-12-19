alphabet_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
# 계속 검색하는게 아니라, replace 를 사용해서 같은 문자가 2번 이상 나오더라도 확인할 수 있음
# alphabet 이 등장할때마다 count +=1 이 아님
# replace "0" 하나짜리 알파벳으로 변경 후 변환된 word 길이를 카운트함
# e.g. alphabet = "c="
# a = "c=c="
# a.replace(alphabet, "0")
# 그럼 같은 alphabet 이 2번 등장하더라도 replace 구문이 전수 대체할 수 있음
for alphabet in alphabet_list:
    if alphabet in word:
        word = word.replace(alphabet, "0")
print(len(word))