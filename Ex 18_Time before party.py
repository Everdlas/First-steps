n1,k = map(int,input().split())
i = [1,2,3,4,5,6,7,8,9,10]
n = i[0:n1]
TL=240-k
s=0
T=0
while T<=TL and 0<=s<=n[-1]:
    s=s+1
    t1=5*s
    T=T+t1
if TL>=0:
    print(s-1)
else:
    print(s)

