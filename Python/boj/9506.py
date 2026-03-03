while True:
    n = int(input())
    
    if n == -1:
        break
    
    divisors = [] 
    
    # √n까지만 검사
    for i in range(1, int(n ** 0.5) + 1): #math.sqrt(n)
        
        if n % i == 0:
            divisors.append(i)
            
            pair = n // i
            
            if pair != i and pair != n:  # sqrt and itself exception handlig
                divisors.append(pair)
    
    divisors.sort()
    
    if sum(divisors) == n:
        print(f'{n} = '+" + ".join(map(str,divisors))) #join only work at str
    else:
        print(f'{n} is NOT perfect.')