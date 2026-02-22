#1193

#이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

#pesudocode

#input x

# board의 크기는 무한이므로 미리 만들지는 않음

#layer = n
#x(횟수) x이 포함하는 횟수 = 1+2+...n.. for i in range(n): x += i

# layer가 포함하는 구간에서 멈춘경우, 연산을 수행함

# 전단계의 시작지점 n = n-layer
# idx(위치) = x -(n-layer) , 만약 x =8이면, idx 는 8 -(10-4) = 2가 된다.(층에서 움직임)

# 짝수층인경우, 1/층(layer) >> 층/1로 (왼쪽 아래로)
# 홀수층인경우, 층/1 >> 1/층으로 (오른쪽 위로)

#x가 주어졌을때, row와 column을 구한 뒤 "row/column" 수행


x = int(input())

layer = 1 # 짝수층인경우, 1/층(layer) >> 층/1로 (왼쪽 아래로)
n = 1 #누적합, layer가 포함하는 x의 구간

while x > n:
    layer += 1
    n += layer

idx = x -(n-layer)

if layer %2 == 0:
    r = idx
    c = layer - idx + 1
else:
    r = layer - idx + 1
    c = idx

print(f'{r}/{c}')



