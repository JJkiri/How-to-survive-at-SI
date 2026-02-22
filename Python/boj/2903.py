#2903

#요구: 점의 갯수 count:  9(3제곱) , 25(5제곱) , 81(9제곱)  (1) 3(+2) (2) 5(+4) (3) 9(+8) 17

#의사코드

#input: n
#side_point = 2^n +1 (= +2, +4, +6, +8...)
#total_point = side^2
#print total_point

#ans

n = int(input())

side_point = 2**n+1

total_point = side_point**2

print(total_point)
