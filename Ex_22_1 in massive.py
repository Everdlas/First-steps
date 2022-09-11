a = []
for i in range(5):
    a.append(list(map(int, input().split())))
n = 0
i = 2
j = 3
while a[2][2] != 1:
    for i in range(5):
        for j in range(5):
            if a[i][j] == 1:
                # print(i, j)
                if j > 2:
                    n += 1
                    a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
                    # print(a)
                elif j < 2:
                    n += 1
                    a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
                    # print(a)
                elif i < 2:
                    n += 1
                    a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
                    # print(a)
                elif i > 2:
                    n += 1
                    a[i][j], a[i - 1][j] = a[i - 1][j], a[i][j]
                    # print(a)
                else:
                    break
print(n)
