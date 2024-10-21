#You are given two integer numbers, the base a and the index b. You have to find the last digit of ab.

#Examples:

#Input: a = "3", b = "10"
#Output: 9
#Explanation: 310 = 59049. Last digit is 9.
#Input: a = "6", b = "2"
#Output: 6
#Explanation: 62 = 36. Last digit is 6.

number_a=int(input("Enter number a::"))
number_b=int(input("Enter number b::"))
power=number_a^number_b
last_digit=power%10
print(f"the last digit of a,b is {last_digit}")