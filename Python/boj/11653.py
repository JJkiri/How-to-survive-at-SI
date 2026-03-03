#pesudo code
# n % 2,3,5,7,9 ... > +
# n // i add to ans_list

n = int(input())
ans_list = []
i = 2

while i <= n: # ** end point i = n
    if n % i == 0: #pass
        n = n // i
        ans_list.append(i)
    else:
        i += 1

ans_list.sort()

# print line to line > for x in list:!
if ans_list: #mean ans_list has value (like True)// #if n =1 , list = [] because while 2 <= 1 == False
    for x in ans_list:
        print(x)
     