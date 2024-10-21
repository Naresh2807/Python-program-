#Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.

#Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.
 

#Examples :

#Input: n = 12
#Output: 2
#Explanation: 1, 2 when both divide 12 leaves remainder 0.
#Input: n = 2446
#Output: 1
#Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.
#Input: n = 23
#Output: 0
#Explanation: 2 and 3, none of them divide 23 evenly.
number=int(input("enter the number"))
temp=number

list1=[]
while(temp>0):
	res=temp%10
	if number%res==0:
		list1.append(res)

	temp=temp//10
c_set=set(list1)
if len(c_set)==0:
	print("the value is",0)
else:
    print("value",c_set)
