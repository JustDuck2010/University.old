ar = []
arb = []
q = 0
a = input()
ar = [int(x) for x in a.split()]
b = input()
arb = [int(x) for x in b.split()]
for i in range (len(ar)):
	for j in range (len(arb)):
		if arb[j] == ar[i]:
			q += 1
			break
print(q)