a = int(input())
for i in range(2, a//2+1):
	if a%i == 0:
		print(i)
		break

'Дано целое число не меньше 2\
Напечатайте наименьший целочисленный делитель данного числа больший 1'