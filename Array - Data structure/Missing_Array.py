num=5
array=[1, 2, 3, 5]

if num==len(array):
    print("No missing in array")
else:
    print("Missing")
    for i in range(1,num+1):
        if i not in array:
            print(f"Missing number:{i}")
