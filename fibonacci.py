n=int(input("enter n terms for fibonacci series: "))
if n<=0:
	print("Invalid input, please enter a positive value")
else:
	t1,t2,t3=0,1,0
	print(t1,t2,end=" ")
	for i in range(n+1):
		t3=t1+t2
		t1=t2
		t2=t3
		print(t3,end=" ")