i = 0
ar = []
ar2 = []
ar3 = []
a = input()
a = a.replace(' ', '5')
while a[i] != '5':
	ar.append(a[i])
	i += 1
i = len(a)-1
while a[i] != '5':
	ar2.append(a[i])
	i -= 1
i = len(ar2)
while i > 0:
	i -= 1
	ar3.append(ar2[i])
print(*ar3, ' ', *ar, sep = '')
