n=121
temp=n
rem=0
rev=0
while temp != 0:
    rem = temp % 10#1
    rev = rev * 10 + rem#12*10=120+1=121
    temp = temp / 10

if n == rev:
	print("pal")
else:
	print("not pal")


s="heeh"
a=s[::-1]

if (a==s):
	print("pal")
else:
	print("not pal")
yolo predict model=yolo11n.pt source='images_large_07_13_11511_06a.jpeg'