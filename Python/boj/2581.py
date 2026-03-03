#pesudo code
# make num list n~m
# pick prime, 
# add to ans_list = []
# summary ans_list

m = int(input())
n = int(input())

nums = list(range(m,n+1)) #list comprehension


ans_list = []
for i in nums:
    n_status = True #True mean Prime
    
    if i == 1: #Exception Handling
        n_status = False
        
    for j in range(2, int(i**0.5)+1): #Prime test ##remember, range cant take float( n**0.5)
        if i % j == 0:
            n_status = False
            break
    
    if n_status == True: #Prime add to ans
        ans_list.append(i)

if ans_list == []:
    print('-1')
else:
    print(sum(ans_list))
    print(min(ans_list))
       
            