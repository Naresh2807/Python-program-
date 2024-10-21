array=[1,2,3,4,5]
array_len=len(array)
last=array[array_len-1]
array.remove(last)
array_rotate=[]
array_rotate.append(last)
for i in array:
	array_rotate.append(i)
print(array_rotate)
