#Problem statement
#Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
#For example:
#'N' = 5.
#The divisors of 5 are 1, 5.

number=int(input("Enter the nuber"))
temp=number
a=[]
for i in range(1,number+1):
	if temp%i==0:
		a.append(i)
print(f"The divisors of {number} are {a}")
