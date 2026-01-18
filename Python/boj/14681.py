#문제: 사분면 찾기
#함수: 조건문
#포인트: case 별 조건문 작성

#입력: 12 \n 5

a = int(input())
b = int(input())

if a>0 and b > 0:
    print('1')
elif a<0 and b>0:
    print('2')
elif a<0 and b<0:
    print('3')
elif a>0 and b<0:
    print('4')
