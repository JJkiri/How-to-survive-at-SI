#문제: 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다.
#숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
#숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
#상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
#할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

#입력:첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

#출력: 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

word = input() # 2 <= word <= 15
# TUV(8)까지는 3의 배수로 구분, else: wxyz는 9 처리 가능
# >> ascii/3으로 나눴을때, 몫에 따라  1~8까지 지정, else: 9 처리로


#ord('a') = 97 # b 98 c 99 32.3 32.6 33 i   if ord(alphabet) -32 = 1~ 9
#ord('a')-96 = 1
#(ord('a')-94) // 3) = additional_time
time = 0
#for i in word: # for i in word: 사용시, i 에는 str이 담기게 됨
#print(ord('A')) #65

#for i in range(len(word)):
    #if ord('P') <= ord(word[i]) <= ord('S'):
        #time += 2+6
    #elif ord('T') <= ord(word[i]) <= ord('V'):
        #time += 2+7
    #elif ord('W') <= ord(word[i]):
        #time += 2+8
    #else:
        #time += 2+((ord(word[i])-62) //3)

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in word: #word >>i(str)
    for j in range(len(dial)): #dial >> j(int)
        if i in dial[j]:
            time += 3+j #ABC index_num = 0, 3
print(time)

#ascii 활용 방법
EZ = '22233344455566677778889999'
for i in range(len(word)):
    time += int(EZ[(ord(word[i])-65)]) +1
print(time)