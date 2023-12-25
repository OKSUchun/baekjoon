n = int(input())
matrix = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y= map(int, input().split())
    for i in range(10):
        for j in range(10):
            matrix[x+i][y+j] = 1
total = 0
for row in matrix:
    total += sum(row)
    # sum({list 명}) -> List 의 모든 원소를 합계를 구할 수 있음
print(total)