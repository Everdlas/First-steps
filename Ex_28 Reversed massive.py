n, m = map(int,input().split())
s = []
q=0
for i in range(n):
    s1=[]
    for j in range(m):
        s1.append(q)
        q +=1
    s.append(s1)
# print(s)
for i in range(n):
    if s.index(s[i]) % 2 != 0:
        s[i].reverse()
for i in range(n):
    print(*s[i])
