ar = []
arb = []
a = input()
ar = [int(x) for x in a.split()]
for i in range (len(ar)):
	if ar[i]>ar[i-1]:
		arb.append(ar[i])
print(*arb)