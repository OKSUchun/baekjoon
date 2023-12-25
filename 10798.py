def solution():
        
    max_length = 0
    matrix = []
    answer = ""
    with open("input.txt", "r", encoding="utf-8") as file:
        # Iterate through each line in the file
        for line in file:
            row = list(str(line.strip()))
            max_length = max(len(row), max_length)
            matrix.append(row)
    for _ in range(5):
        row = list(str(input()))
        max_length = max(len(row), max_length)
        matrix.append(row)
    for row_list in matrix:
        if len(row_list) < max_length:
            row_list.extend([""] * (max_length - len(row_list)))
            # [""] * 2
            # "" * 2

    for j in range(max_length):
        for i in range(5):
            answer += matrix[i][j]
    print(answer)

    # 단어의 최대 갯수는 15개
    for a in zip(*[input().ljust(15) for _ in range(5)]):
        for b in a:
            if b != " ":
                print(b, end="")

def bookSolution():
    # 단어의 최대 갯수는 15개 input().ljust(15) 15보다 짧을 경우, 공백으로 채움
    for a in zip(*[input().ljust(15) for _ in range(5)]):
        # zip
        example_list = ["apple", "banana", "cherry", "date", "elderberry"]
        zip(*example_list)
        # zip(*example_list)의 결과
        # [
        #     ("a", "b", "c", "d", "e"), -- example_list[0][0], example_list[1][0]끼리 zip
        #     ("p", "a", "h", "a", "l"), -- example_list[0][1], example_list[1][1]끼리 zip
        #     ("p", "n", "e", "t", "d"), -- example_list[0][2], example_list[1][2]끼리 zip
        #     ("l", "a", "r", "e", "e"),
        #     ("e", "a", "r", " ", "r"),
        #     (" ", " ", "y", " ", "r"),
        #     (" ", " ", " ", " ", "y"),
        #     (" ", " ", " ", " ", "b"),
        #     (" ", " ", " ", " ", "e"),
        #     (" ", " ", " ", " ", "r"),
        #     (" ", " ", " ", " ", "r"),
        #     (" ", " ", " ", " ", "y"),
        # ]

        for b in a:
            if b != " ":
                print(b, end="")
