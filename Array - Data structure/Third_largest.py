def third(num):
	if len(num)<3:
		return -1
	dub=set(num)
	dub_len=len(dub)
	print(dub_len)
	if dub_len <3:
		return -1
	sort_num=sorted(num)
	return sort_num[2]
num=[5,5,5]
print(third(num))