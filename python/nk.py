string = input("Enter the string: ")  # hello
add = input("Find character: ")  # l

print("Original String:", string)

add1 = [ ]

for i in string:
    if i == add:
        add1.append(i)

print("Count of'", add, "' in the string:", len(add1))
print("Matching characters:", add1)

