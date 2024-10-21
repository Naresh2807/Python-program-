array=[1,2,3,4,5]
array_len=len(array)
rotate=2
array_rotate=[]
for i in range(0,rotate):
	il=array[i]
	array.append(il)
	array_rotate.append(il)
for i in array_rotate:
	array.remove(i)

print(array)
