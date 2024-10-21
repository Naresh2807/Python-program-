array=[1,2,3,4,5,1,1,1,1]
array_len=len(array)
find_ele=1
count=0
for i in range(0,array_len):
	print(array[i])
	if array[i]==find_ele:
		print("count==",array[i])
		count=count+1

print(f'the count of{find_ele} in the array is {count}')