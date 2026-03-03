#pesudo code

#1 n % k == 0, k == ans.
#2 list(ans) write answers
#3 k1, k2, k3 ... ans[k] print.

n, k = map(int,input().split())

ans = []
for i in range(1,n+1):
    if n % i ==0: #1
        ans.append(i) #2
try:
    print(ans[k-1]) #3
except:
    print('0')