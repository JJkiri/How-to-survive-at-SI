#1018, 브루트포스

#문제
#지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 
# M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 
# 나머지는 흰색으로 칠해져 있다. 
# 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

#체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

#보드가 체스판처럼 칠해져 있다는 보장이 없어서, 
# 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 
# 당연히 8*8 크기는 아무데서나 골라도 된다. 
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

#입력
#첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 
# 
# 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다.
#  B는 검은색이며, W는 흰색이다.


#가능한 모든 경우를 나열한다 (for문)
#각 경우에 대해 결과를 계산한다
#최솟값/최댓값을 저장한다

#pseudo code

## 막힌지점
# 1. 보드를 아직 안읽었다. 2차원의 리스트로 입력에서 주어진 보드를 저장한다.
# board = []
# for i in range(n): #row (n)
# board.append(input()) # column(m)
# 이러면 board[0][0]은 W 또는 B가 된다.



# 2. 반복문 구조가 안쪽만 있다. 바깥에서 어디에서 시작할지를 정해야 한다.
# 파이썬은 0-base여서, -8 +1로 생각해야 8칸을 확보할 수 있다. k칸짜리의 윈도우의 시작 range(n-k+1)

n, m = map(int,input().split())
cnt = 0
cnt_min = 64

board = []
for i in range(n):
    board.append(input()) #board에 BW 입력받기

# w start case
for sr in range (n-7): #start row
    for sc in range(m-7): #start column
        #새로운 시작점 point
        cnt_w = 0
        # 8칸 확보가 가능한 횟수만큼 반복을 수행한다.
        for r in range(8): #row
             for c in range(8): #column
                 #board[sr +r] #내가 검사하고자 하는 행! sr에서 r만큼 간다!
                if (r+c) % 2 == 0:
                    expected = 'W'
                else:
                    expected = 'B'
                if board[sr+r][sc+c] != expected:
                    cnt_w += 1 # cnt_b는 따로 계산할 필요가 없는게, 어차피 정답이 정반대라 64-cnt_w와 동일함!
        cnt_b = 64-cnt_w
        if cnt_w < cnt_min:
            cnt_min = cnt_w #최솟값 교체
        if cnt_b < cnt_min:
            cnt_min = cnt_b #최솟값 교체

print(cnt_min)

