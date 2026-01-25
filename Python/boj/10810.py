#문제: 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다.
# 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
# 도현이는 앞으로 M번 공을 넣으려고 한다. 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.
# 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.
# 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.

#입력:첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 각 방법은 세 정수 i j k로 이루어져 있으며, i번 바구니부터 j번 바구니까지에
# k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 넣는다.

#출력: 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.

# basket = list(name) or dict(key) ? > N
# ball = value >> M

# input

n, m = map(int,(input().split())) # 바구니 n개와 공을 넣을 횟수 m

# list 생성
basket = []
for x in range(0,n): # index = key, value = base(0) list 생성
    basket.append(0)
# basket = [0] * n 으로 간략화 가능

for x in range(0,m): #m번동안 공을 넣을거다
    #i 부터 j까지 k공을 넣는다
    i, j, k = map(int, (input().split()))
    for y in range(i-1,j): # list index start from 0, > basket number (input) start from 1
        basket[y] = k

#output
print(" ".join(map(str,basket)))

#print(*basket) # list를 문자열로 바꿔서 출력하는 법?
    #1:"구분자" join(list) > str만 가능, map(str,list) 필요 //
    #2 print(*list)사용시 단순공백출력


#폐기: dict로 key, value가 아닌 list+index사용 / 연속된 숫자이므로 굳이 key 지정 필요 없음

#basket = {}

#for key in range(1,n+1): # n>= 1 이므로 range 범위 주의
    #basket[key] = 0 #append는 안됨, dict_name[key] = value 로 key 추가 가능, 항상 value가 쌍으로 있어야함

#for value in range(0,m):
    #basket



# output, print

