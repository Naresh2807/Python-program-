array_1=[1,1,2,6,4,11,3,12,55]
array_2=[1,2,3]
array_1=set(array_1)
array_1=list(array_1)
array_2=set(array_2)
array_2=list(array_2)
array_out=[]
for i in range(0,len(array_2)):
    if array_2[i] not in array_1:
    	array_out.append(0) 
    else:
	    array_out.append(1)
if 0 not in array_out:
	print("true")
else:
	print("False")