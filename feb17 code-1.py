c=int(input('press 1 for odd\npress 2 for even\n'))
n=int(input('enter the value : '))
sum=0
for i in range(1,n+1) :
	if c==1:
		if i%2==1:
			sum=sum+i
	if c==2:
		if i%2==0:
			sum=sum+i
print(sum,'\n')


c=int(input('press 1 for odd\npress 2 for even\n'))
n=int(input('enter the value : '))
sum=0
for i in range(1,n+1) :
	if c==1:
		if i%2==1:
			sum=sum+i
	if c==2:
		if i%2==0:
			sum=sum+i
print(sum)