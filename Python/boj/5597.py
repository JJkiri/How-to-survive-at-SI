#문제: X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
#교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

#입력: 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

#출력: 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

#input = line * 28
#object = list로 나열

all_list = list(range(1,30+1))

while True:
    try:
        all_list.remove(int(input()))
    except:
        break

    #attend_list = [int(input())]# input을 계속 받으며 int형으로 list add << 이건 아닌거같다



#output
all_list.sort() # 찾기위해 정렬
print(all_list[0])
print(all_list[1]) # 두번째로 작은 수를 출력하는 방법은 뭐지?

