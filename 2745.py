num, base = input().split()
num_list = list(num)
base = int(base)
answer = 0
for i, single in enumerate(num_list[::-1]):
    if single.isalpha():
        answer += (ord(single) - ord("A") + 10) * base ** i
    else:
        answer += int(single) * base ** i
print(answer)