ar = []
arb = []
a = input()
ar = [int(x) for x in a.split()]
min = ar[0]
max = ar[0]
mini = 0
maxi = 0
for i in range (len(ar)):
	if ar[i] < min:
		min = ar[i]
		mini = i
	if ar[i] > max:
		max = ar[i]
		mini = i
for i in range (len(ar)):
	if i == mini:
		arb.append(ar[maxi])
	elif i == maxi:
		arb.append(ar[mini])
	else:
		arb.append(ar[i])
print(*arb)