n = int(input())
wm=0
wc=0
for i in range(n):
    m,c = map(int,input().split())
    if m>c:
        wm += 1
    elif c>m:
        wc += 1
if wm>wc:
    print('Mishka')
elif wc > wm:
    print('Chris')
else:
    print('Friendship is magic!^^')
