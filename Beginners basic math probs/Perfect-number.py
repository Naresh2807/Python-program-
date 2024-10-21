num=int(input("Enter the number"))
a=[]
rev=0
for i in range(1,num):
	if num%i==0:
		a.append(i)
		rev=rev+i
print(rev)