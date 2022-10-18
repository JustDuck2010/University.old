a = input()
ar = [x for x in a]
ab = []
f = 0
q = a.count('h')
for i in range(len(ar)):
	if ar[i] == 'h':
		f += 1
	if 1 <= f < q:
			continue
	ab.append(ar[i])
print(*ab)
#join() - метод