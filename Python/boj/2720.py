#greedy
t = int(input()) #test case number

#cent  / qurter, dime, nikel, penny

coins = [25,10,5,1] #cent

for i in range(t): #testcase num repeat
    c = int(input()) # cent

    #maximize big coins
    q = c//coins[0] # qurter
    c = c% coins[0] # remain cent

    d = c//coins[1] # dime
    c = c%coins[1]

    n = c//coins[2] # nikkel
    c = c%coins[2]

    p = c//coins[3] #penny

    print(q,d,n,p)