#문제<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
#예를 들어, 다음과 같이 81개의 수가 주어지면

#이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다. #r 과 c를 출력할것

#첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.

#첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
# 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

board = []
import sys
for i in range(9):
    r = list(map(int,sys.stdin.readline().split())) #한줄을 받아옴, 9번 받아야함
    board.append(r)
    # row를 9번 반복해서 추가했다.
    # 최대값 r 검사해서 r에 추가하자

maxv = 0
r = 0
c = 0
for i in range(9):
    for j in range(9):
        if maxv <= board[i][j]: #r이 i번째행렬의 최대값보다 작은경우
            maxv = board[i][j]#r을 i번째 max value로 교체함
            r = i+1 #교체할때 row값 교체
            c = j+1 #column 값 교체
print(maxv)
print(r,c)

