#문제
#10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

#10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

#A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

#입력
#첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

#출력

#첫째 줄에 10진법 수 N을 B진법으로 출력한다.


n, b = input().split() #n = num, b = digits
n = int(n)
b = int(b)

digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = [] # 0이 아닌 이유> b진법을 "string"으로 저장해야되기 때문에, list형태로 구현, 단 '나머지'를 거꾸로 쌓아간다는점에 유의

#for문을 사용하지 못하는 이유, 나머지가 나오지 않을때까지 연산해야함 > while문
while n > 0:
    reminders = (n % b) #나머지를 앞의 자리부터 저장함, 진수변환 기능
    result.append(digit[reminders])
    n = (n//b) # 다음 나머지를 찾기 위해 n 갱신

result.reverse()

print(*result,sep="")
