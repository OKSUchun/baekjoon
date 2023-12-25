matrix = []
max_num = max_row = max_col = 0
with open("input.txt", "r", encoding="utf-8") as file:
    # Iterate through each line in the file
    for line in file:
        row = [int(value) for value in line.strip().split()]
        matrix.append(row)
print(max_num, max_row, max_col)

# 예제를 terminal 에 입력하는 대신 input.txt 라는 파일에 저장 후 read 하는 방식으로 변경
