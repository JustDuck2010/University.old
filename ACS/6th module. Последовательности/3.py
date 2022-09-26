ar = []
arb = []
a = input()
ar = [int(x) for x in a.split()]
for i in range (1, len(ar), 2):
	arb.append(ar[i])
	arb.append(ar[i-1])	
print(*arb)