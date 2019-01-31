
def cal (a, b, o,):
	if o =="+":
		print (a+b)
	else:
		print(a-b)

l=int(input("enter limit: "))
for i in range(0, l):
	x = int (input("enter value: "))
	y = int (input("enter value: "))
	z = input("enter + or -: ")
	cal(a=x, b=y, o=z)