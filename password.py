import re

password = input("Enter the password: ")
if re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}', password):  
    print("valid.")
else:
    print("not valid")
