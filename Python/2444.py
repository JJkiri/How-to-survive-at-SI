n = int(input())
m = 2*n-1


# 목표 2(n-1) -1, 2n-1, 2(n-1) -1
for i in range(1,m+1,2):
    print(f'{'*' * i:^{m}}')


for i in range(m-2,0,-2): #start 포함, end 제외하는 python 성격을 고려, m+1 >> -2 (감소치부터) -1 (start반영)
    #range의 경우, -2해야 감소되는 range 순차실행 뒤에 1이 자동으로 붙어있음(기본은 생략)
    print(f'{'*' * i:^{m}}')

#^9의 자리에 2*n-1 를 넣는 법이 없을까?
#f-string에서는 중괄호 한번 더 사용해!

#백준은 오른쪽 끝 공백을 허용하지 않으므로, *앞에 공백을 넣어서 구현시도, 전체 너비 m - 별갯수 i를 뺀게 전체 공백의 수 // 앞공백은 /2
#공백 = (m - i) /2

for i in range(1,m+1,2): #위쪽
    print(" " * ((m-i)//2),"*"*i, sep="")

for i in range(m-2,0,-2): #아래쪽
    print(" " * ((m - i) // 2), "*" * i, sep="")