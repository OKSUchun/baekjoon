# 행렬의 값을 받아주자
row, column = map(int, input().split())
matrix_n = []
for _ in range(row):
    matrix_n.append(list(map(int, input().split())))
print(matrix_n)
matrix_m = []
for _ in range(row):
    matrix_m.append(list(map(int, input().split())))
# matrix_answer = [[0] * column ] * row
matrix_answer = [[0] * column for _ in range(row)]
#####
# matrix_answer = [[0] * column] * row
# 1. [[0] * column ] 라는 객체 생성
# 2. [[0] * column] * row 해당 객체를 row 개수 만큼 복사하는 형식으로 생성
# 3. 파이썬의 list 의 shallow copy 생성
# https://wikidocs.net/16038 
# list와 똑같이 b를 a에 할당하면 같은 메모리 주소를 바라보게 됩니다.
# 4. n rows in the matrix 같은 list 를 참조함 
# 5. 원본 리스트의 변경(matrix[0][1]값 변경-> matrix[1][1], matrix[2][1]도 같이 다 바뀜) 모든 복사본에 영향을 미침
# 6. 결론적으로 matrix 을 만들 때, list 의 경우 list * 3 -> shallow copy 
# 새롭게 object 를 생성해야하는것 
# 7. [0]* 3 의 0 은 immutable object 로 a= [0,0,0] a[0] +=1 로 변경한다고 해서 a[1] = 1 로 변경되지 않는다.
# 8. 중요한 것은 matrix 를 initialize 할때, 
matrix_answer = [[0] * column for _ in range(row)] # row 개수 만큼 list 를 새로 생성해줘야함 


#####
for i in range(row):
    for j in range(column):
        matrix_answer[i][j] = matrix_m[i][j] + matrix_n[i][j]
for row_answer in matrix_answer:
    print(*row_answer, end=" ")
    # list 의 원소들을 각각 빼내서 print 하는 방법
