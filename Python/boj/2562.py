#문제: 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#예를 들어, 서로 다른 9개의 자연수
#3, 29, 38, 12, 57, 74, 40, 85, 61
#이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

#입력:첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

#출력: 첫째 줄에 최댓값을 출력하고, (줄구분) 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

import sys
a = list(map(int,sys.stdin.read().split())) #여러줄의 입력은 readline()으로 읽기 힘들다!, 실행시 ctrl+z / 엔터 누를것
#read()는 여러줄의 입력을 전부 받음
#응용: asterisk 사용
# asterisk *>>> a, *data = map(int, sys.stdin.read().split())
# a = 5 / *data = [ 6, 8, 9,  11] 등 나머지 인자를 받을 수 있음


#list value를 통해 index를 반환하는 법?
#list.index(value)
print(a)
print(a.index(max(a))+1)