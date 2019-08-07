file = open("in.txt", 'r')
lineArr = file.readlines()
#for line in lineArr:
#	print(line)

def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)

def f(n, k):
	if k==0:
		return fact(n)
	return f(n, k-1) - f(n-1, k-1)

print(f(4,1))
for i in range(1,18):
	for j in range(1, i+1):
		print(i, j, f(i,j))
