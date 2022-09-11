a=int(input())
b=list(map(int,input().split()))
def rec(q):
    if len(q) == 1:
        return q[0]
    return rec()
print(rec(b))
print(b)
