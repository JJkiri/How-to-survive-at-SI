#구구단
#출력형식과 같게 N*1부터 N*9까지 출력한다. , 각 단별로 줄띄움이 되어 있다.

n = int(input())
for i in range(1,9+1):
    print(n,'*',i,'=',n*i)
