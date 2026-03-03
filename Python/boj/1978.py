#pesudo code
# key: factor, prime check until n **0.5, pair == math.sqrt() 
# nums = list(N)
# if nums % i != 0, status == not prime
# pass, status == prime >> count +=1

n = int(input())
nums = list(map(int,input().split()))

count = 0
# how can i

for i in nums: 
    if i ==1:
        continue
    n_status = True
    
    for j in range(2, int(i**0.5)+1): # n**0.5  <<need int, range only take int not float
        if i % j == 0:
            n_status = False
            break
            
    if n_status == True:
        count += 1    

print(count)