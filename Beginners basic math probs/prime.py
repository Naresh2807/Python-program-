number=int(input("Enter the nuber"))
temp=number
a=[]
for i in range(1,number+1):
	if temp%i==0:
		a.append(i)
print(f"The divisors of {number} are {a}")
a_len=len(a)
if a_len==2:
	print("prime")
else:
	print("Not a prime")