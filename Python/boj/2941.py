#첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
#단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

#입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

#Testcase ljes=njak

# len(cro_word)

word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 리스트 정의

for i in croatia:
    word = word.replace(i,'*')  # list 단어를 word에서 전환, in croatia 리스트의 요소들을 하나씩 돌면서 감사
    #replace(str, target) str >> target으로 교체함, str은 immutable 이므로, replace는 새로운 문자열을 반환할 뿐임

print(len(word))