a=-1
b=1
d=0
n=int(input('enter the fibonacci range : '))
for i in range(1,n+1):
    c=a+b
    print(c,'+')
    d=d+c
    a=b
    b=c
print(f'= {d} //is the sum of fibonacci values') 