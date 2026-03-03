#문제: 입력 받은 대로 출력하는 프로그램을 작성하시오.

#입력: 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, (limit)
# 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. (limit)
# 각 줄은 100글자를 넘지 않으며,
# 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

#출력: 입력받은 그대로 출력한다.


# stdin.read
# try-except
import sys

#while True: input값의 개수를 모를때

#stdin >> for문 조합시 한줄씩 계속 끄집어냄 >> 인풋값의 개수를 모를때
#stdin.readline() 한줄만 끄집어냄 >> 첫째, 둘째 등 줄 수를 알때
#stdin.read()모든 줄을 '한문자열'에 불러옴


for i in sys.stdin: #input load, \n base, 줄이 여러개이므로 for문 사용 가능
    print(i.rstrip90)

while True:
    word = sys.stdin.readline() #1줄 for문 불가 , while로 돌려줘야함
    print(word.rstrip())
    if not word.rstrip():
        break