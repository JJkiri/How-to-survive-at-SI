#알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
#팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다.
#level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.
#첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

#for문을 통한 일치여부 반복 검사(개별글자)
# 1 line, 1word, readline().rstrip
import sys
word = sys.stdin.readline().rstrip() # \n

l = len(word)
result = 1

# input값을 받을때 홀수, 짝수인경우를 나눠서 구현해야하는가?
for i in range(l//2): # str, list, range()... int is not iterable
    if word[i] == word[l-1-i]: #index number start from 0(zero)
        pass
    else:
        result = 0
        break
print(result)

#슬라이싱을 이용한 풀이

word = sys.stdin.readline().rstrip()
if word == word[::-1]:
    result = 1
else:
    result = 0
print(result)


