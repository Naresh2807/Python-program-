a=int(input("Enter units:"))
if a<=100:
	print("Bill amount: 0")
elif(a>=101 and a<200):
	a=a-100
	print("Bill amount:",a*2)
else:
	print("Bill amount:",((((a-100)-100))*5+(200)))