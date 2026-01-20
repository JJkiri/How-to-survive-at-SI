#목표: 주사위의 결과에 따른 상금 계산
#함수: 조건문
#포인트: 동일 눈이 3개인 경우 n*1,000 / 2개인 경우 1000+ n*100 / 모두 다른경우(1개인 경우) 가장 큰 눈 *100


#입력: 3 3 6
#출력: 1300

#오류1: 리스트에서 동일한 값을 세는 방법
#탐색1: for문과 if문을 조합해서 key(눈)과 value(등장횟수)를 기록한 dict를 생성

#오류2: dict에서 value가 제일 큰 값을 추출하는 방법
#탐색2: max_key = max(n, key=n.get) n-> key 순회 / key=n.get -> key의 value 기준으로 비교
#개선사항:

#채점1: list.append()는 값을 1개만 받음. -> dice_list[a,b,c]로 인풋값을 그대로 넣기


#save input to list
a, b, c = map(int,input().split())
dice_list = [a,b,c]
# dice_list.append(a,b,c) < list.append()는 변수 하나만 입력 가능 # 복습1


#list to dict
result = {}
for dice in dice_list:
    if dice in result: # dice(눈)= 동일한 값이 to result에(dict) 존재하는 경우 +1
        result[dice] += 1
    else:
        result[dice] = 1 # dice(눈) 이 동일한 값이 to result 없는 경우 = 최초

# 많이 등장한 눈의 등장 횟수
max_key = max(result, key=result.get) #가장 많이 등장한 눈 # 복습2
max_value = result[max_key] # 중복 눈의 등장 횟수
# 눈의 최대값
big_dice = max(dice_list) # 리스트에서 최대값 추출, 자료는 정수형

#상금 계산
if max_value ==1: # 중복눈이 없는 경우
    print(big_dice * 100)

# 동일눈 3개
elif max_value ==3:
    print(10000+ max_key*1000)

# 동일눈 2개
elif max_value ==2:
    print(1000+ max_key*100)
