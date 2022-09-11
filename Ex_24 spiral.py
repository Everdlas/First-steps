n = int(input())
s = []
for i in range(n):
    s1 = []
    for j in range(n):
        s1.append(0)
    s.append(s1)
for i in range(n):  # 1 линия(вправо, n)
    s[0][i] = i + 1
q = n
for j in range(1, n - 1):  # первый спуск(n)
    q += 1
    s[j][n - 1] = q
for j in range(n - 1, -1, -1):  # первый налево(n)
    q += 1
    s[n - 1][j] = q
v = 0
while q != n ** 2:
    for i in range(n - 2 - v, v, -1):  # первый вверх(n-1)
        q += 1
        s[i][v] = q
    for i in range(1+v, n - 1 - v):  # первый вправо(n-1)
        q += 1
        s[1+v][i] = q
    for i in range(2 + v, n - 1 - v):  # второй вниз(n-2)
        q += 1
        s[i][n - 2 - v] = q
    for i in range(n - 3 - v, 0 + v, -1):  # второй влево(n-2)
        q += 1
        s[n - 2 - v][i] = q
    v += 1

# print(q)
for l in s:
    print(*l)
