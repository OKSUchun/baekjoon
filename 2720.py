coin = [25, 10, 5, 1]
n = int(input())
changes = []
for _ in range(n):
    changes.append(int(input()))

for change in changes:
    for i in coin:
        print(change//i, end= " ")
        change %= i
    print()