number=int(input("Enter the number"))#153
temp=number
number_len=str(number)
number_len=len(number_len)
rev=0
rel=0
while (temp>0):
	rev=temp%10
	print("rev",rev)
	rel=(rel)+(rev**number_len)
	print("rev",rel)
	temp=temp//10
if number==rel:
	print("True it is armstrong",number)
else:
	print("False it it not a armstrong",number)