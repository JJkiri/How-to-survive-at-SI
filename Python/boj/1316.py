#그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

#첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

#첫째 줄에 그룹 단어의 개수를 출력한다.
import sys
n = int(sys.stdin.readline().strip()) #단어의 개수 n


#(1) 이전 글자를 기억한다.

#(2) 지금까지 등장했던 글자를 저장한다.

count = 0 #그룹단어의 수

for i in range(n):
    word = sys.stdin.readline().strip() #n번의 입력을 받아내는 word 변수

    prev = None #공백 만들기
    checked = [] #이전에 검사한 글자들 저장하기, list 아닌 set로 하자 중복 의미없음
    status = True # 문제없음

    #검사하는 1단어 단위
    for j in word: #단어알파뱃 검사를 수행
        if j != prev: #직전 단어와 다른 경우
            if j in checked: #검사한 글자에 있는 경우
                status = False # 실패
                break # 검사 종료
            else:
                pass # true 유지
            checked.append(j) #검사가 끝났으면 j에 추가

        prev = j # for문 돌릴때 항상 직전단어 교체
    if status == True: #for문 검사 돌려서 상태가 True일때,
        count += 1 # 그룹단어수 추가

# count의 출력
print(count)







