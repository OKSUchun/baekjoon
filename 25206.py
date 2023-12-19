score_map = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F" : 0.0,
}
# 평점 = 이수 학점 * 학점 의 합 / 총 이수학점
total_credit = 0
total_score = 0 

# 평점이 P/F 의 경우 , 평점이 P 인 경우에는 제외해야함
# 3.3 점 이상이어야 함
for _ in range(20):
    subject, credit, score_alpha = input().split()
    if score_alpha in score_map: # P 가 아닌 경우
        score_num = score_map[score_alpha]
        credit = float(credit)
        total_score += score_num * credit
        total_credit += credit
    else: # P 인 경우, 그냥 평점에서 빼버려
        pass
print(round(total_score/total_credit,7))

# eval 함수를 배움
# string으로 주어진 python expression/statement 을 파이썬 자체 표현형식으로 인식하고 실행하는 함수
# result = eval("5+3")
# print(result)
# 8
# int, float 대신 사용할 수 있음 
