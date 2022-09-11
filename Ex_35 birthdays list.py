s={}
while input() != 'конец':
    q = input().split(', ')
    s.setdefault(q[0], []).append(q[1])
# for i in s.values():
#     i.sort()
print(s)
