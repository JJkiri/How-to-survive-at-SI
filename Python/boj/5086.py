#pesudo code

# input = num1, num2

# case1 ) b%a == 0   factor
# case2 ) a%b == 0   multiple
# case3 ) neither case1 nor case2    neither

while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')