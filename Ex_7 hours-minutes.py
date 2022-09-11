s=int(input("Введите кол-во секунд "))
h=s//3600
m=s//60-h*60
ss=s-h*3600-m*60
print(h,':',m,':',ss,sep='')
