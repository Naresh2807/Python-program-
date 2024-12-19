import re

number = input("Enter the phone number: ")

if re.fullmatch(r"\d{10}", number):  
    print("The phone number is valid.")
else:
    print("The phone number is not valid.")
