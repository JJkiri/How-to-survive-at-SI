#치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.

#전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
#인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.

# A+	4.5
# A0	4.0
# B+	3.5
# B0	3.0
# C+	2.5
# C0	2.0
# D+	1.5
# D0	1.0
# F	0.0

#P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
#>> P, F인경우 스크리닝 (조건1)

#20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
#>> split()

#치훈이의 전공평점을 출력한다.

import sys
point = 0 #누적 학점
grade = 0 #누적 학점*과목평점


for i in range(20):
    n, p, g = sys.stdin.readline().split() #입력값을 받기 name, point, grade
    p = float(p) # 정수형으로 p (학점)
    if g == 'P': #'PASS'인경우 계산하지 않음
        pass # pass의 경우 아래코드를 계속 실행하므로, else로 감
    #만약 continue 사용시 아래코드를 실행하지 않으므로, elif문으로 전부 수행해도 됨(else - if) 계단구조 없어도 됨!
    else:
        point += p #누적 학점을 point에 적립함.

        #학점과 과목 평점에 곱을 누적 grade에 적립함.
        if g == 'A+':
            grade += 4.5 * p
        if g == 'A0':
            grade += 4.0 * p
        if g == 'B+':
            grade += 3.5 * p
        if g == 'B0':
            grade += 3.0 * p
        if g == 'C+':
            grade += 2.5 * p
        if g == 'C0':
            grade += 2.0 * p
        if g == 'D+':
            grade += 1.5 * p
        if g == 'D0':
            grade += 1.0 * p
        if g == 'F':
            grade += 0.0 * p

avg = grade/point #전공 평점

print(avg)