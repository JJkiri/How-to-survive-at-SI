#위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를
#주소로 매길 수 있다.
# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오.
# 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

#문제: 1-(+5) / 2-6(+6) / 3-12... 6, 12, 18, 24 6n만큼 테두리의 방 갯수 증가

#의사코드
# input = n은 목표하는 방, 정수

# 방의 개수(ans) = 구간의 위치

# 6^0 + 6^1 ... = .. (ans)

#layer 1(1) = 1, layer2(7) = 1 + 6*1 + 6*2...
# layer = 1 + 6*1... 6*x , >> for i in range(x): >> while true
# if n < layer, x+1

# output = print(x) #방의 갯수, 층

n = int(input())

layer = 1
max_room_layer = 1

while n > max_room_layer:
    max_room_layer = max_room_layer + 6*layer
    layer = layer+1

print(layer)