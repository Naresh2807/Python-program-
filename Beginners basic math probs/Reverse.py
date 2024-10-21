###You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.

#Example 1:

#Input: 200
#Output: 2
#Explanation: By reversing the digits of 
#number, number will change into 2.
#Example 2:

#Input : 122
#Output: 221
#Explanation: By reversing the digits of 
#number, number will change into 221.###

number=int(input("Enter the nuber::"))
temp=number
res=0
rev=0
number_1=str(number)
number_2=len(number_1)
for i in range(1,number_2):
    if temp%10==0:
    	temp=temp//10
    	print(temp)
while (temp>0):
    res=temp%10
    rev=(rev*10)+res
    temp=temp//10
print(f"the reverse is {rev}")

###or####@2 method
num=input("enter the number::")
num1=num[::-1]
num=int(num1)
print(num)



