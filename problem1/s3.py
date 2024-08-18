p=[1,2]
l=[2,3]
p.sort()
list1=p
l.sort()
list2=l
list1=set(list1)
list2=set(list2)
print("yes") if(list1==list2) else print("no")