#한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다. 또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다.
#심심해진 영석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.

#>> 5줄은 고정

import sys

board = []
for i in range(5):
    word = list(sys.stdin.readline().strip()) #5줄을 입력받음, 글자를 하나씩 받아야함, 최대 15글자, list()는 str을 한글자씩 저장함
    board.append(word) #한글자씩 리스트로 담는다



# board = [[word1],[word2],[word3]..[word5]]
for c in range(15): #열부터 읽어본다. 최대 15열!!
    for r in range(5): #5행 반복
        if c <len(board[r]): #r행의 길이보다 c가 짧을때, (글자가 존재하는경우만)
            print(board[r][c],end = "")
