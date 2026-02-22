#2869

#pesudocode

#입력
#첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# input = A(up), B(down), V(goal)

#dont use while(check), timelimit 0.25sec cant bear it.

#net climbing: a-b
#(d-day -1) v-a

#   (v-a) % (a-b) +1(ceil, they have reamins) = day -1 (always, -a part)




#출력
#첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

a, b, v = map(int,input().split())

#check
if v <= a:
    print(1)
else:
    day = (v - a) // (a - b) + 1
    if (v-a) % (a-b) !=0:
        day += 1
    print(day)