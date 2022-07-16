a=int(input())
b=int(input())
c=int(input())
Sum1 = a+b+c
Sum2 = a+b*c
Sum3 = a*b+c
Sum4 = (a+b)*c
Sum5 = a*(b+c)
Sum6 = a*b*c
print(max(Sum1,Sum2,Sum3,Sum4,Sum5,Sum6))
