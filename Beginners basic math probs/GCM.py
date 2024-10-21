# The GCD (Greatest Common Divisor) of two numbers is the largest number that divides both of them without leaving a remainder.

N = int(input("Enter the first number: "))
M = int(input("Enter the second number: "))

if M == 0:
    print(f"The GCD is {N}")  
else:
    while M != 0:
        N, M = M, N % M  

    print(f"The GCD is {N}")  
