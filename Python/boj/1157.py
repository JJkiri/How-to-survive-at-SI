#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

import sys
word = sys.stdin.readline().upper().rstrip() # upper()로 통일, 대소문자 구분 불필요

#중복제거의 경우 set{} 활용<<
#set은 index가 없으므로 list로 index 부여
alphabet_list = list(set(word))

count_list = [] # alphabet_list에서 count한 value 저장목적으로 생성
for i in alphabet_list:
    count_list.append(word.count(i)) # word.count(i) // alphabet_list 순서대로, count_list에 value 저장

if count_list.count(max(count_list)) > 1: #max(count_list) >1 인경우, maxvalue가 중복이라는뜻
    print("?")
else:
    print(alphabet_list[count_list.index(max(count_list))]) #count_list (value) index num = alphabet_list index num(key) 일치시키기
    # (1) max(count_list)의 .index() 추출
    # (2) alphabet_list에서 가져오기

