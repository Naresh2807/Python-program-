array=[0,0,0,1,1,2,2]

a0=0
a1=0
a2=0
for i in array:
	if i == 0:
	    a0=a0+1
	elif i==1:
	    a1=a1+1
	elif i==2:
	    a2=a2+1
	else:
		pass
array=[]
for i in range(1,a0+1):
	array.append(0)
for i in range(1,a1+1):
	array.append(1)
for i in range(1,a2+1):
	array.append(2)
print(array)