ar = []
q = 0
a = input()
ar = [int(x) for x in a.split()]
for i in range (len(ar)):
	f = 0
	for j in range (i-1, -1, -1):
		if ar[j] == ar[i]:
			print("Да")
			f = 1
			break
	if f == 0:
		print("Нет")