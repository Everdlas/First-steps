a=int(input())
b=0                 #Кол-во в последнем ряде
c=0                 #Кол-во рядов
while a>b and a>0:
    c=c+1
    b=b+c
    a=a-b
    #print('c=',c)
    #print('b=',b)
   # print('a=',a)
if a<0:
    print(c-1)
else:
    print(*result)
