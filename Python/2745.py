#B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
#10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
#A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
#ord(A) = 65
# unicode num으로 > ord / chr

#첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
#B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.

#첫째 줄에 B진법 수 N을 10진법으로 출력한다.
import sys
n, b = sys.stdin.readline().split()

b = int(b)
result = 0
#tip: reversed(n) is iterator , cant indexing ( reversed(n)[i] XX)
for ch in n:
    if '0' <= ch <= '9': #문자열 대소 비교 가능, 알파뱃은 숫자문자열 보다 큰가?  > 모두 유니코드로 하면 되겠지뭐
        temp = (ord(ch) - ord('0'))
    else:
        temp = (ord(ch) - ord('A') + 10) #'A' = 10
    result = result*b + temp #(1)기존 숫자가 자릿수 늘어날때 b를 곱하고, (2)temp를 더한다 (3)다음에는 기존숫자가 36진법으로 늘어나고(*b) temp 더해질것!
print(result)

