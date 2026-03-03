#검정색 피스는 모두 있었으나, 흰색 피스는 개수가 올바르지 않았다.
#체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

#첫째 줄에 동혁이가 찾은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어진다. 이 값은 0보다 크거나 같고 10보다 작거나 같은 정수이다.
# 1줄, 공백구분 > readline, 6data

#첫째 줄에 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력한다.
#만약 수가 양수라면 동혁이는 그 개수 만큼 피스를 더해야 하는 것이고, 음수라면 제거해야 하는 것이다.
import sys

white = list(map(int,sys.stdin.readline().split()))

black = [1,1,2,2,2,8]

for i in range(6):
    need = [black[i] - white[i] for i in range(0,6)] #list comprehension, (조)
print(*need)