number=int(input("Enter the number"))
temp=number
rev=0
rel=0
while(temp>0):
	rev=temp%10
	rel=(rel*10)+(rev)
	temp=temp//10
if number==rel:
	print("the number is palindrome",rel)
else :
	print("the number is not palindrome",rel)