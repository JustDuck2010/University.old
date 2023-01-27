a = input()
ar = [int(x) for x in a.split()]
print(ar[2])
x = len(ar)
print(ar[x-1])
for i in range(5):
	print(ar[i], end = ' ')
print('')
for i in range(len(ar)-2):
	print(ar[i], end = ' ')
print('')
for i in range(0, len(ar),2):
	print(ar[i], end = ' ')
print('')
for i in range(1, len(ar),2):
	print(ar[i], end = ' ')
print('')
for i in range(len(ar)-1, -1, -1):
	print(ar[i], end = ' ')
print('')
for i in range(len(ar)-1, -1, -2):
	print(ar[i], end = ' ')
