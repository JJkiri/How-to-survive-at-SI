#문제:N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

#첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
#이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

#첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

import sys

n, m = map(int,sys.stdin.readline().split())

a = []
b = []
c = []

for i in range(n): #n번 입력 받음, 원소의 갯수 m 개
    x = list(map(int,sys.stdin.readline().split()))
    a.append(x)

    #extend는 리스트를 풀어서 원소를 하나 씩 넣는다

# a = [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]]

for i in range(n): #n번 입력 받음 (b)
    y = list(map(int,sys.stdin.readline().split()))
    b.append(y)

# b = [y1~y9]
for i in range(n): #n번 입력 받음, 원소의 갯수 m 개
    z = []
    for j in range(m): #0이 m개인 리스트(z)를 만들고
        z.append(0)
    c.append(z)


#행렬의 덧셈
for i in range(n): #행 n,i
    for j in range(m): #렬 m,j
       c[i][j] = a[i][j] + b[i][j] #같은 행렬끼리 더하기
    print(*c[i])
 #여기까지 리스트로 출력, 공백 구분을 원할시 *a[i]




